from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+pymysql://root:3184@localhost:3306/authentication")
meta = MetaData()
conn = engine.connect()