print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10
print(f"Hello {name}, you are {age} years old.")

if age >= 18:
    print("You are old enough to play!")
    decision = input("Do you wants to play? type: yes or no:  ").lower()

    if decision == "yes":
        print(f"You are starting with {health} health")
        print("Let's play!")
        left_or_right = input("First choise.... Left or Right? (left/right)?").lower()
        if left_or_right == "left":
            ans = input("Nice, you followed a path and reached a lake... Do you swim across or go around("
                        "across/around)? ").lower()
            if ans == "across":
                print("You managed to get across, but were bit by fish and lost 5 health.")
                health -= 5
                print(f"You have {health} health left")
            elif ans == "around":
                print("You went around and reached the other side of the lake")

            ans = input("You notice a house and a river. Which do you go to(river/house)? ").lower()

            if ans == "house":
                print("You go to the house and are greeted by the owner... "
                      "He doesn't like you and you lost 5 health")
                health -= 5
                print(f"You have {health} health left...")
            else:
                print("You fell in the river and lost...")

        else:
            print("You fell down and lost!!")
    else:
        print(f"OPPS... Bye {name}.")
else:
    print("You are not old enough to play...")