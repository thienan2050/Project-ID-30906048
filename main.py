import csv
cardNumber = []
cardExp = []
securityCode = []
fullName = []
address = []
town = []
phoneNumber = []
emailAddress = []
DOBirth = []
sortCode = []
account = []
submitted = []
location = []
index = 0
total = 0




with open('data.csv', 'r') as file:
    i = 0
    reader = csv.reader(file)
    for row in reader:
        index += 1
        if row[0] == '----------- Personal Login -----------':
            total += 1
        if (index % 33) == 6:
            fullName.append(row[0].split(':')[1].strip())
        if (index % 33) == 7:
            DOBirth.append(row[0].split(':')[1].strip())
        if (index % 33) == 8:
            emailAddress.append(row[0].split(':')[1].strip())
        if (index % 33) == 9:
            address.append(row[0].split(':')[1].strip())
        if (index % 33) == 10:
            phoneNumber.append(row[0].split(':')[1].strip())
        if (index % 33) == 11:
            town.append(row[0].split(':')[1].strip())
        if (index % 33) == 19:
            cardNumber.append(row[0].split(':')[1].strip().replace(' ',''))
        if (index % 33) == 20:
            cardExp.append(row[0].split(':')[1].strip())
        if (index % 33) == 21:
            securityCode.append(row[0].split(':')[1].strip())
        if (index % 33) == 23:
            sortCode.append(row[0].split(':')[1].strip())
        if (index % 33) == 24:
            account.append(row[0].split(':')[1].strip())
        if (index % 33) == 26:
            submitted.append(row[0].split(':')[1].strip())
        if (index % 33) == 27:
            location.append(row[2].strip())
        
    

for i in range(0, total):
    print(cardNumber[i]+'|'+cardExp[i]+'|'+securityCode[i]+'|'+fullName[i]+'|'+address[i]+'|'+town[i]+'|'+location[i]+'|'+phoneNumber[i]+'|'+emailAddress[i]+'|'+DOBirth[i]+'|'+sortCode[i]+'|'+account[i]+'|'+submitted[i])

with open("output.txt",'w') as f:
    for i in range(0, total):
        f.write(cardNumber[i]+'|'+cardExp[i]+'|'+securityCode[i]+'|'+fullName[i]+'|'+address[i]+'|'+town[i]+'|'+location[i]+'|'+phoneNumber[i]+'|'+emailAddress[i]+'|'+DOBirth[i]+'|'+sortCode[i]+'|'+account[i]+'|'+submitted[i]+'\n')    





            



        