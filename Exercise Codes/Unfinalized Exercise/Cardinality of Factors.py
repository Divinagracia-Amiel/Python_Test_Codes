#cardinality of factors
def card_fact(x):
    limit = int(x/2)
    card = 0
    for i in range(1, limit+1):
        fact = x % i
        if fact == 0:
            card += 1
    return card
 
def cardinality(x):
    card = 0
    for i in x:
        card += 1
    return card

print(card_fact(6))
name = ['Amiel Osias Divinagracia']
order = 0
print("Press 0 to exit")
while True:
    add_name = str(input("Enter name: "))
    if add_name == '0':
        break
    name.append(add_name)
print("The names of the students are the following: ")
for i in name:
    order += 1
    print(f"{order}.)",i)
stud_quan = cardinality(name)
print(f"There are {stud_quan} students enrolled in this school")

    

