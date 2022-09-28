import psycopg2 as p
# from create2 import Create
# from read2 import Read
# from update2 import Update
# from delete2 import Delete

mydb = p.connect(
    user='santosh1',
    password='postgres',
    dbname='postdatabase',
    host="localhost"    
)
mycursor=mydb.cursor()

def Create():
    while True:
        print("\n","\t","--Please enter field to store in database--")
        name=input("Enter your name: ")
        city=input("Enter your city: ")
        sql = "INSERT INTO crud (name,city) VALUES (%s, %s)"
        val = (name,city)
        mycursor.execute(sql, val)
        mydb.commit()
        print("\n","--Data saved successfully--")
        x=int(input("1:More user\n2:exit\nSelect option: "))
        if x==2:
          return True


