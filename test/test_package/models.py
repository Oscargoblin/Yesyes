from email.policy import default
from test_package import db

#=========================================================================
class User(db.Model):
    
    U_id = db.Column(db.String(45), primary_key = True)
    Name = db.Column(db.String(45))
    Account = db.Column(db.String(45))
    Password = db.Column(db.String(45))
    Role_id = db.Column(db.String(45), db.ForeignKey('role.R_id') ,default='1')
    
    #__init__這裡要求幾個參數，在new一個User時就要傳入幾個參數
    def __init__( self,uid, name, account, password):
         self.U_id = uid
         self.Name = name
         self.Account = account
         self.Password = password

    
    
    def __repr__(self) :
        return "<User('%s','%s', '%s')>\n" % (self.Name, self.Account, self.Password)

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