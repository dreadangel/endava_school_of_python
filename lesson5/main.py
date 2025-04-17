import lesson5.sqlite_example.start as sqlite
import lesson5.kenobi_example.sample as kv_db



def sqlite_test()-> None:
    sqlite.demo()


def kenobi_test()-> None:
    kv_db.demo()
        

if __name__ == "__main__":
    # sqlite_test()
    kenobi_test()