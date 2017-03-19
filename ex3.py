names = ['john Doe', 'jane doe','jonny turk']

#change the first name in the list
names[0] = 'foo Bar'
print('Names now:', names)

#append some more names
names.append('molly mormon')
names.append('joe bloggs')
print('Names finally:',names)
print('last name in the list: %s' %names[-1])

#You can join lists using str.join() method
joined_names = '\n'.join(names)
print('\nList of names:')
print(joined_names)