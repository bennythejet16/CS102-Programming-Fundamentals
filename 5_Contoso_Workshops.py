# Contoso Workshop - Benjamin Kilgore - 3/5/2023 - CS102

# Displays to the user what workshops and loactions are available.
#print_workshop():
print ('\tWORKSHOPS \tRegistration Fee \tDays')
print ('1) Handling Stress \t$2500 \t\t\t3 ')
print ('2) Time Management\t$850 \t\t\t3 ')
print ('3) Supervision Skills\t$1000 \t\t\t3 ')
print ('4) How to Interview \t$600 \t\t\t1\n')

print ('\tLOCATION \tLodging Fee per Day')
print ('1) Austin \t\t$170')
print ('2) Chicago\t\t$250 ')
print ('3) Phoenix\t\t$175 ')
print ('4) Orlando\t\t$300 ')

#Gets input from the user 
def get_input():
    workshop_number = float(input('What lesson number would you like to take?: '))
    location_number = float(input('What location number?: '))
    return workshop_number,location_number

#Statemets to determind how much its going to cost
def workshop(workshop_number,location_number):
    if workshop_number == 1:
        workshop_fee= 2500
        days = 3
    elif workshop_number == 2:
        workshop_fee = 850
        days = 3
    elif workshop_number == 3:
        workshop_fee = 1000
        days = 3 
    elif workshop_number == 4:
        workshop_fee = 600
        days = 1
    else:
        workshop_fee = 0
        days = 0

    if location_number == 1:
        lodgingfee = 170
    elif location_number == 2:
        lodgingfee = 250
    elif location_number == 3:
        lodgingfee = 175
    elif location_number == 4:
        lodgingfee = 300
    else:
        lodgingfee = 0
    return lodgingfee,workshop_fee,days

#calculate what the user put in
def cal(lodgingfee,days,workshop_fee):
    lodging_total = lodgingfee * days

    total = lodging_total + workshop_fee
    return total,lodging_total

#main function
def main():
    workshop_number,location_number =get_input()
    lodgingfee,workshop_fee,days=workshop(workshop_number,location_number)
    total,lodging_total=cal(lodgingfee,days,workshop_fee)
 
    print('Your registration fee is: \t$',format(workshop_fee,',.2f'))

    print('Your total lodging fee is: \t$',format(lodgingfee,',.2f'))

    print('Your Total is:             \t$',format(total,',.2f'))


main()