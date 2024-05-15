#Benjamin Kilgore - 3/18/2022 - CS102 - Rosewood (edit)

def get_input():
    Orchestra = float(input('# of Orchestra Seats: '))

#Center Stage = 50.00
    Center = float(input('# of Center Stage Seats: '))

#Outer Stage = 25.00
    Outer = float(input('# of Outer Stage Seats: '))
    member = input('Are you a member Y or N: ')
    return Orchestra,Center,Outer,member

def cal(Orchestra,Center,Outer,memeber):
# Calulates the total of each seat cost
    total = Orchestra * 75 + Center * 50 + Outer * 25
    if memeber.upper()== 'Y':
        total = total * .95
    return total

def print1(total):
# Display total 
    print('Your total is', total)

#functions used
def main():
    Orchestra,Center,Outer,member =get_input()
    total=cal(Orchestra,Center,Outer,member)
    print1(total)

main()
#call to main