import sqlite3

conn = sqlite3.connect('app.db')
c = conn.cursor()

def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS malli(name TEXT,age INT)')
create_table()

def adding_items():
        while True:
            name  = input("enter your name: ")
            if not name.isalpha():
                continue
            else:
                try:
                    age = int(input("enter age"))
                except ValueError:
                    print("sorry i did'nt understand that")
                
                
            c.execute("INSERT INTO malli(name,age) VALUES(?,?)",(name,age))
            conn.commit()
            print("it works")
            
            break
                    
adding_items()

def read_database():
    c.execute("SELECT * FROM  malli")
    
    for a in c.fetchall():
        print(a)
read_database()