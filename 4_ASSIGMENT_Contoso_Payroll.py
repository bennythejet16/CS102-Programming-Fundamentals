# Contoso Payroll - Benjamin Kilgore - 2/17/2023 - CS102

#Varables
start_amount = 0.02
daty_started = 1

#loop used to get input from the user and calulate the data
for number in range(1):
    day = int(input('how many days did you work?: '))
    amount_end = day * start_amount * 2
    
#prints the total
print('Your total is: ', amount_end)
