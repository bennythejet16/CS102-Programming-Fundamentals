# Benjamin Kilgore - 3/20/2023 - CS-102

# main function 
def main():
    #input number of days the user wants to record 
    temp = int(input('How many days would you like to record: '))
    #file that the editor records to
    temp_file = open('temp.txt', 'w')

    print('Enter the temperature for each day')
    #loop used to input the days. 
    for count in range(1, temp + 1):
        day_temp = float(input(f'Day #{count}: '))
        temp_file.write(f'{day_temp}\n')
    #close the file
    temp_file.close()


if __name__ == '__main__':
    main()
#close the main