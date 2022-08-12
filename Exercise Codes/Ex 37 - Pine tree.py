quan = -1
while quan < 0: #inputs
    try:
        quan = int(input("Enter the height of the tree's crown:\n"))
    except ValueError:
        print("Please enter an integer")
        continue
    if quan < 0:
        print("Please enter a positive integer")
        continue
count = 0      #Crown constants
count_ = 0
count_t = 0
pine = 1
for i in range(1, quan+1):       #Loop per line of crown
    while count_ < quan:         #Spaces before asterisk
        print(" ", end ="")
        count_ = count_ + 1
    while count < pine:          #Asterisk per new line
        print("*", end="")
        count = count + 1
    print("") #New line
    count = 0
    count_ = 0
    count_t = count_t + 1
    quan = quan - 1
    pine = pine + 2
sp_cnt = 0   #Trunk constants
width = 0
pn_width = (2 * count_t)-1  #Crown width
sp_sp = int(pn_width / 3)   #limit loop for spaces before tree trunks and the tree trunk itself
sp_rem = pn_width % 3       #Centering the trunk
trunk = round(count_t / 2)  #Height of the trunk relative to pine width
if pine > 9:                   #Width of tree trunk
    for i in range(1, trunk+1): #Height of tree trunk
        if sp_rem == 1:           #sp_rem for centering the tree trunk
            while sp_cnt < sp_sp+2: #sp_cnt loop for spaces before the trunk
                print(" ", end ="")
                sp_cnt = sp_cnt + 1
            while width < sp_sp-1:  #width loop for trunk width
                print("*", end ="")
                width = width + 1
        elif sp_rem == 2:
            while sp_cnt < sp_sp+2:
                print(" ", end ="")
                sp_cnt = sp_cnt + 1
            while width < sp_sp:
                print("*", end ="")
                width = width + 1
        elif sp_rem == 0:
            while sp_cnt < sp_sp+1:
                print(" ", end ="")
                sp_cnt = sp_cnt + 1
            while width < sp_sp:
                print("*", end ="")
                width = width + 1
        print("")      #New line
        sp_cnt = 0     #For resetting sp_cnt until tree trunk height is achieved
        width = 0      #For resetting width for a consistent width of the tree
if pine <= 9:          #Width of tree trunk if crown too small
    trunk = round((count_t / 2)+1)
    sp_sp = int((pine / 2))
    for i in range(1, trunk+1):
        while sp_cnt < sp_sp:
            print(" ", end ="")
            sp_cnt = sp_cnt + 1
        print("*")
        sp_cnt = 0
input("Press ENTER to continue...")