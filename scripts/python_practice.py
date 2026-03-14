"""
Python Crash Course 3rd Edition Exercises

This script contains the exercises from the book "Python Crash Course 3rd Edition" by Eric Matthes. Each section corresponds to a chapter in the book, and the exercises are implemented as functions. You can run this script to see the results of each exercise.
"""

##############################
# Chapter 1: Getting Started #
##############################

def chapter_1_starting():
    print("Hello, World!")
    print("Hello, Python Crash Course!")
    print("I am Dom Sunga!")
    return

##############################################
# Chapter 2: Variables and Simple Data Types #
##############################################

def chapter_2_variables():
    # Variables
    name = "Dom Sunga"
    print("Hello, " + name + "would you like to learn python today?")
    quote = "To bring about change, you must not be afraid to take the first step. We will fail when we fail to try."
    famous_person = "Rosa Parks"
    print(famous_person + " once said, " + '"' + quote + '"')
    name_student = "\t\n Trent Biop \t\n"
    print(name.lstrip())
    print(name.rstrip())
    print(name.strip())
    
    # Integers
    print(5+3)
    print(4*2)
    print(12-4)
    print(24/3)
    favorite_number = 11
    print ("My favorite number is " + str(favorite_number) + " because of Rukawa.")
    return

################################
# Chapter 3: Introducing Lists #
################################

def chapter_3_lists():
    """
    Basic List
    """
    friends = ["Bob", "Brett", "Brienne", "Bobby"]
    print("I threw " + friends[0].title() + ".")

    transportations = ["car", "motorcycle", "bicycle", "airplane", "boat", "train"]
    print("I would like to ride in a " + transportations[3] + ".")

    """
    Changing, Adding, and Removing Elements
    """

    guests = ["Max Verstappen", "Roger Federer", "Alysa Liu"]
    print(f"Dear Mr./Ms. {guests[2]} it would be an honor to discuss art and flight over dinner.")
    unavailable_guest = guests[0]
    print(f"Our valuable guest Mr./Ms. {unavailable_guest} cannot attend the dinner due to prior commitments.")
    guests[0] = "Elon Musk"

    # Added new guest in front, middle, and end of the list
    guests.insert(0, "Michael Jackson")
    guests.insert(2, "Shohei Ohtani")
    guests.append("Oscar Piastri")

    # 1. Announce the bad news
    print("Change of plans: The new table won't arrive in time, so I can only invite two people.")

    # 2. Use pop() to remove guests until only two remain
    # pop() removes the last item by default and returns it
    popped_guest = guests.pop()
    print(f"Sorry, {popped_guest}, I can't invite you to dinner.")

    popped_guest = guests.pop()
    print(f"Sorry, {popped_guest}, I can't invite you to dinner.")

    popped_guest = guests.pop()
    print(f"Sorry, {popped_guest}, I can't invite you to dinner.")

    popped_guest = guests.pop()
    print(f"Sorry, {popped_guest}, I can't invite you to dinner.")

    # 3. Confirm invitations for the remaining two
    print(f"{guests[0]}, you are still invited!")
    print(f"{guests[1]}, you are still invited!")

    # 4. Use del to empty the list completely
    del guests[0]
    del guests[0]

    # 5. Verify the list is empty
    print(f"Final guest list: {guests}")

    """
    Optimizing a List
    """

    locations = ["Tokyo", "Reykjavik", "Cairo", "Machu Picchu", "Zermatt"]

    # 1. Original order
    print("Original order:", locations)

    # 2. Alphabetical (Temporary)
    print("Alphabetical (sorted):", sorted(locations))

    # 3. Confirm original order is intact
    print("Original order still:", locations)

    # 4. Reverse Alphabetical (Temporary)
    print("Reverse Alphabetical (sorted):", sorted(locations, reverse=True))

    # 5. Confirm original order is STILL intact
    print("Original order still:", locations)

    # 6. Reverse the list (Permanent)
    locations.reverse()
    print("Reversed order:", locations)

    # 7. Reverse again to get back to original (Permanent)
    locations.reverse()
    print("Back to original:", locations)

    # 8. Sort Alphabetically (Permanent)
    locations.sort()
    print("Sorted alphabetically:", locations)

    # 9. Sort Reverse Alphabetically (Permanent)
    locations.sort(reverse=True)
    print("Sorted reverse alphabetical:", locations)

    return

#################################
# Chapter 4: Working with Lists #
#################################

def chapter_4_loops():
    """
    Looping Through an entire list
    """
    animals = ["Dog", "Cat", "Rabbit"]

    # Use a descriptive variable name like 'animal'
    for animal in animals:
        print(f"A {animal.lower()} would make a great pet.")

    print("\nAny of these animals would make a great pet!")

    """
    Numerical Lists
    """
    # 4-3: Counting to Twenty
    for number in range(1, 21):
        print(number)

    # 4-4: This would take a while to print, skipping the print
    numbers = list(range(1, 1000001))
    # for num in numbers: print(num) 

    # 4-5: Stats on a million numbers
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Sum: {sum(numbers)}")

    # 4-6: Odd numbers (start at 1, skip by 2)
    odds = list(range(1, 21, 2))
    for odd in odds:
        print(odd)

    # 4-7: Multiples of 3
    threes = list(range(3, 31, 3))
    for three in threes:
        print(three)
    
    # 4-8: Standard Loop
    cubes = []
    for value in range(1, 11):
        cube = value**3
        cubes.append(cube)

    # 4-9: List Comprehension
    for cube in cubes:
        print(cube)
    # The logic is: [expression for item in list]
    cubes = [value**3 for value in range(1, 11)]
    print(cubes)

    # 4-10: Slices
    # A list of places to travel
    travel_goals = ["Tokyo", "Reykjavik", "Cairo", "Lima", "Zermatt", "Paris", "Seoul"]

    # First three items (starts at 0, stops before 3)
    print(f"The first three items in the list are: {travel_goals[:3]}")

    # Three items from the middle
    # We'll start at index 2 and stop before 5
    print(f"Three items from the middle of the list are: {travel_goals[2:5]}")

    # The last three items (using negative indexing)
    print(f"The last three items in the list are: {travel_goals[-3:]}")

    # 4-11: My Pizza, Your Pizza
    my_pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]

    # Correct way to copy: use [:]
    friend_pizzas = my_pizzas[:]

    # Add different pizzas to each list
    my_pizzas.append("Meat Lovers")
    friend_pizzas.append("Hawaiian")

    # Prove they are separate
    print("My favorite pizzas are:")
    for pizza in my_pizzas:
        print(f"- {pizza}")

    print("\nMy friend's favorite pizzas are:")
    for pizza in friend_pizzas:
        print(f"- {pizza}")

    # 4-12: More Loops
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]

    my_foods.append('cannoli')
    friend_foods.append('ice cream')

    print("My favorite foods are:")
    for food in my_foods:
        print(food)

    print("\nMy friend's favorite foods are:")
    for food in friend_foods:
        print(food)

    # 4-13: Buffet
    # 1. Store five simple foods in a tuple
    buffet_foods = ("Pasta", "Salad", "Steak", "Soup", "Bread")

    # 2. Use a for loop to print the original menu
    print("Original Menu:")
    for food in buffet_foods:
        print(f"- {food}")

    # 3. Try to modify an item (uncomment the line below to see the error)
    # buffet_foods[0] = "Pizza"  

    # 4. Rewrite the tuple to change the menu
    # We redefine the entire variable to "change" it
    buffet_foods = ("Pizza", "Salad", "Steak", "Fruit", "Bread")

    # 5. Print the revised menu
    print("\nRevised Menu:")
    for food in buffet_foods:
        print(f"- {food}")

############################
# Chapter 5: IF Statements #
############################

def chapter_5_if_statements():
    # --- 5-1: Basic Conditional Tests ---

    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    food = 'pizza'
    print("\nIs food == 'pizza'? I predict True.")
    print(food == 'pizza')

    print("\nIs food == 'broccoli'? I predict False.")
    print(food == 'broccoli')

    age = 25
    print("\nIs age == 25? I predict True.")
    print(age == 25)

    # --- 5-2: More Advanced Tests ---

    # 1. Tests for equality and inequality with strings
    language = 'Python'
    print("\nIs language == 'Python'? I predict True.")
    print(language == 'Python')

    print("Is language != 'Java'? I predict True.")
    print(language != 'Java')

    # 2. Tests using the lower() method
    name = 'Eric'
    print("\nIs name.lower() == 'eric'? I predict True.")
    print(name.lower() == 'eric')

    print("Is name == 'eric'? I predict False (Case sensitivity matters!).")
    print(name == 'eric')

    # --- 5-5: Alien Color Test ---

    alien_color = 'red'

    if alien_color == 'green':
        print("You just earned 5 points!")
    elif alien_color == 'yellow':
        print("You just earned 10 points!")
    else:
        print("You just earned 15 points!")

    # --- 5-6: Stages of Life Test ---

    age = 21

    if age < 2:
        print("You're a baby!")
    elif age < 4:
        print("You're a toddler!")
    elif age < 13:
        print("You're a kid!")
    elif age < 20:
        print("You're a teenager!")
    elif age < 65:
        print("You're an adult!")
    else:
        print("You're an elder!")

    # --- 5-7: Favorite Fruit Test ---

    favorite_fruits = ["orange", "banana", "blueberries"]

    if "orange" in favorite_fruits():
        print("You really like orange!")
    if "banana" in favorite_fruits():
        print("You really like banana!")
    if "pineapple" in favorite_fruits():
        print("You really like pineapple!")
    if "grapes" in favorite_fruits():
        print("You really like grapes!")
    if "blueberries" in favorite_fruits():
        print("You really like blueberries!")

    # --- 5-10: Favorite Fruit Test ---

    current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
    new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

    current_users_lower = [user.lower() for user in current_users]

    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"Sorry {new_user}, that name is taken.")
        else:
            print(f"Great, {new_user} is still available.")
    return

# chapter_1_starting()
# chapter_2_variables()
# chapter_3_lists()
# chapter_4_loops()
# chapter_5_if_statements()