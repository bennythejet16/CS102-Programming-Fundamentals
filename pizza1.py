def menu():
    print("Pizza's For Sale")
    print('Beef = 12.00$')
    print('Cheese = 10.00$')
    print('Supreme = 15.00$')

def delchg(delivery):
    if delivery.upper() == 'Y':
        deliveryCharge = 1.50
    else:
        deliveryCharge = 0
    return deliveryCharge

def main():
    try:
        BEEFPIZZA = 12.00
        CHEESEPIZZA = 10.00
        SUPREMEPIZZA = 15.00
        menu()
        #get input
        beef = int(input('Enter the number of beef pizzas: '))
        cheese = int(input('Enter the number of cheese pizzas: '))
        supreme = int(input('Enter the number of supreme pizzas: '))
        delivery = input('Do you want delivery Y or N: ')

        #get delivery
        deliveryCharge=delchg(delivery)

        #add pizzas * pizza price 
        Tpizzas = beef + cheese + supreme
        Tbeef = beef * BEEFPIZZA 
        Tcheese = cheese * CHEESEPIZZA
        Tsupreme = supreme * SUPREMEPIZZA

        #calulate subtotal
        subtotal = Tbeef + Tcheese + Tsupreme 

        #calulate discount
        if Tpizzas >3:
            discount = .10
        else:
            discount = 0
        #find total discount 
        Tdiscount = subtotal * discount
        total = subtotal - Tdiscount
        total = total + deliveryCharge

        print(f'The Subtotal is: {subtotal:.2f}')
        print(f'The delivery charge is: {deliveryCharge:.2f}')
        print(f'The discount is: {Tdiscount:.2f}')
        print(f'The total is: {total:.2f}')
    except:
        print('Error')
main()

