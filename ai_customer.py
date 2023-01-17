import random
print(" ")
print("Welcome to the Café")



coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
coffee_numbers = [1, 2, 3, 4, 5]
choice = random.randint(1, 5)

        
def logic():
    if choice == 1:
        print(f"You picked {coffee[0]}")
    elif choice == 2:
        print(f"You picked {coffee[1]}")
    elif choice == 3:
        print(f"You picked {coffee[2]}")
    elif choice == 4:
        print(f"You picked {coffee[3]}")
    elif choice == 5:
        print(f"You picked {coffee[4]}")
    else:
        print(f"you picked: {choice} unfortunately this item doesn't exist")
   
   
   
   
def logic2():
    if choice > coffee_numbers[4] or choice < coffee_numbers[0]:
        raise IndexError("Invalid number")
        
# wanted to throw this in here, zero requirement for it but this is what would happen if you call an index which doesnt exist.



logic()
logic2()


try: 
    print("")        
except:
    print("")
finally:
    print("Thanks for stopping by, run script to continue.")


# the exception block is at the end as we want the 'finally' statement to come last

