while 1:
    print("Good morning, pls select an option from the menu below")
    print("1. Area of rectangle")
    print("2. Volume of a cube")
    print("3. Area of a circle")
    print("4. Circumference of a circle")
    print("Exit the program")

    choice = input("Enter your choice (1-5) :) Option \"5\" will be for exiting: ")

    if choice == "1":

        print("You selected the area of a rectangle")
        l = float(input("Enter the length of the rectangle: "))
        w = float(input("Enter the width of the rectangle: "))
        area_rectangle = l * w
        print("The area of the rectangle is:", area_rectangle)
    elif choice == "2":
        print("You selected the volume of a cube")
        l = float(input("Enter the side length of the cube: "))
        w = float(input("Enter the width of the cube: "))
        h = float(input("Enter the height of the cube: "))
        volume_cube = l * w * h
        print("The volume of the cube is:", volume_cube)
    elif choice == "3":
        print("You selected the area of a circle")
        r = float(input("Enter the radius of the circle: "))
        area_circle = 3.14159 * (r ** 2)
        print("The area of the circle is:", area_circle)
    elif choice == "4":
        print("You selected the circumference of a circle")
        r = float(input("Enter the radius of the circle: "))
        circumference_circle = 2 * 3.14159 * r
        print("The circumference of the circle is:", circumference_circle)
    elif choice == "5":
        print("Exiting the program. Goodbye! Have a good one :)")
    break

