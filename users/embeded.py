from django.db import connection 

def register_player(name,mobile_number,address,email):
    
    with connection.cursor() as cursor:
        cursor.execute("insert into player(name,mobile_number,address) values(\"%s\",\"%s\",\"%s\");",[name,mobile_number,address])
        cursor.execute("SELECT LAST_INSERT_ID();")
        player_id = cursor.fetchall()[0][0] 
        cursor.execute("insert into account(player_id,current_balance,date_of_opening) values(%s,1000,NOW())",[player_id])
        cursor.execute("insert into player_email(player_id,email) values(%s,\"%s\");",[player_id,email])

def extract_data_player():
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
    return (columns,data)

def extract_data_employee():
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
    return (columns,data)


def update_employee_salary(new_salary,id):
    
    with connection.cursor() as cursor:
        cursor.execute("update employee set salary = %s where id = %s",[new_salary,id])

def extract_data_player_with_id(id):
    with connection.cursor() as cursor:
        cursor.execute("select * from player where id=%s;",id)
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

def extract_data_employee_with_id(id):
    with connection.cursor() as cursor:
        cursor.execute("select * from employee where id=%s;",id)
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

def new_employee(id,name,position,mobile,address,salary,email):
    
    with connection.cursor() as cursor:
        cursor.execute("insert into employee values(%s,\"%s\",\"%s\",\"%s\",\"%s\",%s);",[id,name,position,mobile,address,salary])
        cursor.execute("insert into employee_email(employee_id,email) values(%s,\"%s\");",[id,email])

def game_maker_max_profit(id):

    with connection.cursor() as cursor:
        cursor.execute("select max(total_profit) as Maximum_Profit FROM game WHERE id IN ( SELECT game_id FROM made WHERE game_maker_id =  %s);",[id])

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

def update_records(email,won,bet,game_id):
    with connection.cursor() as cursor:
        cursor.execute("select player_id from player_email where email like \"%s\"",[email])
        player_id = cursor.fetchall()[0][0]
        cursor.execute("insert into game_transaction(game_id,player_id,won_lost,bet,dt) values(%s,%s,%s,%s,NOW());",[game_id,player_id,1 if won else 0,1 if bet else 0])
        cursor.execute("select id from account where player_id = %s",[player_id])
        account_id = cursor.fetchall()[0][0]
        if bet:
            if won:
                cursor.execute("update account set current_balance = current_balance+100 where id = %s;",[account_id])
            else:
                cursor.execute("update account set current_balance = if ( current_balance>=100,current_balance-100,0) where id = %s;",[account_id])
        else:
            cursor.execute("update account set current_balance = if ( current_balance>=10,current_balance-10,0) where id = %s;",[account_id])

def player_profile(email):
    with connection.cursor() as cursor:
        cursor.execute("select player_id from player_email where email like \"%s\"",[email])
        player_id = cursor.fetchall()[0][0]
        cursor.execute("select * from player where id =%s",[player_id])
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