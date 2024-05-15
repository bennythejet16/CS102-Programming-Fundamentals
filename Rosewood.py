#Benjamin Kilgore - 3/4/2022 - CS102

def get_input():
    Orchestra = float(input('# of Orchestra Seats: '))

#Center Stage = 50.00
    Center = float(input('# of Center Stage Seats: '))

#Outer Stage = 25.00
    Outer = float(input('# of Outer Stage Seats: '))
    return Orchestra,Center,Outer

def cal(Orchestra,Center,Outer):
# Calulates the total of each seat cost
    total = Orchestra * 75 + Center * 50 + Outer * 25
    return total

def print1(total):
# Display total 
    print('Your total is', total)

#functions used
def main():
    Orchestra,Center,Outer =get_input()
    total=cal(Orchestra,Center,Outer)
    print1(total)

main()
#call to main