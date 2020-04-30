from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required 
import random
from .embeded import *
words = ["casino","acute","gallon","communication","crosswalk","peasant","fix","knee","discrimination","indoor","paragraph","bathroom","fountain","acid","fasle","wealth","mayor","country","fee","march"]

@login_required
def profile(request):
    return render(request,'users/profile.html')

message = ""
messagenumber = ""
@login_required
def play(request):
    global word, message, jword ,betb, betv
    message = ""
    betb = request.GET["q1"]
    word = random.choice(words)
    jum = random.sample(word,len(word))
    jword = "".join(jum)
    context = {
        'jword' : "".join(jum),
        'message' : message,
        'betb' : betb
    }

    return render(request,'users/play.html',context)

def checkans(request):
    global word, jword, message,betb, betv
    user_ans = request.GET["answer"]
    # print(betb, betv,betb=='y')   
    won = True
    if (user_ans in words):   
        message = "That was the correct answer. Great job!"        
    else:
        won = False
        message = "Oop! Better Luck next time!"

    update_records(request.user.email,won,betb=='y',1)

    return placebid(request)

@login_required
def placebid(request):
    global betb, betv,message
    context = {
        'message' : message,        
    }
    return render(request,'users/placebid.html',context)

messagenumber = ""   
@login_required
def placebid_guessno(request):
    global betgb, betgv,messagenumber

    context = {
        'messagenumber' : messagenumber,

    }
    return render(request,'users/placebid_guessno.html',context)
num = []
@login_required
def guessno(request):
    global num, messagenumber,betgb, betgv
    messagenumber = ""
    number = random.randint(0,31)
    num.append(number)  
    betgb = request.GET["q2"]
    context = {
        'num' : num[-1],
        'messagenumber' : messagenumber,
        'betgb' : betgb
    }
    return render(request,'users/guessno.html',context)

def checknumber(request):
    global messagenumber,betgb, betgv
    user_ans = int(request.GET["number"])
    won = True
    if (user_ans == num[-1]):
        messagenumber = "That was the correct answer. great Job!"
    else:
        won = False
        messagenumber = "Oop! Better Luck next time!"
    context = {
        'user_ans' : user_ans,
        'num' : num 
    }
    update_records(request.user.email,won,betgb=='y',2)
    return placebid_guessno(request)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            register_player(form.data["first_name"]+" "+form.data["last_name"],form.data["mobile_number"],form.data["address"],form.data["email"])
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.user.is_staff:
        return render(request,'users/profile.html')
    query = "select * from player where id = %s;"%(request.user.id+13)
    columns,data =  extract_data(query)
    # print(query)
    return render(request,'users/profile.html',{'pro_data':data,'pro_columns':columns})


@login_required
def query1a(request):
    columns,data = extract_data_player()

    return render(request,'users/profile.html',{'query':1,'data':data,'columns':columns})

@login_required
def query2a(request):
    columns,data = extract_data_employee()

    return render(request,'users/profile.html',{'query':2,'data':data,'columns':columns})

@login_required
def query3a(request):
    if request.method == 'POST':
        form = Id_SalaryForm(request.POST)
        if form.is_valid():
            # print(form.data['id'],form.data['new_salary'],int(form.data['new_salary']),int(form.data['id']))
            # print(form.data)
            update_employee_salary(form.data['new_salary'],form.data['id'])
            id = form.data['id']
            messages.success(request, f'Salary Updated for employee with ID {id}')  
        return redirect('profile')
    else:
        form = Id_SalaryForm()
    return render(request,'users/profile.html',{'query':3,'form':form})

@login_required
def query4a(request):
    if request.method == 'POST':
        form = Id_Form(request.POST)
        if form.is_valid():
            # print(form.data)
            (columns,data) = extract_data_player_with_id(form.data['id'])
            return render(request,'users/profile.html',{'query':4,'data':data,'columns':columns})

        return render(request,'users/profile.html',{'query':4,'form':form,})
    else :
        form = Id_Form()
    return render(request,'users/profile.html',{'query':4,'form':form})


@login_required
def query5a(request):
    if request.method == 'POST':
        form = Id_Form(request.POST)
        if form.is_valid():
            # print(form.data)
            (columns,data) = extract_data_employee_with_id(form.data['id'])
            return render(request,'users/profile.html',{'query':5,'data':data,'columns':columns})

        return render(request,'users/profile.html',{'query':5,'form':form,})
    else :
        form = Id_Form()
    return render(request,'users/profile.html',{'query':5,'form':form})

@login_required
def query6a(request):
    if request.method == 'POST':
        form = New_Employee(request.POST)
        if form.is_valid():
            # print(form.data)
            STATES = {
                    'E1':'Accounts Employee',
                    'E2': 'Game Maker',
                    'E3': 'Casino Dealer'
                }
            new_employee(form.data['id'],form.data['name'],STATES[form.data['position']],form.data['mobile'],form.data['address'],form.data['salary'],form.data['email'])
            
            messages.success(request, f'New Employee Account Created!!')  
        return redirect('profile')
    else:
        form = New_Employee()
    return render(request,'users/profile.html',{'query':6,'form':form})

@login_required
def query7a(request):
    if request.method == 'POST':
        form = Id_Form(request.POST)
        if form.is_valid():
            # print(form.data)
            (columns,data) = game_maker_max_profit(form.data['id'])
            return render(request,'users/profile.html',{'query':7,'data':data,'columns':columns})

        return render(request,'users/profile.html',{'query':7,'form':form,})
    else :
        form = Id_Form()
    return render(request,'users/profile.html',{'query':7,'form':form})

@login_required
def query8a(request):
    columns,data = player_profile(request.user.email)

    return render(request,'users/profile.html',{'query':8,'data':data,'columns':columns})

@login_required
def query9a(request):
    columns,data = player_game_details(request.user.email)

    return render(request,'users/profile.html',{'query':9,'data':data,'columns':columns})

@login_required
def query10a(request):
    columns,data = player_games_not_played(request.user.email)

    return render(request,'users/profile.html',{'query':10,'data':data,'columns':columns})

@login_required
def query11a(request):
    columns,data = player_account_balance(request.user.email)

    return render(request,'users/profile.html',{'query':11,'data':data,'columns':columns})

@login_required
def query12a(request):
    columns,data = player_ranklist()

    return render(request,'users/profile.html',{'query':12,'data':data,'columns':columns})
