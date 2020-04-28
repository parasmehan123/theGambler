from django.db import connection 

def register_player(name,mobile_number,address,email):
    
    with connection.cursor() as cursor:
        cursor.execute("insert into player(name,mobile_number,address,email) values(\"%s\",\"%s\",\"%s\",\"%s\");",[name,mobile_number,address,email])

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
        cursor.execute("insert into employee values(%s,\"%s\",\"%s\",\"%s\",\"%s\",%s,\"%s\");",[id,name,position,mobile,address,salary,email])

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