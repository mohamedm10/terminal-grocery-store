
class Admin():
  admin_username = 'root'
  admin_password = 'qwerty'
  def set_admin(username,password):
    Admin.admin_username = username
    Admin.admin_password = password

  def login(username,password):
    if username == Admin.admin_username and password == Admin.admin_password:
      print('>>>>logging successful')
    else:
      print('>>>>wrong username/password')
      
  @classmethod
  def display(self):
    print('username:',self.admin_username,' password:',self.admin_password)