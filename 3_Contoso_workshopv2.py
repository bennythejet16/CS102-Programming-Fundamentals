# Contoso Workshop - Benjamin Kilgore - 2/5/2023 - CS102

# Displays to the user what workshops and loactions are available.
print ('\tWORKSHOPS \tRegistration Fee \tDays')
print ('1) Handling Stress \t$2000 \t\t\t3 ')
print ('2) Time Management\t$800 \t\t\t3 ')
print ('3) Supervision Skills\t$1500 \t\t\t3 ')
print ('4) How to Interview \t$500 \t\t\t1\n')

print ('\tLOCATION \tLodging Fee per Day')
print ('1) Austin \t\t$150')
print ('2) Chicago\t\t$225 ')
print ('3) Phoenix\t\t$175 ')
print ('4) Orlando\t\t$300 ')

# gets input from the user.
workshop_number = int(input('What lesson number would you like to take? (1-4): '))

location_number = int(input('What location number? (1-4): '))

if workshop_number == 1:
    workshop_fee= 2000
    days = 3
elif workshop_number == 2:
    workshop_fee = 800
    days = 3
elif workshop_number == 3:
    workshop_fee = 1500
    days = 3 
elif workshop_number == 4:
    workshop_fee = 500
    days = 1
else:
    workshop_fee = 0
    days = 0

if location_number == 1:
    lodgingfee = 150
elif location_number == 2:
    lodgingfee = 225
elif location_number == 3:
    lodgingfee = 175
elif location_number == 4:
    lodgingfee = 300
else:
    lodgingfee = 0

# the data that was given by the user gets calulated.
lodging_total = lodgingfee * days

total = lodging_total + workshop_fee

# the data gets printed on screen.
print('Your registration fee is: \t$',format(workshop_fee,',.2f'))

print('Your total lodging fee is: \t$',format(lodgingfee,',.2f'))

print('Your total is:             \t$',format(total,',.2f'))
