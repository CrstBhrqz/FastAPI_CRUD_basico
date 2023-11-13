import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name="../database.sqlite"#nombre de la base de datos y donse se quiere crear 
base_dir= os.path.dirname(os.path.realpath(__file__)) #para leer el directorio


database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

Session =sessionmaker(bind=engine)#perfil de conexion 

Base = declarative_base()