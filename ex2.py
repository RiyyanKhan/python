dob= input("enter date of birth in yyyy-mm-dd format: ")
date_parts= dob.split('-')
[year,month,day]= date_parts

dob_timestamp = float(year)+float(month)/12+float(day)/365
[today_year,today_month,today_day]=['2073','12','05']
today_timestamp = float(today_day)+float(today_month)/12+float(today_day)/365

 
years= today_timestamp-dob_timestamp
months= (years-int(years))*12
print('your age is %d years %d months' %(years, months))