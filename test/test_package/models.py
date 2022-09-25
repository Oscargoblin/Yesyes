from email.policy import default
from test_package import db ,bcrypt

#=========================================================================
class User(db.Model):
    
    U_id = db.Column(db.String(45), primary_key = True)
    Name = db.Column(db.String(45))
    Account = db.Column(db.String(45))
    Password = db.Column(db.String(1000))
    Role_id = db.Column(db.String(45), db.ForeignKey('role.R_id') ,default='1')
    
    @property
    def encrypted_password(self):
        return self.password
    
    @encrypted_password.setter
    def encrypted_password(self,plain_text_password):
        self.Password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


#=========================================================================

class Role(db.Model):
    
    R_id = db.Column(db.String(45), primary_key = True)
    RoleName = db.Column(db.String(45))
    auth_id = db.Column(db.String(45), db.ForeignKey('authority.auth_id'))
    
    def __init__(self, role_id, role_name, auth_id):
         self.R_id = role_id
         self.RoleName = role_name
         self.auth_id = auth_id
    
    def __repr__(self) :
        return "<Role('%s','%s', '%s')>\n" % (self.R_id, self.RoleName, self.auth_id)
    
    
#=========================================================================


class Authority(db.Model):
    auth_id = db.Column(db.String(45), primary_key = True)
    can_do = db.Column(db.String(45))
    
    def __init__(self, auth_id, can_do):
         self.auth_id = auth_id
         self.can_do = can_do
         
    
    def __repr__(self) :
        return "<Authority('%s','%s')>\n" % (self.auth_id, self.can_do)