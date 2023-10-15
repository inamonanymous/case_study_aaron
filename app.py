from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from model import db, Users, LaundryList, LaundryCategories, LaundryItems, SupplyList, Inventory
import datetime
from sqlalchemy.orm import aliased

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/laundry_aaron'
db.init_app(app)
app.secret_key = 'ajdshfaskdjhf'

@app.route('/delete_user/<int:id>', methods=['POST', 'GET'])
def delete_user(id):
    if 'username' in session:
        target_obj = Users.query.filter_by(id=id).first()
        if target_obj:
            db.session.delete(target_obj)
            db.session.commit()
            return redirect('/option/option7')
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/edit_user', methods=['GET'])
def edit_user():
    if 'username' in session:
        id, name, username, password = request.form['id'], request.form['name'], request.form['username'], request.form['password']
        target_obj = Users.query.filter_by(id=id).first()
        if target_obj:
            check_user = Users.query.filter_by(username=username).first()
            if check_user:
                return f"username exists"
            target_obj.name = name
            target_obj.username = username
            target_obj.password = password
            db.session.commit()
            return redirect('/option/option7')
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/edit_existing_user/<int:id>', methods=['GET'])
def edit_existing_user(id):
    if 'username' in session:
        users_obj = Users.query.filter_by(id=id).first()
        return render_template('edit_supply_form.html', obj=users_obj)
    return redirect(url_for('index'))

@app.route('/delete_supply/<int:id>', methods=['POST', 'GET'])
def delete_supply(id):
    if 'username' in session:
        target_obj = SupplyList.query.filter_by(id=id).first()
        db.session.delete(target_obj)
        db.session.commit()
        return redirect('/option/option4')
    return redirect(url_for('url_for'))

@app.route('/edit_supply', methods=['POST', 'GET'])
def edit_supply():
    if 'username' in session:
        id, name = request.form['id'], request.form['name']
        target_obj = SupplyList.query.filter_by(id=id).first()
        target_obj.name = name
        db.session.commit()
        return redirect('/option/option4')
    return redirect(url_for('index'))

@app.route('/edit_existing_supply/<int:id>', methods=['GET'])
def edit_existing_supply(id):
    if 'username' in session:
        suppply_obj = SupplyList.query.filter_by(id=id).first()
        return render_template('edit_supply_form.html', obj=suppply_obj)
    return redirect(url_for('index'))


@app.route('/delete_category/<int:id>', methods=['POST', 'GET'])
def delete_category(id):
    if 'username' in session:
        target_obj = LaundryCategories.query.filter_by(id=id).first()
        db.session.delete(target_obj)
        db.session.commit()
        return redirect('/option/option3')
    return redirect(url_for('index'))

@app.route('/edit_category', methods=['POST', 'GET'])
def edit_category():
    if 'username' in session:
        id, name, price_kg = request.form['id'], request.form['name'], request.form['price_kg']
        target_obj = LaundryCategories.query.filter_by(id=id).first()
        target_obj.name=name
        target_obj.price=price_kg
        db.session.commit()
        print(target_obj.price)
        return redirect('/option/option3')
    return redirect(url_for('index'))

@app.route('/edit_existing_category/<int:id>', methods=['GET'])
def edit_existing_category(id):
    if 'username' in session:
        category_obj = LaundryCategories.query.filter_by(id=id).first()
        return render_template('edit_category_form.html', obj=category_obj)
    return redirect(url_for('index'))

@app.route('/delete_laundry/<int:id>', methods=['POST', 'GET'])
def delete_laundry(id):
    if 'username' in session:
        target_laundry_list_obj = LaundryList.query.filter_by(id=id).first()
        target_laundry_item_obj = LaundryItems.query.filter_by(laundry_id=id).first()
        db.session.delete(target_laundry_item_obj)
        db.session.delete(target_laundry_list_obj)
        db.session.commit()
        return redirect('/option/option2')
    return redirect(url_for('index'))

@app.route('/edit_laundry', methods=['POST', 'GET'])
def edit_laundry():
    if 'username' in session:
        id, customer_name, status, queue, pay_status, amount_tendered, remarks = request.form['id'], request.form['customer_name'], request.form['status'], request.form['queue'], request.form['pay_status'], request.form['amount_tendered'], request.form['remarks']
        laundry_obj = LaundryList.query.filter_by(id=id).first()
        if pay_status=="1":
            if float(amount_tendered) < laundry_obj.total_amount:
                return redirect(url_for('dashboard'))
            laundry_obj.amount_change = int(amount_tendered) - laundry_obj.total_amount
            laundry_obj.cutomer_name=customer_name
            laundry_obj.status=status
            laundry_obj.pay_status=1
            laundry_obj.queue=queue
            laundry_obj.amount_tendered=amount_tendered
            laundry_obj.remarks=remarks    
            db.session.commit()
            print(f"from inside: {pay_status} {type(pay_status)}")
            return redirect('/option/option2')
        elif pay_status=="0":
            laundry_obj.cutomer_name=customer_name
            laundry_obj.status=status
            laundry_obj.queue=queue
            laundry_obj.remarks=remarks
            db.session.commit()
            print(f"from elif: {pay_status} {type(pay_status)}")
            return redirect('/option/option2')
    print(f"from other outside: {pay_status} {type(pay_status)}")
    print(pay_status=="1")
    print(pay_status=="0")
    return redirect(url_for('index'))

@app.route('/edit_existing_laundry/<int:id>')
def edit_existing_laundry(id):
    if 'username' in session:
        laundry_obj = LaundryList.query.filter_by(id=id).first()
        return render_template('edit_laundry_form.html', obj=laundry_obj)
    return redirect(url_for('index'))

@app.route('/save_user', methods=['POST', 'GET'])
def save_user():
    if 'username' in session:
        current_user = Users.query.filter_by(username=session.get('username', "")).first()
        if current_user.type==1 and request.method=="POST":
            name, username, password, type = request.form['name'], request.form['username'], request.form['password'], request.form['type']
            
            check_user = Users.query.filter_by(username=username).first()
            if check_user:
                return "user already registered"

            user_entry = Users(name=name, username=username, password=password, type=type)            
            db.session.add(user_entry)
            db.session.commit()
            return redirect('/option/option7')
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/manage_inventory', methods=['POST', 'GET'])
def manage_inventory():
    if 'username' in session:
        supply_id, supply_type, supply_qty = request.form['supply_name'], int(request.form['supply_type']), int(request.form['supply_qty'])
        inventory_obj = Inventory.query.filter_by(supply_id=supply_id, main=1).first()
        print(inventory_obj.qty)
        if supply_type==1:
            inventory_entry = Inventory(
                supply_id=inventory_obj.supply_id,
                qty=supply_qty,
                stock_type=1,
                date_created=datetime.datetime.now(),
                main=0
            )
            inventory_obj.qty+=inventory_entry.qty
            db.session.add(inventory_entry)
            db.session.commit()
            return redirect('/option/option5')
        if supply_qty<inventory_obj.qty:
            inventory_entry_outside = Inventory(
                    supply_id=inventory_obj.supply_id,
                    qty=supply_qty,
                    stock_type=0,
                    date_created=datetime.datetime.now(),
                    main=0
                )
            inventory_obj.qty-=inventory_entry_outside.qty
            db.session.add(inventory_entry_outside)
            db.session.commit()
            return redirect('/option/option5')
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/save_supply', methods=['POST', 'GET'])
def save_supply():
    if 'username' in session:
        supply = request.form['supply']
        if supply:
            supply_entry = SupplyList(name=supply)
            db.session.add(supply_entry)
            db.session.commit()
            inventory_entry = Inventory(supply_id=supply_entry.id,
                                        qty=0,
                                        stock_type='',
                                        date_created=datetime.datetime.now(),
                                        main=1)
            db.session.add(inventory_entry)

            db.session.commit()
            return redirect('/option/option4')
        return redirect('/option/option4')
    return redirect(url_for('index'))

@app.route('/save_laundry_category', methods=['POST', 'GET'])
def save_laundry_category():
    if 'username' in session:
        category, price_kg = request.form['category'], request.form['price_kg']
        if category:
            laundry_category_entry = LaundryCategories(
                name=category,
                price=price_kg
            )
            db.session.add(laundry_category_entry)
            db.session.commit()
            return redirect(url_for('/option/option3'))
        return redirect('/option/option3')
    return redirect(url_for('index'))

@app.route('/save_laundry', methods=['POST', 'GET'])
def save_laundry():
    if request.method == 'POST' and 'username' in session:
        # Get data from the form
        customer_name = request.form['customer_name']
        remarks = request.form['remarks']
        laundry_category = request.form['laundry_category']
        weight = request.form['weight']
        amount = request.form['amount']  # This will be the calculated amount
        try:
            paid = request.form['paid']
            
            if paid:
                amount_from_cus, change = float(request.form['amount_from_cus']), float(request.form['change'])
                if change<0 or amount_from_cus is None:
                    return redirect(url_for('dashboard'))
                laundry_list_entry = LaundryList(
                    customer_name=customer_name,
                    status=0,
                    queue=1,
                    total_amount=amount,
                    pay_status=paid,
                    amount_tendered=amount_from_cus,
                    amount_change=change,
                    remarks=remarks,
                    date_created=datetime.datetime.now()
                )

                laundry_category_obj=LaundryCategories.query.filter_by(name=laundry_category).first()
                db.session.add(laundry_list_entry)
                db.session.commit()
                laundry_item_entry = LaundryItems(
                    laundry_category_id=laundry_category_obj.id,
                    weight=weight,
                    laundry_id=laundry_list_entry.id,
                    unit_price=laundry_category_obj.price,
                    amount=amount
                )

                db.session.add(laundry_item_entry)
                db.session.commit()
                return redirect('/option/option2')

        except:
            laundry_list_entry = LaundryList(
                customer_name=customer_name,
                status=0,
                queue=1,
                total_amount=amount,
                pay_status=0,
                amount_tendered=0,
                amount_change=0,
                remarks=remarks,
                date_created=datetime.datetime.now()
            )

            laundry_category_obj=LaundryCategories.query.filter_by(name=laundry_category).first()
            db.session.add(laundry_list_entry)
            db.session.commit()
            laundry_item_entry = LaundryItems(
                laundry_category_id=laundry_category_obj.id,
                weight=weight,
                laundry_id=laundry_list_entry.id,
                unit_price=laundry_category_obj.price,
                amount=amount
            )
            # Add and commit the entry to the database
            
            db.session.add(laundry_item_entry)
            db.session.commit()

            # Redirect to the desired page after processing
            return redirect('/option/option2')
    return redirect(url_for('index'))

@app.route('/get_laundry_data', methods=['GET'])
def get_laundry_data():
    if 'username' in session:
        laundry_categories_all = LaundryCategories.query.all()
        selected_category = request.args.get('laundry_category')
        
        # Filter data based on the selected category
        filtered_data = [item for item in laundry_categories_all if item.name == selected_category]
        print(f"gago: gagoL {filtered_data}")

        filtered_data_dict = [{'name': item.name, 'price': item.price} for item in filtered_data]
        print(filtered_data_dict)
        return jsonify(filtered_data_dict)
    return redirect(url_for('index'))


@app.route('/option/<option>')
def option(option):
    if 'username' in session:
        #values to display in home page <- option1 
        profit, customer, claimed_laundry=LaundryList.profit_customer_claimed_today()

        #values to display in laundry list page <- option2
        laundry_list_all_obj = LaundryList.query.all()
        laundry_categories_all = LaundryCategories.query.all()
        
        #values to display in supply list page <- option3
        supply_list_all_obj = SupplyList.query.all()

        #values to display in inventory page <- option4
        inventory_list_all_obj = Inventory.query.all()

        supply_list_alias = aliased(SupplyList)
        inventory_list_alias = aliased(Inventory)
        joined_supply_inventory_obj=db.session.query(inventory_list_alias.date_created, 
            supply_list_alias.name, 
            inventory_list_alias.qty, 
            inventory_list_alias.stock_type)\
            .join(supply_list_alias, supply_list_alias.id == inventory_list_alias.supply_id)\
            .filter(inventory_list_alias.main==0)\
            .all()
        joined_main_supply_inventory_obj = db.session.query(inventory_list_alias.id,
                                        supply_list_alias.name,
                                        inventory_list_alias.qty)\
                                        .join(supply_list_alias, supply_list_alias.id==inventory_list_alias.supply_id)\
                                        .filter(inventory_list_alias.main==1)\
                                        .all()

        #values to display in reports page <- option5
        report_list_all_obj = LaundryList.query.filter_by(status=3).all()

        users_list_all_obj = Users.query.all()
        #values to display in users page <- option6

        return render_template('dashboard.html', selected_option=option, 
                               profit=profit, 
                               customer=customer, 
                               claimed_laundry=claimed_laundry, 
                               laundry_list_all_obj=laundry_list_all_obj, 
                               laundry_categories_all=laundry_categories_all, 
                               supply_list_all_obj=supply_list_all_obj,
                               inventory_list_all_obj=inventory_list_all_obj,
                               joined_supply_inventory_obj=joined_supply_inventory_obj,
                               joined_main_supply_inventory_obj=joined_main_supply_inventory_obj,
                               report_list_all_obj=report_list_all_obj,
                               users_list_all_obj=users_list_all_obj)
    
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('index'))

@app.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
    username, password = request.form.get('username'), request.form.get('password')
    if Users.login_is_true(username, password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')



if __name__ == "__main__":
    """with app.app_context():
        db.create_all()"""
    app.run(debug=True, host="0.0.0.0")