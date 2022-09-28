import psycopg2 as p
from create2 import Create
from read2 import Read
from update2 import Update
from delete2 import Delete

mydb = p.connect(
    user='santosh1',
    password='postgres',
    dbname='postdatabase',
    host="localhost"    
)
mycursor=mydb.cursor()

def checkregistration():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ').upper()
    if choice == 'C':
        t=Create()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'R':
        t=Read()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'U':
        t=Update()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'D':
        t=Delete()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    else:
        print('Wrong Entry')
        checkregistration()

checkregistration()      






