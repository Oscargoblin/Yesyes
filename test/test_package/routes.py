
import string
import random

from test_package import app ,db
from flask import render_template , redirect, request , url_for ,flash ,get_flashed_messages,session
from test_package import form
from test_package.models import User, Role
from test_package.form import  RegisterForm , LoginForm

@app.route("/", methods = ['GET'])
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    #如果當前有使用者登入，並且角色為管理員
    if  session.get('user') and session.get('role')=='1':
        results = db.session.query(User,Role).join(Role).all()
        return render_template('market.html',page_results=results )
    #如果沒有則導回login_page
    else:
        flash('你好像不是管理員，請重新登入', category='danger')
        return redirect(url_for("login_page"))
    
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
    
    if form.validate_on_submit():
        #先從登入表單接資料下來，並拿去資料庫比對
        attempted_user =  User.query.filter_by(Name=form.username.data).first()
        #如果使用者存在，並且check_user_password()檢查表單傳入的密碼正確
        if (attempted_user and attempted_user.check_user_password( attempted_password=form.password1.data ) ):
            #將使用者登入，並創建session
            session["user"] = attempted_user.Name
            session["role"] = attempted_user.Role_id
            
            flash(f'Success! You are logged in as: {attempted_user.Name}', category='success')
            return redirect(url_for("market_page"))
        else:
            flash('Username and password are not match! Please try again', category='danger')

        
    
    return render_template('login.html',login_page_form = form)

#帶參數的def
#return redirect(url_for('profile', username = attempted_user.Name))

@app.route('/mod_user/<get_user_id>' , methods= ['GET' ,'POST'])
def mod_user_page(get_user_id):

    user = User.query.filter_by(U_id= get_user_id).first()
    roles = Role.query.all()
    
    if request.method == 'POST':
        roleName = request.form.get('roleList')
        user.Role_id = Role.query.filter_by( RoleName = roleName).first().R_id
        user.Name = request.form.get('newName')
        user.Account = request.form.get('newEmail')
        user.Password = request.form.get('newPassword')
        
        db.session.commit()
        return redirect(url_for("market_page"))
        
        
    return render_template('modify_user.html' , user_to_mod = user ,roll_list=roles)

@app.route('/logout')
def logout():
    session.clear()
    flash('你已經登出', category='info')
    return redirect(url_for("home_page"))

@app.route('/user')
def profile():
    if session.get('user'):
        user = session.get('user')
        return f'{user}\'s profile'
    return '你還沒登入'

