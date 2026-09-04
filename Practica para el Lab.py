age = int(input("Enter ur age:"))
heigh = float(input("Enter your heigh:"))
adult = str(input("Adult, yes or no:"))

adult_price= 15
free_entrance = 0
enfant_entrance = 8
elderly_price= 10

if age < 5:
    if adult == "yes":
        et = "Free entrance"
        price = 0
    else:
        et = "No puede ingresar sin un adulto"
        price = 0
elif age >= 5 and age <= 12:
    if heigh >= 1.20:
        et = "Enfant entrance - access to all amousements"
        price = enfant_entrance + 2
    else:
        et= "Enfant entrance, limited acccess"
        price = enfant_entrance
elif age >= 13:
    if age >= 65:
        et = "Elderly discount"
        price = elderly_price
    else:
        et = "Adult price"
        price = adult_price

print("Tipo de entrada =", et)
print("Price to pay: $", price)







