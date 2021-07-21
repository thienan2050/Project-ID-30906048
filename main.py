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
        if '----------- Personal Login -----------' in row[0]:
            total+=1
        if 'Full name' in row[0]:
            fullName.append(row[0].split(':')[1].strip())
        if 'Date Of Birth' in row[0]:
            DOBirth.append(row[0].split(':')[1].strip())
        if 'Email Address' in row[0] and '@' in row[0]:
            emailAddress.append(row[0].split(':')[1].strip())
        if 'Address' in row[0] and not '@' in row[0]:
            address.append(row[0].split(':')[1].strip())
        if 'Phone Number' in row[0]:
            phoneNumber.append(row[0].split(':')[1].strip())
        if 'Town' in row[0]:
            town.append(row[0].split(':')[1].strip())
        if 'Card number' in row[0]:
            cardNumber.append(row[0].split(':')[1].strip().replace(' ',''))
        if 'Card exp' in row[0]:
            cardExp.append(row[0].split(':')[1].strip())
        if 'Security code' in row[0]:
            securityCode.append(row[0].split(':')[1].strip())
        if 'Sortcode' in row[0]:
            sortCode.append(row[0].split(':')[1].strip())
        if 'Account' in row[0]:
            account.append(row[0].split(':')[1].strip())
        if 'Submitted by' in row[0]:
            submitted.append(row[0].split(':')[1].strip())
        if 'Location' in row[0]:
            location.append(row[2].strip())
for i in range(0, total):
    print(cardNumber[i]+'|'+cardExp[i]+'|'+securityCode[i]+'|'+fullName[i]+'|'+address[i]+'|'+town[i]+'|'+location[i]+'|'+phoneNumber[i]+'|'+emailAddress[i]+'|'+DOBirth[i]+'|'+sortCode[i]+'|'+account[i]+'|'+submitted[i])

with open("output.txt",'w') as f:
    for i in range(0, total):
        f.write(cardNumber[i]+'|'+cardExp[i]+'|'+securityCode[i]+'|'+fullName[i]+'|'+address[i]+'|'+town[i]+'|'+location[i]+'|'+phoneNumber[i]+'|'+emailAddress[i]+'|'+DOBirth[i]+'|'+sortCode[i]+'|'+account[i]+'|'+submitted[i]+'\n')    





            



        


            



        