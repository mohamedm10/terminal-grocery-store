# Name
# TP number
# from model import Admin
import view
from customer import register,view_profile,login
import grocery
import order
import admin

def run():
  prog = True
  while prog:
    print(' ------------\n','program running...\n','-----------')
    view.main_menu()
    option = view.user_choice_form()
    if option == '1' : #display Admin menu
      while True:
        view.admin_menu1()
        option = view.user_choice_form()
        if option == '1': #login
          username,password = view.login_form()
          admin.admin_login(username,password)
        elif option == '2': #upload grocery
          name,exp_date,price,specs = view.upload_grocery_form()
          grocery.upload_grocery(name,exp_date,price,specs)
        elif option == '3': #view all grocery
          grocery.view_all_grocery()
        elif option == '4': #edit grocery
          record_number,price = view.edit_grocery_form()
          grocery.edit_grocery(record_number,price)
        elif option == '5': #delete grocery
          grocery.delete_grocery()
        # elif option == '6': find grocery details
        elif option == '7': #view all orders
          order.view_all_orders()
        elif option == '8': #search order by customer
          customer = view.find_order_form()
          order.find_order(customer)
        elif option == '9': #exit
          break
        # username,password = ask_login()
        # Admin.login(username,password)
    elif option == '2' : #display New Customer menu
      while True:
        view.new_customer_menu()
        option = view.user_choice_form()
        if option == '1': #view grocery details
          grocery.view_all_grocery()
        elif option == '2': #register
          customer_info = view.customer_registration_form()
          register(customer_info)
        elif option == '3': #exit
          break
    elif option == '3' : #display Registered Customer menu
      logged_in_customer = None
      while True:
        view.registered_customer_menu(logged_in_customer)
        option = view.user_choice_form()
        if option == '1': #login
          username,password = view.login_form()
          logged_in_customer = login(username,password)
        # elif option == '2': view all grocery
        elif option == '3': #place order
          order_details = [product,price,quantity] = view.place_order_form()
          order.place_order(logged_in_customer,order_details) if logged_in_customer else view.login_reminder()
        # elif option == '4': view orders  
        elif option == '5': #view profile
          view_profile(logged_in_customer)
        elif option == '6': #exit
          break
    elif option == '4':
      break
    else : #ask user to choose from given options
      print('invalid choice!!!!, choose from options given....')
      continue
    # prog = False
  print('program stopped!!!')
    

if __name__ == '__main__':
  run()