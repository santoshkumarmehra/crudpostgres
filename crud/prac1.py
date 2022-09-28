import psycopg2 as p

mydb = p.connect(
    user='santosh1',
    password='postgres',
    dbname='postdatabase',
    host="localhost"    
)
mycursor=mydb.cursor()

# Command="create table crud(name text,city text)"
# mycursor.execute(Command)
# mydb.commit()

# name=input("name: ")
# city=input("city: ")
# q="insert into crud(name,city) values('{}','{}')".format(name,city)
# mycursor.execute(q)
# mydb.commit()

mycursor.execute("select * from crud")
data=mycursor.fetchall()
for i in data:
    print(i)