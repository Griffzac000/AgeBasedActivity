#TODO: Enter your age as an int.  Using the input function.
age = int(input("Enter your age: "))

if age < 5:
    # TODO: print the following "You should play with toys."
    print("You should play with toys.")
elif age >= 5 and age <= 12:
    # TODO: print the following "You can play outdoor game."
    print("You can play outdoor game.")
# TODO: handle the 13 to 17 condition
elif age >= 13 and age <= 17:
    print("You might enjoy video games.")

# TODO: handle the 18 or older condition.
elif age >= 18:
    print("You can try hiking or traveling.")