#Benjamin Kilgore - 3/20/23 - CS102

def menu():
    print("Pizzas for sale")
    print("Cheese = 10.00$")
    print("Beef = 12.00$")
    print("supreame = 15.00$")

def delcharge(delivery):
    if delivery.upper()=='Y':
        deliverycharge = 1.50
    else:
        deliverycharge =0
    del deliverycharge

def main():
    BEEFPIZZA = 12.00
    CHEESEPIZZA = 10.00
    SUPREMEPIZZA = 15.00
    menu()

    #get input
    beef = int(input('Enter the amount of beef pizzas: '))
    cheese = int(input('Enter the amount of cheese pizzas: '))
    supreame = int(input('Enter the amount of supreame: '))
    delivery = input('Do you want your pizzas delivered Y or N')
    #get delivery

    deliverycharge=delcharge(delivery)



    #add pizzas * pizza price 
    tpizzas = beef + cheese + supreame
    tbeef = beef * BEEFPIZZA 
    tcheese = cheese * CHEESEPIZZA 
    tsupreme = supreame * SUPREMEPIZZA
    #calulate subtotal
    subtotal = tbeef + tcheese + tsupreme + deliverycharge
    #calulate discount 
    if tpizzas >3:
        discount = .10
    else :
        discount = 0
    #find total discount 
    tdiscount =  subtotal * discount
    total  =  subtotal - tdiscount
    total = total + deliverycharge

    #print totals 
    print(f'The subtotal is: {subtotal:.2f}')
    print(f'The delivery charge is: {deliverycharge:.2f}')
    print(f'The discount is: {tdiscount:.2f}')
    print(f'The total is {total:.2f}')

main()