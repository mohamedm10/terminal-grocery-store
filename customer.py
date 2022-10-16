# 

def register(customer_info):
  name, address, email, telephone, gender, dob, user_id, password, confirm_pass = customer_info
  customer = f'{name},{address},{email},{telephone},{gender},{dob},{user_id},{password},{confirm_pass}'
  
  with open('customer.txt','a+') as f:
    print(str(customer),file=f)    
  print('registration successful!!!!')

def login(username,password):
  with open('customer.txt','r') as f:
    for line in f.readlines():
      user = line.strip().split(',')
      if user[6] == username and user[7] == password:
        print('user logged in successfully!!')
        return user[0]
      else:
        message = 'invalid user id/password'
    print(message)

def view_profile(customer):
  if customer:
    with open('customer.txt','r') as f:
      print('Name |', 'Address |', 'Email |', 'Telephone |', 'Gender')
      print('-'*50)
      for line in f.readlines():
        line = line.strip().split(',')
        if line[0] == customer:
          print(line[0],' '*2,line[1],' '*2,line[2],' '*2,line[3],' '*2,line[4])
  else:
    print('please login to view profile!!')