# 

def upload_grocery(name,exp_date,price,specs):
  # grocery = {'Medicine Name': name, 'Expiry Date': exp_date, 'Price': price, 'Specification': specs}
  grocery = f'{name},{exp_date},{price},{specs}'
  
  with open('grocery.txt','a+') as f:
    print(grocery,file=f)
  print('new grocery record saved !!!')
  
def view_all_grocery():
  with open('grocery.txt','r') as f:
    print('Medicine Name |', 'Expiry date |', 'Price |', 'Specification')
    print('-'*50)
    for index,line in enumerate(f.readlines(),1):
      line = line.strip().split(',') 
      print(index,' ',line[0],' '*7,line[1],' '*7,line[2],' '*5,line[3])

def edit_grocery(record_number,price):
  with open('grocery.txt', 'a+') as f:
    f.seek(0)
    data = []
    for index,line in enumerate(f.readlines()):
      line = line.strip().split(',')
      if index == record_number-1:
        line[2] = price
        data.append(','.join(line))
      else:
        data.append(','.join(line))
    f.seek(0)
    f.truncate()
    for i in data:
      print(i,file=f)

def delete_grocery():
  record_number = int(input('record number to delete? '))
  with open('grocery.txt', 'a+') as f:
    f.seek(0)
    data = []
    for index,line in enumerate(f.readlines()):
      line = line.strip().split(',')
      if index == record_number-1:
        pass
      else:
        data.append(','.join(line))
    f.seek(0)
    f.truncate()
    for i in data:
      print(i,file=f)
  
def display_grocery_detail(name,detail):
  pass