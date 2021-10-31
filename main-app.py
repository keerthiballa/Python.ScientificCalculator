from calculator import Calculator
import math

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def getOneNumber():     # get one number instead
    a = float(input("first number? "))
    return a

def switchDisplayModeInput(): #added by KB
    """
    Switch display mode (binary, octal, decimal, hexadecimal)
    switchDisplayMode() should rotate through the options
    :return:
    """
    return str(input('Select a display mode - bin, oct, dec, hex: '))

def trig_units_mode_input(): #added by KB
    """
    Switch trig units mode (Degrees, Radians)
    switchUnitsMode() should rotate through the options
    :return:
    """
    return input('Select deg or rad: ')

def displayResult(temp_display: float):
    print("\nDISPLAY:\n")
    print(temp_display)


def performCalcLoop(calc, temp_display): # KB - removed none assignment to temp_display
    print('\nBOO! Happy Halloween ;) \n\n "Welcome to your Scientific Calculator."')
    print("\nHere's a list of choices:")
    print('~' * 70)
    print("1 : Addition  \t\t               17 : Inverse sine")
    print("2 : Subtraction \t               18 : Inverse cosine")
    print("3 : Multiplication\t               19 : Inverse tangent")
    print("4 : Division  \t\t               20 : Trig units mode - Convert Radians to Degrees")
    print("5 : Square     \t                   21 : Trig units mode - Convert Degrees to Radians")
    print("6 : Square Root\t                   22 : Factorial")
    print("7 : Variable Exponentiation \t   23 : Log x")
    print("8 : Inverse of Display  \t       24 : 10 power x - Inverse nog")
    print("9 : Invert Sign (+/-)\t           25 : Ln x - Natural log")
    print("10 : Switch Display\t                     26 : e power x - Inverse natural log")
    print("11 : M+ \t\t                       27 : Pi")
    print("12 : MC \t\t                       28 : Exponentiation constant")
    print("13 : MRC \t\t                       29: Quit")
    print("14 : Sine")
    print("15 : Cosine")
    print("16 : Tangent")
    print('~' * 70)


    while True:
        try:
            choice = input("Enter number to choose your operation:\n")
        except:
            print("Please enter a valid number.")

        if choice == '20':
            print("Thanks for stopping by, have a great day.")
            break  # user types q to quit calulator.

        elif choice == '1':
            a, b = getTwoNumbers()
            temp_display = calc.add(a, b)
            displayResult(temp_display)

        elif choice == '2':
            a, b = getTwoNumbers()
            temp_display = calc.sub(a, b)
            displayResult(temp_display)

        elif choice == '3':
            a, b = getTwoNumbers()
            temp_display = calc.mult(a, b)
            displayResult(temp_display)

        elif choice == '4':
            a, b = getTwoNumbers()
            if b == 0:
                print("\nDISPLAY:\nErr")
            else:
                temp_display = calc.div(a, b)
            displayResult(temp_display)

        elif choice == '5':
            a = getOneNumber()
            temp_display = calc.sq(a)
            displayResult(temp_display)

        elif choice == '6':
            a = getOneNumber()
            temp_display = calc.sqrt(a)
            displayResult(temp_display)

        elif choice == '7':
            a, b = getTwoNumbers()
            temp_display = calc.varexp(a, b)
            displayResult(temp_display)

        elif choice == '8':
            a = getOneNumber()
            temp_display = calc.inverse(a)
            displayResult(temp_display)

        elif choice == '9':
            a = getOneNumber()
            temp_display = calc.invert_sign(a)
            displayResult(temp_display)



        elif choice == '10': #added by KB
                # switch display
            a = switchDisplayModeInput()
            displayResult(calc.switchDisplayMode(a,temp_display))

        #elif choice == 'M+':
        #elif choice == '11':


        #elif choice == '12''MC':

        #elif choice == '13''MRC':

        elif choice == '14': #added by KB
            a = trig_units_mode_input()
            x=getOneNumber()
            if a == 'deg':
                temp_display = calc.sin_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.sin_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '15':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.cos_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.cos_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '16':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.tan_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.tan_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")

        elif choice == '17': #added by KB
            a = trig_units_mode_input()
            x=getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_sin_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_sin_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '18':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_cos_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_cos_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '19':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_tan_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_tan_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")

        elif choice == '20':  # added by KB
            x = getOneNumber()
            temp_display = calc.trig_units_mode_deg_to_rad(x)
            print(displayResult(temp_display)," radians")

        elif choice == '21':  # added by KB
            x = getOneNumber()
            temp_display = calc.trig_units_mode_rad_to_deg(x)
            print(displayResult(temp_display), " degrees")

        elif choice == '22':# added by KB
            x = getOneNumber()
            temp_display = calc.factorial(x)
            print(displayResult(temp_display))

        elif choice =='23':# added by KB
            print("Enter your number and base as prompted below\n")
            x,b = getTwoNumbers()
            temp_display = calc.log(x,b)
            print(displayResult(temp_display))

        elif choice == '24':# added by KB
            x = getOneNumber()
            temp_display = calc.inverse_log(x)
            print(displayResult(temp_display))

        elif choice == '25':# added by KB
            x = getOneNumber()
            temp_display = calc.ln(x)
            print(displayResult(temp_display))

        elif choice == '26':# added by KB
            x = getOneNumber()
            temp_display = calc.inv_ln(x)
            print(displayResult(temp_display))

        elif choice == '27':# added by KB
            temp_display = calc.pi()
            print(displayResult(temp_display))

        elif choice == '28':# added by KB
            temp_display = calc.e()
            print(displayResult(temp_display))

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc, 0) #KB - passed second input parameter 0
    print("Done Calculating.")


if __name__ == '__main__':
    main()