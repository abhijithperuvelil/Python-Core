from shapes.circle import area as ca
from shapes.circle import perimeter as cp
from shapes.rectangle import area as ra
from shapes.rectangle import perimeter as rp

choice = input("Enter shape (circle/rectangle): ")
op = input("Enter operation (area/perimeter): ")

if choice == "circle":
    r = float(input("Enter radius: "))

    if op == "area":
        print("Area =", ca(r))
    elif op == "perimeter":
        print("Perimeter =", cp(r))
    else:
        print("Invalid operation")

elif choice == "rectangle":
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    if op == "area":
        print("Area =", ra(l, b))
    elif op == "perimeter":
        print("Perimeter =", rp(l, b))
    else:
        print("Invalid operation")

else:
    print("Invalid shape")