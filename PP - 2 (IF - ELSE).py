
n1 = float(input("Enter value n1: "))
n2 = float(input("Enter value n2: "))
n3 = float(input("Enter value n3: "))


if n1 > n2 and n1 > n3:
    print("N1 is the biggest")
elif n2 > n1 and n2 > n3:
    print("N2 is the biggest")
elif n3 > n1 and n3 > n2:
    print("N3 is the biggest")
else:
    print("Invalid numbers")
