from flask import Flask ,render_template , request
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData,create_engine
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:110proj@192.168.1.188:3306/eco_streetlight'
app.config['SECRET_KEY']='6fd32112ea45db2f50754b47'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)

#engine = create_engine("mysql+pymysql://root:a123@localhost:3306/eco_streetlight")
#m = MetaData()
#m.reflect(engine)
#for table in m.tables.values():
#    print(table.name)
    
from test_package import routes