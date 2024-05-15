#Benjamin Kilgore - 1/22/23 CS102

#Enter House Value here
house_value = float(input('House Value: '))

#Fedral Taxes here 3.5% or 0.035
fed_tax = float(input('Fedral Tax Precentage: '))

#State Taxes here 6% or 0.06
state_tax = float(input('State Tax Precenage: '))

# calulates all presentages 
#amount_owed = house_value / house_value + 0.035 + 0.06

amount_owed = (house_value * fed_tax) + (house_value * state_tax) + house_value

# Displays result here 
print('Amount Owed: ', format(amount_owed,',.2f'))


