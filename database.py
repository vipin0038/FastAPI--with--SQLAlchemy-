from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,registry
from sqlalchemy.ext.declarative import declarative_base


# "mysql+pymysql://name:password@host:post/database_name"
URL = "mysql+pymysql://root:root@localhost/demodb"

# wo connect to sql database
engine = create_engine(URL)

# so create a session
SessionLocal = sessionmaker(bind = engine,autoflush=False)

# help in table if a table is already created then it will prevent it from creating again
Base = declarative_base()
