a = input("Enter a first word: ")
b = input("Enter a second word: ")
a_len = len(a)
b_len = len(b)
ab_len = a_len + b_len
print(a, end="")
if ab_len <= 30:
    for i in range(1,31 - ab_len):
        print(".", end="")
print(b)
