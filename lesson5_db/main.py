import src.pg_driver.database as pg_direct
import src.pg_orm.database as pg_orm

if __name__ == "__main__":
    # pg_direct.simple_connection()
    # pg_direct.connection_using_context()
    pg_orm.show_cities()