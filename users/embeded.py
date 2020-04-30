from django.db import connection 

def register_player(name,mobile_number,address,email):
    
    with connection.cursor() as cursor:
        cursor.execute("insert into player(name,mobile_number,address) values(\"%s\",\"%s\",\"%s\");",[name,mobile_number,address])
        cursor.execute("SELECT LAST_INSERT_ID();")
        player_id = cursor.fetchall()[0][0] 
        cursor.execute("insert into account(player_id,current_balance,date_of_opening) values(%s,1000,NOW())",[player_id])
        cursor.execute("insert into player_email(player_id,email) values(%s,\"%s\");",[player_id,email])
        cursor.execute("insert into player_ranklist(player_id,no_of_wins,no_of_loses,total_profit,total_loss) values(%s,0,0,0,0);",[player_id])
        cursor.execute("insert into game_details(game_id,player_id,no_of_wins,no_of_losses,amount_won,amount_lost) values(4,%s,0,0,0,0);",[player_id])
        cursor.execute("insert into game_details(game_id,player_id,no_of_wins,no_of_losses,amount_won,amount_lost) values(5,%s,0,0,0,0);",[player_id])
        

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
        

        cursor.execute("update game_details set no_of_wins = no_of_wins + %s where player_id = %s AND game_id = %s ;",[1 if won else 0, player_id, game_id+3]  )
        connection.commit()
        cursor.execute("update game_details set no_of_losses = no_of_losses + %s where player_id = %s AND game_id = %s ;",[0 if won else 1, player_id, game_id+3]  )
        connection.commit()
        cursor.execute("update game_details set amount_won = amount_won + %s where player_id = %s AND game_id = %s ;",[100 if won and bet else 0, player_id, game_id+3]  )
        connection.commit()
        cursor.execute("update game_details set amount_lost = amount_lost + %s where player_id = %s AND game_id = %s ;",[10 if not bet else (0 if won else 100), player_id, game_id+3]  )
        connection.commit()

        cursor.execute("update player_ranklist set no_of_wins = no_of_wins + %s where player_id = %s ;",[1 if won else 0, player_id]  )
        connection.commit()
        cursor.execute("update player_ranklist set no_of_loses = no_of_loses + %s where player_id = %s ;",[0 if won else 1, player_id]  )
        connection.commit()
        cursor.execute("update player_ranklist set total_profit = total_profit + %s where player_id = %s ;",[100 if won and bet else 0, player_id]  )
        connection.commit()
        cursor.execute("update player_ranklist set total_loss = total_loss + %s where player_id = %s ;",[10 if not bet else (0 if won else 100), player_id]  )
        connection.commit()

        cursor.execute("update game set no_of_games_played = no_of_games_played + %s where id = %s ;", [1, game_id+3]  )
        connection.commit()
        cursor.execute("update game set total_profit = total_profit + %s where id = %s ;",[100 if won and bet else 0, game_id+3]  )
        connection.commit()
        cursor.execute("update game set total_loss = total_loss + %s where id = %s ;",[10 if not bet else (0 if won else 100), game_id+3]  )
        connection.commit()
        
        #Update ranklist in game_details
        cursor.execute("alter table game_details drop column rank")
        connection.commit()
        cursor.execute("set @row_number = 0;")
        cursor.execute("select game_id, player_id, @row_number := @row_number + 1 AS rank from game_details order by no_of_wins desc;")
        data = cursor.fetchall()
        # print(data)
        cursor.execute("alter table game_details add Rank int not null")
        connection.commit()
        for x in data:
            # print(x)
            cursor.execute("update game_details set rank = " + str(x[2]) + " where player_id = " + str(x[1]) + " && game_id = " + str(x[0] + 3) + " ;")
            connection.commit()


        #Update ranklist in player_ranklist
        cursor.execute("alter table player_ranklist drop column rank")
        connection.commit()
        cursor.execute("set @row_number = 0;")
        cursor.execute("select player_id, @row_number := @row_number + 1 AS rank from player_ranklist order by no_of_wins desc;")
        data = cursor.fetchall()
        # print(data)
        cursor.execute("alter table player_ranklist add Rank int not null")
        connection.commit()
        for x in data:
            print(x)
            cursor.execute("update player_ranklist set rank = " + str(x[1]) + " where player_id = " + str(x[0]) + " ;")
            connection.commit()

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

def player_game_details(email):
    with connection.cursor() as cursor:
        cursor.execute("select player_id from player_email where email like \"%s\"",[email])
        player_id = cursor.fetchall()[0][0]
        cursor.execute("SELECT no_of_wins,no_of_losses,G.name FROM game_details, game G WHERE player_id = %s and G.id = game_id;",[player_id])
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

def player_games_not_played(email):
    with connection.cursor() as cursor:
        cursor.execute("select player_id from player_email where email like \"%s\"",[email])
        player_id = cursor.fetchall()[0][0]
        cursor.execute("SELECT name	FROM game WHERE game.id not in (SELECT game_id  FROM game_details WHERE player_id = %s and (no_of_wins <> %s or no_of_losses <> %s) );",[player_id,0,0])
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

def player_account_balance(email):
    with connection.cursor() as cursor:
        cursor.execute("select player_id from player_email where email like \"%s\"",[email])
        player_id = cursor.fetchall()[0][0]
        cursor.execute("SELECT acc.current_balance FROM account acc where acc.player_id = %s;",[player_id])
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

def player_ranklist():
    with connection.cursor() as cursor:
        cursor.execute("select rank,player_id,name from player_ranklist,player where player.id = player_ranklist.player_id order by rank asc;")
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