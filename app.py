from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from model import db, Users, LaundryList, LaundryCategories, LaundryItems, SupplyList
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/laundry_aaron'
db.init_app(app)
app.secret_key = 'ajdshfaskdjhf'

@app.route('/update_supply', methods=['POST', 'GET'])
def update_supply():
    if 'username' in session:
        supply_name, supply_type, qty = request.form['supply_name'], int(request.form['supply_type']), int(request.form['supply_qty'])
        supply_obj = SupplyList.query.filter_by(id=supply_name).first()
        if supply_type==1:
            supply_obj.qty += qty 
            db.session.commit()
            return redirect('/option/option5')
        supply_obj.qty -= qty
        db.session.commit()
        return redirect('/option/option5')
    return redirect(url_for('index'))

@app.route('/save_supply', methods=['POST', 'GET'])
def save_supply():
    if 'username' in session:
        supply = request.form['supply']
        if supply:
            supply_entry = SupplyList(name=supply)
            db.session.add(supply_entry)
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

        # You can now process and save this data to your database or perform any other necessary actions

        # Example: Create a new LaundryList entry in the database
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
        return redirect(url_for('dashboard'))
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
        #values to display in home page
        profit, customer, claimed_laundry=LaundryList.profit_customer_claimed_today()

        #values to display in laundry list page
        laundry_list_all_obj = LaundryList.query.all()
        laundry_categories_all = LaundryCategories.query.all()
        
        #values to display in supply list page
        supply_list_all_obj = SupplyList.query.all()

        return render_template('dashboard.html', selected_option=option, 
                               profit=profit, 
                               customer=customer, 
                               claimed_laundry=claimed_laundry, 
                               laundry_list_all_obj=laundry_list_all_obj, 
                               laundry_categories_all=laundry_categories_all, 
                               supply_list_all_obj=supply_list_all_obj)
    
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