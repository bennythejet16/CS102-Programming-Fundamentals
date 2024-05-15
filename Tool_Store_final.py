# Tool Store (Final) - Benjamin Kilgore - 3/23/2023 - CS102

# menu prices.
def menu():
    print('Toolboxes for sale!')
    print('Toolbox 10 Piece = 30.00$')
    print('Toolbox 20 Piece = 45.00$')
    print('Toolbox 50 Piece = 65.00$')
    
# main function.
def main():
    #try and except function.
    try:
        #returns the menu so the user can see it.
        menu()

        #inputs data from the user
        toolbox10 = int(input('How many 10 piece tools boxes do you need?: '))
        toolbox20 = int(input('How many 20 piece tool boxes do you need?: '))
        toolbox50 = int(input('How many 50 piece tool boxes do you need?: '))
        ship = input('Would you like in store pickup or to be shipped? (cost $11.00) Y or N: ')
        
        # if statment if the user wants shipping or not.
        if ship.upper() == 'Y':
            shipto = 11.00
        else:
            shipto = 0.00



        #constant varibles for prices for each toolkit.
        TOOLB10 = 30.00
        TOOLB20 = 45.00
        TOOLB50 = 65.00

        #price calulations.
        tb10 = toolbox10 * TOOLB10
        tb20 = toolbox20 * TOOLB20
        tb50 = toolbox50 * TOOLB50

        #Calulates the total that the user inputs.
        final_total = tb10 + tb20 + tb50 + shipto
        
        #prints the final total and shipping cost.
        print('Your Shipping cost is $',shipto)
        print('Your final total is $',final_total)

    except:
        print('Error')
    #main close.
main()
