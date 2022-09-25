import string
import random

from test_package import app ,db
from flask import render_template , redirect , url_for ,flash ,get_flashed_messages
from test_package.models import User, Role
from test_package.form import RegisterForm , LoginForm

@app.route("/", methods = ['GET'])
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    
    results = db.session.query(User,Role).join(Role).all()
    return render_template('market.html',page_results=results )

@app.route('/register' , methods= ['GET','POST'])
def register_page():
    #建立一個來自form.py 的 RegisterForm()
    form = RegisterForm()
    #如果form的submit_field被按下
    if form.validate_on_submit():
        #建立一個User物件
        user_to_create = User(
                            U_id = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))),
                            Name = form.username.data,
                            Account = form.email_address.data,
                            encrypted_password = form.password1.data
                            )
        #db新增一筆資料
        db.session.add(user_to_create)
        db.session.commit()
        #將網頁重新導向( redirect()函數會要求位址字串，但是直接把位址寫死不好所以將他導到 def market_page() 函數，由他來負責網頁跳轉)
        return redirect(url_for('market_page'))
    
    #如果表單呈報的資料有錯誤(不符合要求的格式)，則打印出來看
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash("表單提交錯誤"+str(err_msg), category='danger')

    return render_template('register.html', page_form = form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form=LoginForm()
    return render_template('login.html',login_page_form = form)


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


