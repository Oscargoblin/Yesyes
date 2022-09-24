from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField ,SubmitField
from wtforms.validators import Length,EqualTo, Email , DataRequired ,ValidationError
from test_package.models import User

class RegisterForm(FlaskForm):
    
    #檢查是否有帳號重名
    #FlaskForm 會將這個def名稱拆開成 validate_ + username ，只要是validate_開頭的就會被默認執行
    #接著FlaskForm搜索所有的變數欄位(fields) 像是下方寫的 username , email_address , password1等 
    #所以命名由來是這樣，假如我改成validate_name等其他名字就不會被觸發
    
    def validate_username(self, username_to_check):
        #username_to_check.data才能拿到該field的值
        user = User.query.filter_by(Name = username_to_check.data).first()
        if user:
            raise ValidationError('使用者已經存在，請試試另一個名字 ')
    
    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(Account = email_to_check.data).first()
        if email:
            raise ValidationError('該email帳號已被使用 ')
    
    username = StringField(label= '使用者姓名', validators=[Length(min=4,max=10),DataRequired()])
    email_address = StringField(label= '電子郵件',validators=[Email(),DataRequired()] )
    password1 = PasswordField(label= '密碼' , validators=[Length(min=4,max=20), DataRequired()])
    password2 = PasswordField(label='確認密碼' , validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label = '創建帳號')