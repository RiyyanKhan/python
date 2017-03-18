#Write the program to ask for the marks of the five subjects
s1= input("Enter the marks of s1: ")
s2= input("Enter the marks of s2: ")
s3= input("Enter the marks of s3: ")
s4= input("Enter the marks of s4: ")
s5= input("Enter the marks of s5: ")
total= float(s1)+float(s2)+float(s3)+float(s4)+ float(s5)
percentage = ((float(total) /500) *100)
print("percentage is %.2f" %percentage)
