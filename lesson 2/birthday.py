nowDay = 4
nowMonth = 10
nowYear = 2019

day = int(input('Enter day>'))
month = int(input('Enter month>'))
year = int(input('Enter year>'))

if (month > nowMonth) or (month == nowMonth and day > nowDay):
    print (nowYear - year - 1)
else:
    print(nowYear - year)