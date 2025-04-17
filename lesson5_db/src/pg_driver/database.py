from psycopg2 import connect
from typing import Any
from  contextlib import contextmanager



@contextmanager
def get_connection(connection_details:dict[str, str]) -> Any:
    try:
        conn = connect( **connection_details)
        yield conn
    except Exception as ex:
        print(ex)
        raise ex from None
    finally:
        if conn:
            conn.close()
    


def connection_using_context() -> None:
    connection_data: dict[str, str] = {
                        "database":"dvdrental",
                        "host":"172.21.59.55",
                        "user":"postgres",
                        "password":"mysecretpassword",
                        "port":"5432"}
    
    with get_connection(connection_details=connection_data) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from city c")
        result = cursor.fetchall()
        print(result)        


def simple_connection()->None:
    conn = connect(database="dvdrental",
                        host="172.21.59.55",
                        user="postgres",
                        password="mysecretpassword",
                        port="5432")
        
    cursor = conn.cursor()
    cursor.execute("select * from city c")
    result = cursor.fetchall()
    print(result)
    
    conn.close()


if __name__ == "__main__":
    pass