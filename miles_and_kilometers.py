##### miles and kilometers #####
        

def kilometers_to_miles():

    conversion_factor = 0.621371

    correct_value = True

    while correct_value:
        kilometers = float(input("Enter value in kilometers: "))
        miles = kilometers * 0.621371
        if kilometers > 0:
            correct_value = False
        else:
            print("You can not enter 0.")

    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
    
# kilometers_to_miles()

def miles_to_kilometers():

    conversion_factor = 0.621371

    correct_value = True

    while correct_value:
        miles = float(input("Enter value in miles: "))
        kilometers = miles / 0.621371
        if miles > 0:
            correct_value = False
        else:
            print("You can not enter 0.")

    print('%0.2f miles is equal to %0.2f kilometers' %(miles,kilometers))

# miles_to_kilometers()
