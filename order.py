#
# import grocery

def view_all_orders():
  with open('order.txt') as f:
    print('Customer Name |', 'Grocery |', 'Price |', 'Quantity')
    print('-'*50)
    for index,line in enumerate(f.readlines(),1):
      line = line.strip().split(',') 
      print(index,' ',line[0],' '*3,line[1],' '*3,line[2],' '*3,line[3])

def find_order(customer):
  with open('order.txt') as f:
    print('Customer Name |', 'Grocery |', 'Price |', 'Quantity')
    print('-'*50)
    for index,line in enumerate(f.readlines(),1):
      line = line.strip().split(',') 
      if line[0] == customer:
        print(index,' ',line[0],' '*3,line[1],' '*3,line[2],' '*3,line[3])

def place_order(customer,order_details):
  grocery,price,quantity = order_details
  with open('order.txt', 'a+') as f:
    order = f'{customer},{grocery},{price},{quantity}'
    print(order,file=f)
  print('order placed successfully')

def view_customer_order(customer):
  pass