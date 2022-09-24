from test_package import app
#========================__init__.py=======================================

#========================__init__.py=======================================


#========================model=======================================

#========================model=======================================


#new_user= User( U_id = "U007" ,Name = "也圓心支柱4" , Account= "AAE@gmail.com", Password= "a11234234", Role_id = "3")
#db.session.add(new_user)
#db.session.commit()

#兩張表的查詢
#results = db.session.query(User,Role).join(Role).all()

#三張表的查詢
#results = db.session.query(User,Role,Authority).select_from(User).join(Role).join(Authority).all()

#sql 的 where
#results = db.session.query(User,Role,Authority).select_from(User).join(Role).join(Authority).filter(User.Name =='Sharon1').all()

#for u ,r in  results:
#    print(u.Name ,r.RoleName)
#========================routes=======================================


#========================routes=======================================


#========================run.py=======================================
if __name__ == "__main__":
    
    app.run(host="0.0.0.0")
    
#========================run.py=======================================
