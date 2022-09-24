
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def sql_test():
    url = "mysql+pymysql://root:a123@localhost:3306/eco_streetlight"
    engine = db.create_engine(url,{})
    conn = engine.connect()
    metadata = db.MetaData()
    table = db.Table('malfunction_sensor_record',metadata, autoload = True ,autoload_with= engine)
    
    
    query = db.select([table]).limit(10)
    rows = conn.execute(query).fetchall()
    print (type(rows))
    
    for row in rows:
        print (type(row))
        print(str(row.Mal_Sensor_id)+"  "+str(row.Mal_Sensor_Time))
    
    
sql_test()