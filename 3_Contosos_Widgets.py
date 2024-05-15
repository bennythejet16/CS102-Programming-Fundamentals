# Contoso's Widgets - Benjamin Kilgore - 2/2/2023 - CS102

#user inputs data for how many widgets they want to buy
widgets = int(input('How many widgets you would like to buy?:'))


price = 99.00

#user inputs data, it gets a discount depending on how much is being bought
if widgets < 10:
    discount = 0
elif widgets >= 10 and widgets <= 19:
    discount = .10 
elif widgets >= 20 and widgets <= 49:
    discount = .20
elif widgets >= 50 and widgets <= 99:
    discount = .30
elif widgets >= 100:
    discount = .40

# data given gets calulated. 
widget_total = widgets * price

discount_precent = (widget_total) * discount

final_total = widget_total - discount_precent


# data is calulated and displayed to the user.
print('Your final total is: ', final_total)







