first_name = input('your first name')
last_name = input('your last name')
  
  #old style formating
 print('hello %s %s!' %(first_name,last_name))

 #new style formating
 print('hello {} {}'.format(first_name,last_name))
 print('hello {0} {1}'. format(first_name,last_name))


  # this is where you will feel the difference
 print('hello {1} {0}'.format(first_name,last_name))
 print('hello {0} {0} {1}'.format(first_name,last_name))