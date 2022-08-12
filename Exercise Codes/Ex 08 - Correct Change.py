input_cents = False
while input_cents == False:
    try:
        input_cents = int(input("Input the cents:\n"))
    except ValueError:
        print("Please enter an integer.")
        continue
    break
dollars = int(input_cents / 100)
dollar_rem = input_cents % 100
quarter = int(dollar_rem / 25)
quarter_rem = dollar_rem % 25
if dollars == 0 and quarter_rem < 5 and quarter == 0:
    cents = quarter_rem
    print(f"Your change is: {cents} cent/s")
elif dollars >= 1 and quarter_rem == 0 and quarter == 0:
    print(f"Your change is: {dollars} dollar/s")
elif dollars == 0 and quarter >= 1 and quarter_rem == 0:
    print(f"Your change is: {quarter} quarter/s")
elif quarter >= 1 and quarter_rem == 0:
    print(f"Your change is: {dollars} dollar/s and {quarter} quarter/s")
elif quarter_rem >= 0 and quarter_rem < 100:
    dime = int((quarter_rem / 10))
    dime_rem = quarter_rem % 10
    if dime_rem >= 0 and dime_rem < 25:       
        nickel = int(dime_rem / 5)
        nickel_rem = dime_rem % 5
        cents = nickel_rem
        if dollars == 0 and cents == 0:
            if quarter == 0:
                if dime == 0:
                    print(f"Your change is: {nickel} nickel/s")
                elif nickel == 0:
                    print(f"Your change is: {dime} dime/s")
                else:
                    print(f"Your change is: {dime} dime/s, {nickel} nickel/s")
            elif quarter > 0:
                if dime == 0:
                    print(f"Your change is: {quarter} quarter/s, and {nickel} nickel/s")
                elif nickel == 0:
                    print(f"Your change is: {quarter} quarter/s, and {dime} dime/s")
        elif dollars == 0:
            if quarter == 0:
                if dime == 0:
                    print(f"Your change is: {nickel} nickel/s, and {cents} cent/s")
                elif nickel == 0:
                    print(f"Your change is: {dime} dime/s, and {cents} cent/s")
                else:
                    print(f"Your change is: {dime} dime/s, {nickel} nickel/s, and {cents} cent/s")
            elif quarter > 0:
                if dime == 0 and nickel == 0:
                    print(f"Your change is: {quarter} quarter/s, and {cents} cent/s")
                elif dime == 0:
                    print(f"Your change is: {quarter} quarter/s, {nickel} nickel/s, and {cents} cent/s")
                elif nickel == 0:
                    print(f"Your change is: {quarter} quarter/s, {dime} dime/s, and {cents} cent/s")
                elif dime > 0 and nickel > 0:
                    print(f"Your change is: {quarter} quarter/s, {dime} dime/s, {nickel} nickel/s, and {cents} cent/s")
        elif cents == 0:
            if quarter == 0:
                if dime == 0:
                    print(f"Your change is: {dollars} dollar/s, and {nickel} nickel/s")
                elif nickel == 0:
                    print(f"Your change is: {dollars} dollar/s, and {dime} dime/s")            
                else:
                    print(f"Your change is: {dollars} dollar/s, {dime} dime/s, and {nickel} nickel/s")
            elif dime > 0 and nickel > 0:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s, {dime} dime/s, and {nickel} nickel/s")
            elif dime == 0:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s, and {nickel} nickel/s")
            elif nickel == 0:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s and {dime} dime/s")
        else:
            if quarter == 0:
                if dime == 0 and nickel == 0:
                    print(f"Your change is: {dollars} dollar/s, and {cents} cent/s")
                elif dime == 0:
                    print(f"Your change is: {dollars} dollar/s, {nickel} nickel/s, and {cents} cent/s")
                elif nickel == 0:
                    print(f"Your change is: {dollars} dollar/s, {dime} dime/s, and {cents} cent/s")          
            elif dime == 0 and nickel == 0:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s, and {cents} cent/s")
            elif dime == 0:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s, {nickel} nickel/s, and {cents} cent/s")
            elif nickel == 0:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s, {dime} dime/s, and {cents} cent/s")
            else:
                print(f"Your change is: {dollars} dollar/s, {quarter} quarter/s, {dime} dime/s, {nickel} nickel/s, and {cents} cent/s")
                
                
                
                
