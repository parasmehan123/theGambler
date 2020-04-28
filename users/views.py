from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required 
from django.db import connection 
import random
words = ["casino","acute","gallon","communication","crosswalk","peasant","fix","knee","discrimination","indoor","paragraph","bathroom","fountain","acid","fasle","wealth","mayor","country","fee","march"]




@login_required
def profile(request):
    return render(request,'users/profile.html')

message = ""
@login_required
def play(request):
    global word, message, jword ,betb, betv
    message = ""
    betb = request.GET["q1"]
    betv = request.GET["bet"]
    word = random.choice(words)
    jum = random.sample(word,len(word))
    jword = "".join(jum)
    context = {
        'jword' : "".join(jum),
        'message' : message,
        'betv' : betv,
        'betb' : betb
    }

    return render(request,'users/play.html',context)
def checkans(request):
    global word, jword, message,betb, betv
    user_ans = request.GET["answer"]
    won = True
    if (user_ans in words):   

        message = "That was the correct answer. Great job!"
        
    else:
        won = False
        message = "Oop! Better Luck next time!"

    query = "insert into game_transaction(user_email,won_lost,dt) values(\""+request.user.email+"\","
    if won:
        query += 'TRUE'
    else:
        query += 'FALSE'

    query += ",NOW());"
    # print(query)
    with connection.cursor() as cursor:
        cursor.execute(query)

    return placebid(request)
@login_required
def placebid(request):
    global betb, betv,message
    context = {
        'message' : message,        
    }
    return render(request,'users/placebid.html',context)
def extract_data(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        columns_names = [col[0] for col in cursor.description]
        data_raw = cursor.fetchall()

        columns = []
        c=1
        for i in columns_names:
            tmp = {
                'text':i,
                'meta':'cell100 column'+str(c),
            }
            columns.append(tmp)
            c+=1
        data = []
        for i in data_raw:
            tmp = []
            c = 1
            for col in i:
                tmp2 = {
                    'text' :col,
                    'meta' : 'cell100 column'+str(c),
                }
                c+=1
                tmp.append(tmp2)
            data.append(tmp)
    return (columns,data)

def id_query(request,query,query_no):
    if request.method == 'POST':
        form = Id_Form(request.POST)
        if form.is_valid():
            # print(form.data)
            columns,data = extract_data(query%(form.data['id']))
            return render(request,'users/profile.html',{'query':query_no,'data':data,'columns':columns})

        return render(request,'users/profile.html',{'query':query_no,'form':form,})
    else :
        form = Id_Form()
    return render(request,'users/profile.html',{'query':query_no,'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                # print(form.data)
                cursor.execute("insert into player(name,mobile_number,address,email) values(\"%s\",\"%s\",\"%s\",\"%s\");", [form.data["first_name"]+" "+form.data["last_name"],form.data["mobile_number"],form.data["address"],form.data["email"]])
                row = cursor.fetchone()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

@login_required
def query1a(request):
    columns,data = extract_data("select * from player;")

    return render(request,'users/profile.html',{'query':1,'data':data,'columns':columns})

@login_required
def query2a(request):
    columns,data = extract_data("select * from employee;")

    return render(request,'users/profile.html',{'query':2,'data':data,'columns':columns})

@login_required
def query3a(request):
    if request.method == 'POST':
        form = Id_SalaryForm(request.POST)
        if form.is_valid():
            # print(form.data['id'],form.data['new_salary'],int(form.data['new_salary']),int(form.data['id']))
            # print(form.data)
            with connection.cursor() as cursor:
                cursor.execute("update employee set salary = %s where id = %s",[form.data['new_salary'],form.data['id']])
            id = form.data['id']
            messages.success(request, f'Salary Updated for employee with ID {id}')  
        return redirect('profile')
    else:
        form = Id_SalaryForm()
    return render(request,'users/profile.html',{'query':3,'form':form})

@login_required
def query4a(request):
    return id_query(request,"select * from player where id=%s;",4)

@login_required
def query5a(request):
    return id_query(request,"select * from employee where id=%s;",5)

@login_required
def query6a(request):
    if request.method == 'POST':
        form = New_Employee(request.POST)
        if form.is_valid():
            # print(form.data)
            with connection.cursor() as cursor:
                #create table employee(id int primary key , name varchar(200),position varchar(100) not null,mobile varchar(200),address varchar(1000),salary int not null, email varchar(1000));
                STATES = {
                    'E1':'Accounts Employee',
                    'E2': 'Game Maker',
                    'E3': 'Casino Dealer'
                }
                cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s);",[form.data['id'],form.data['name'],STATES[form.data['position']],form.data['mobile'],form.data['address'],form.data['salary'],form.data['email']])
            
            messages.success(request, f'New Employee Account Created!!')  
        return redirect('profile')
    else:
        form = New_Employee()
    return render(request,'users/profile.html',{'query':6,'form':form})

@login_required
def query7a(request):
    return id_query(request,"select max(total_profit) as Maximum_Profit FROM game WHERE id IN ( SELECT game_id FROM made WHERE game_maker_id =  %s);",7)
