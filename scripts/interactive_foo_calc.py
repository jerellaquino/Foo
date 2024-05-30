from foo import sphereVolume, sphereSA

active = True

while active:
    print("Welcome to the foo physics calculator interactive script. \n" \
            "Please select a foo physics operation: \n" \
            "1. volume of sphere\n" \
            "2. Surface area of sphere\n" \
            "3. exit \n")

    user_option = int(input("Choose an option from 1, 2, 3: "))

    if (user_option == 1):
        r =  float(input("To calculate sphere volume, please enter the radius of the sphere: \n"))
        print("\n RESULT: sphere volume = ", sphereVolume(r), "\n")

    elif (user_option == 2):
        r =  float(input("To calculate sphere suraface area, please enter the radius of the sphere: \n"))
        print("\n RESULT: sphere surface area = ", sphereSA(r), "\n")
    
    elif (user_option == 3):
        print("exiting foo calculator script, bye!\n")
        break

    else:
        print("invalid input, please try again or enter '3' to exit")
