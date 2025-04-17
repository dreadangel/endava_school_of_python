from src.pg_orm.dto import City

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

connection_data: dict[str, str] = {
                        "database":"dvdrental",
                        "host":"172.21.59.55",
                        "user":"postgres",
                        "password":"mysecretpassword",
                        "port":"5432"}


def show_cities()-> None:
    try:
        db_uri:str = f"postgresql://{connection_data["user"]}:{connection_data["password"]}@{connection_data["host"]}:{connection_data["port"]}/{connection_data["database"]}"
        engine = create_engine(db_uri, echo=True)
        
        session = Session(engine)
        stmt = select(City).where(City.city.in_(["Chisinau", "Bucuresti"]))
        for item in session.scalars(stmt):
            print(f"{item.city_id}\t{item.city}")
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")


def insert_cities()-> None:
    try:
        db_uri:str = f"postgresql://{connection_data["user"]}:{connection_data["password"]}@{connection_data["host"]}:{connection_data["port"]}/{connection_data["database"]}"
        engine = create_engine(db_uri, echo=True)
        
        session = Session(engine)
        stmt = select(City).where(City.city.in_(["Chisinau", "Bucuresti"]))
        for item in session.scalars(stmt):
            print(f"{item.city_id}\t{item.city}")
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")
