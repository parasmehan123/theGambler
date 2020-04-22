from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required 
from django.db import connection 
import random
words = ["casino","acute","gallon","communication","crosswalk","peasant","fix","knee","discrimination","indoor","paragraph","bathroom","fountain","acid","fasle","wealth","mayor","country","fee","march"]

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
def play(request):
    global word, message, jword
    word = random.choice(words)
    jum = random.sample(word,len(word))
    jword = "".join(jum)
    context = {
        'jword' : "".join(jum),
        'message' : message
    }
    return render(request,'users/play.html',context)
def checkans(request):
    global word, jword, message
    user_ans = request.GET["answer"]
    if (user_ans in words):
        message = "That was the correct answer. Great job!"
        
    else:
        message = "Oop! Better Luck next time!"

    return play(request)
@login_required
def query1a(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from player;")
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

        # print(data,columns)
    return render(request,'users/profile.html',{'query':1,'data':data,'columns':columns})

@login_required
def query2a(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from employee;")
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

        # print(data,columns)
    return render(request,'users/profile.html',{'query':2,'data':data,'columns':columns})

@login_required
def query3a(request):
    if request.method == 'POST':
        form = IdForm(request.POST)
        if form.is_valid():
            # print(form.data['id'],form.data['new_salary'],int(form.data['new_salary']),int(form.data['id']))
            print(form.data)
            with connection.cursor() as cursor:
                cursor.execute("update employee set salary = %s where id = %s",[form.data['new_salary'],form.data['id']])
            id = form.data['id']
            messages.success(request, f'Salary Updated for employee with ID {id}')  
        return redirect('profile')
    else:
        form = IdForm()
    return render(request,'users/profile.html',{'query':3,'form':form})
