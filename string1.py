s = input('enter a string')
#count the no of vowels
print("no.of 'a' = %s" %s.count ('a'))
print("no of 'e' =%s" %s.count('e'))
print("no of 'i' =%s" %s.count('i'))
print("no of 'o'= %s" %s.count('o'))
print("no of 'u'= %s" %s.count('u'))

#calculate percentage of vowels
total_vowels = s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
percentage = (float(total_vowels) / len(s)) *100
print("\n%.2f%% are vowels." %percentage)