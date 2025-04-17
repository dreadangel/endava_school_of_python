import sqlite3
from pathlib import Path
from prettytable import from_db_cursor, PrettyTable


def prepare_db_structure(conn : sqlite3.Connection) ->None:
    #table Persons
    conn.execute('''CREATE TABLE PERSONS
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            EMAIL         CHAR(50));''')
    #table Companies
    conn.execute('''CREATE TABLE COMPANIES
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            ADDRESS        CHAR(50),
            EMAIL         CHAR(50));''')
    #table Employes
    conn.execute('''CREATE TABLE EMPLOYES
            (ID INT PRIMARY KEY     NOT NULL,
            PERSONID    INT     NOT NULL,
            COMPANYID    INT     NOT NULL,
            SALARY         REAL);''')
    conn.commit()


def do_selects(conn : sqlite3.Connection) ->None:
    print("PERSONS data:",end="\n")
    cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, EMAIL from PERSONS")
    for row in cursor:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}",end="\n")

    print("COMPANIES data:",end="\n")
    cursor = conn.execute("SELECT ID, NAME, ADDRESS, EMAIL from COMPANIES")
    for row in cursor:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}",end="\n")


def get_prettytable(sql_comm:str, conn : sqlite3.Connection) -> PrettyTable:
    cursor = conn.execute(sql_comm)
    return from_db_cursor(cursor)


def do_selects_pretty(conn : sqlite3.Connection) ->None:
    print("PERSONS data in pretty format:",end="\n")
    print(get_prettytable(sql_comm="SELECT ID, NAME, AGE, ADDRESS, EMAIL from PERSONS", conn=conn))
    print("COMPANIES data in pretty format:",end="\n")
    print(get_prettytable(sql_comm="SELECT ID, NAME, ADDRESS, EMAIL from COMPANIES", conn=conn))


def prepare_data(conn : sqlite3.Connection) ->None:
    #table Persons
    conn.execute("INSERT INTO PERSONS (ID,NAME,AGE,ADDRESS,EMAIL) VALUES (1, 'Paul', 32, 'California', 'paul@california.com' )")
    conn.execute("INSERT INTO PERSONS (ID,NAME,AGE,ADDRESS,EMAIL) VALUES (2, 'Leonardo', 19, 'Italia', 'leo@italia.eu' )")
    conn.execute("INSERT INTO PERSONS (ID,NAME,AGE,ADDRESS,EMAIL) VALUES (3, 'Ion', 25, 'Chisinau', 'ion@mail.md' )")
    #table Companies
    conn.execute("INSERT INTO COMPANIES (ID,NAME,ADDRESS,EMAIL) VALUES (1, 'Endava', 'Arborilor, 21b', 'info@endava.com' )")
    conn.execute("INSERT INTO COMPANIES (ID,NAME,ADDRESS,EMAIL) VALUES (2, 'Parlament', 'Stefan cel Mare', 'info@parlament.com' )")
    #table Employes
    conn.execute("INSERT INTO EMPLOYES (ID,PERSONID,COMPANYID,SALARY) VALUES (1, 1, 1, 2500.0 )")
    conn.execute("INSERT INTO EMPLOYES (ID,PERSONID,COMPANYID,SALARY) VALUES (2, 2, 1, 700.0 )")
    conn.execute("INSERT INTO EMPLOYES (ID,PERSONID,COMPANYID,SALARY) VALUES (3, 3, 2, 25000.0 )")
    conn.commit()


def demo()->None:
    my_file = Path("test.db")
    if my_file.is_file():
        Path.unlink("test.db")

    connection : sqlite3.Connection = sqlite3.connect('test.db')
    # connection : sqlite3.Connection = sqlite3.connect(':memory:')
    prepare_db_structure(conn=connection)
    prepare_data(conn=connection)
    # do_selects(conn=connection)
    do_selects_pretty(conn=connection)
    connection.close()


if __name__ == "__main__":
    pass