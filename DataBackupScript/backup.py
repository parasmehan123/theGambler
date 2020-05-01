import mysql.connector
from mysql.connector import errorcode
import xlsxwriter

def writeListToExcel(table_name, data_list):
    with xlsxwriter.Workbook('BackupData/'+table_name+'_backup.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(data_list):
            worksheet.write_row(row_num, 0, data)

# Obtain connection string information from the portal
config = {
  'host':' gambler.mysql.database.azure.com',
  'user':' thegambler@gambler',
  'password':'james@123',
  'database':'casino'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

cursor.execute("show tables;")
table_name_data = cursor.fetchall()
table_names = [x[0] for x in table_name_data ]

for name in table_names:
  print(name + " back up complete")
  cursor.execute("describe " + name + ";")
  table_headers_data = cursor.fetchall()
  headers = [ x[0] for x in table_headers_data ]
  hearders = tuple(headers)
  cursor.execute("select * from " + name)
  data = cursor.fetchall()
  data.insert(0,headers)
  # print(data)
  writeListToExcel(name, data)
  # break






  # # Drop previous table of same name if one exists
  # cursor.execute("DROP TABLE IF EXISTS inventory;")
  # print("Finished dropping table (if existed).")

  # # Create table
  # cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  # print("Finished creating table.")

  # # Insert some data into table
  # cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  # print("Inserted",cursor.rowcount,"row(s) of data.")
  # cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
  # print("Inserted",cursor.rowcount,"row(s) of data.")
  # cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
  # print("Inserted",cursor.rowcount,"row(s) of data.")

  # # Cleanup
  # conn.commit()
  # cursor.close()
  # conn.close()
  # print("Done.")