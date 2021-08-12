import random

# Empty list
random_list = []

# Roll dice and try again function
def try_again(random_list):
    '''Roll the dice, and get random numbers which are save in the list.'''

    # Get random numbers from the range 1 to 6
    six_side_dice = random.randint(1, 6)
    # Add get items in the list
    random_list.append(six_side_dice)
    # Show the number
        # f-string
    print(f"Six side dice number: {six_side_dice}")

    # Loop
    while True:

        # Try again option
        user_confirmation = input("Do you want roll the dice again? [Y/N]> ")

        # Conditions
           # .lower() -> Transform all characters in lowercase
        if user_confirmation.lower() == "y":
            print("\n")
            # Run the function again
            try_again(random_list)
            return

        elif user_confirmation.lower() == "n":
            #for i in random_list:
            # Get showed numbers
            print(f"Showed numbers: {random_list}")
            # Finish function
            return
            
        else:
            print("Invalid input, you must use Y (y) or N (n), please try again.\n")
            # Continue until the user write valid input
            continue

try_again(random_list)