# welcome the customer
print("Welcome to Dylan's House of Pies! Here is our selection: \n")

# fill out the pie menu
pies = ["Apple", "Pecan", "Pumpkin", "Peach", "Key Lime"]

# set the order list
orders = [0,0,0,0,0]

# set variable to get into while loop
again = True

while again == True:
    i = 1
    # print menu
    for pie in pies:
        print("(" + str(i) + ") " + pie)
        i = i + 1

    # get order
    order = int(input("\nWhich pie would you like?: "))

    orders[order - 1] = orders[order - 1] + 1

    print("Great! One " + pies[order - 1] + " pie coming up!")

    # ask if more pie is wanted
    more_pie = input("Would you like another pie? (y)es or (n)o: ")

    if(more_pie == "y"):
        again = True
    elif(more_pie == "n"):
        again = False

j = 0
# total order
print("Here is your total order: \n")
for order in orders:
    if order > 0:
        print(str(order) + " " + pies[j])
    j = j + 1

# thank the customer
print("\n Thanks for shopping at Dylan's House of Pies!")