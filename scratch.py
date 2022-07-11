from miles_and_kilometers import kilometers_to_miles, miles_to_kilometers
import time

allowed_choices = [1, 2]

choice = True

while choice:

    welcome = int(input("Enter 1 for kilometers to miles converter \n" 
                        "Enter 2 for miles to kilometers converter: " ))

    if welcome in allowed_choices:
        choice = False
        
    else:
        print("""Error: "You have to choose 1 or 2" """)
        time.sleep(2)

if welcome == 1:
    kilometers_to_miles()
elif welcome == 2:
    miles_to_kilometers()