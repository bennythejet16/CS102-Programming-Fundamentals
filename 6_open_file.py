# Benjamin Kilgore - 3/20/2023 - CS-102

# function used to calulate averges 
def file_avg(file_name):

    #open the file
    file = open(file_name)

    list_number = file.readlines()

    total = 0 

    for number in list_number:
        total = total + float(number)

    file.close()

    return total / len(list_number)
#gets the file name from the user, needs to be in the same dir
input_filename = input("Tempture File location?: ")

average = file_avg(input_filename)

#prints the average
print("Average:", average)