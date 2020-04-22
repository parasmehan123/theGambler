from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 
from django.db import connection 

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
def query1(request):
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

        print(data,columns)
    return render(request,'users/profile.html',{'query':1,'data':data,'columns':columns})