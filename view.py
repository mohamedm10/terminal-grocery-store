
def main_menu():
  text = '''
    Welcome to Main Menu
    Please select option.
      1. Admin 
      2. New Customer
      3. Registered Customer
      4. Close Program
  '''
  print(text)

def user_choice_form():
  option = input('select an option? ')
  return option
  
def login_form():
  username = input('enter username? ')
  password = input('enter password? ')
  return username,password

########## Admin Views
def admin_menu1():
  text = '''
    Welcome to Admin Menu
    Please select an option.
      1. Login
      2. Upload grocery
      3. View all grocery
      4. Edit grocery
      5. Delete grocery
      6. Display grocery details
      7. View all orders
      8. Search order by customer
      9. Exit
  '''
  print(text)

def upload_grocery_form():
  name = input('Medicine Name? ')
  exp_date = input('Expiry Date(dd-mm-yyyy)? ')
  price = input('Price? ')
  specs = input('Specifications? ')

  return name,exp_date,price,specs

def edit_grocery_form():
  record_number = int(input('record number? '))
  price = input('new price? ')
  
  return record_number,price

def find_order_form():
  customer = input('Enter customer name? ')
  return customer
  
########## New Customer Views
def new_customer_menu():
  text = '''
    Welcome New Customer
    Please select an option.
      1. View grocery details
      2. Register
      3. Exit.
  '''
  print(text)

def customer_registration_form():
  name = input('Name? ')
  address = input('Address? ')
  email = input('Email? ')
  telephone = input('Telephone? ')
  gender = input('Gender? ')
  dob = input('Date of Birth(dd-mm-yyyy)? ')
  user_id = input('Username? ')
  password = input('Password? ')
  confirm_pass = input('Confirm Password ')
  
  return [name, address, email, telephone, gender, dob, user_id, password, confirm_pass]
  
######## Registered Customer Views
def registered_customer_menu(customer_name):
  customer_name = 'Customer' if not customer_name else customer_name
  text = f'''
    Welcome back {customer_name}
    Please select an option.
    1. Login 
    2. View All groceries detail
    3. Place order and pay
    4. View orders
    5. View profile.
    6. Exit.
  '''
  print(text)

def place_order_form():
  product = input('Grocery name? ')
  price  = input('Price? ')
  quantity = input('Quantity? ')

  return product,price,quantity

def login_reminder():
  print('please login to continue!!')