from kenobi import KenobiDB
import re


def prepare_data(db:KenobiDB)-> None:
    db.insert({"name": "Leonard", "email": "leo@mail.it"})

    db.insert_many([
        {"name": "Teo", "email": "teo@mail.ro"},
        {"name": "Ion", "email": "ion@mail.md"}
    ])


def show_data(db:KenobiDB)-> None:
    print("All data:", end="\n")
    for record in db.all():
        print(f"\t{record}")

def search_example(db:KenobiDB)-> None:
    print("Search example:", end="\n")
    
    db.insert_many([
            {"name": "Alex", "email": "alex@endava.com"},
            {"name": "Ana", "email": "ana@endava.com"}
    ])

    
    for record in db.search("name", "Ana"):
        print(f"\t{record}")

    # pattern = r"^.*endava.com$"
    pattern = r"^.*.md$"

    print("Regex search example:", end="\n")
    for record in list(filter(lambda item: re.match(pattern, item["email"]), db.all())):
        print(f"\t{record}")
        

def demo()->None:
    db:KenobiDB = KenobiDB("example.db")

    prepare_data(db=db)
    show_data(db=db)
    search_example(db=db)
    
    # db.purge()
    db.close()


if __name__ == "__main__":
    pass