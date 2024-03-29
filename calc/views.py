from django.shortcuts import render
from django.http import HttpResponse
from .models import Dest
import psycopg2
import pprint
li=[]
# Create your views here.
def home(request):
    return render(request,"fun.html")
def fun0(request):
    n=request.POST['r1']
    s=request.POST['r2']
    p=request.POST['r3']
    r=request.POST['r4']
    conn_string = "host='localhost' dbname='svhs' user='postgres' password='1234'"
    connection= psycopg2.connect(conn_string)
    c=connection.cursor()
    print(n,s,p,r)
    a=str(13)
    b=str(r)
    d=str(s)
    #c.execute("insert into public.calc_dest(id,name,contact,email,password) values(12,'prasad',961,'r@gmail.com','1234')")
    print("insert into public.calc_dest(id,name,contact,email,password) values("+a+","+n+","+d+","+p+","+r+")")
    c.execute("insert into public.calc_dest(id,name,contact,email,password) values("+a+","+"'"+n+"'"+","+d+","+"'"+p+"'"+","+"'"+b+"'"+")")
    connection.commit()
    connection.close()
    print("Done")
    return render(request,"fun.html")
def fun1(request):
    return render(request,"signupform.html")
def sub(request):
    d1=Dest()
    print(type(d1.name))
    n=request.POST['name']
    l=request.POST['lame']
    if n.isalpha() != True or l.isnumeric() != True:
        return render(request,"fun.html") 
    print(n,l)
    conn_string = "host='localhost' dbname='svhs' user='postgres' password='1234'"

    column_names = []
    data_rows = []
    li=[]
    with psycopg2.connect(conn_string) as connection:
        with connection.cursor() as cursor:
            cursor.execute("select * from public.calc_dest where id="+l)
            column_names = [desc[0] for desc in cursor.description]
            for row in cursor:
                data_rows.append(row)
                records = cursor.fetchall()
                li=[i for i in row]
                print(li)
                #print(records)
                pprint.pprint(records)
                print (type(records))
    print("Column names: {}\n".format(column_names))
    return render(request,"fun1.html",{'name':li[1]+' '+n})

def obj(request):
    conn_string = "host='localhost' dbname='svhs' user='postgres' password='1234'"

    column_names = []
    data_rows = []

    with psycopg2.connect(conn_string) as connection:
        with connection.cursor() as cursor:
            cursor.execute("select id, name")
            column_names = [desc[0] for desc in cursor.description]
            for row in cursor:
                data_rows.append(row)
                records = cursor.fetchall()
                pprint.pprint(records)
                print (type(records))

    print("Column names: {}\n".format(column_names))