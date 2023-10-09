from flask import Flask, render_template, request, url_for, session, redirect
from model import db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/laundry_aaron'
db.init_app(app)
app.secret_key = 'ajdshfaskdjhf'

@app.route('/option/<option>')
def option(option):
    if 'username' in session:
        return render_template('dashboard.html', selected_option=option)
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