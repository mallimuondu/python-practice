import sqlite3
conn = sqlite3.connect('app.db')
c = conn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS malli(name TEXT)')
    
table()


 
def addinput():
    while True:
        name  = input("enter your name: ")
        if not name.isalpha():
            continue
        else:
            c.execute("INSERT INTO malli (name)VALUES(?)",(name,))
                      
            conn.commit()
            print("DATER ENTER SUCSEFULLY")
            
            break
#    conn.close()
addinput()



def read_from_db():
    c.execute("SELECT * FROM malli ")
    
    a = c.fetchall()
    
    print(a)
    
#    for row in c.fetchall():
#        print(row)  
#conn.close()

read_from_db