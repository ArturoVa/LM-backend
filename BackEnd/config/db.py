
from sqlalchemy import create_engine,MetaData


#Configuarcion para acceder a la BD
DATABASE_URL = "mysql+pymysql://rootAdmin:Admin123@tasklist.mysql.database.azure.com/hw"
engine = create_engine(DATABASE_URL)
conn = engine.connect()
meta = MetaData()


