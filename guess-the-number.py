max_attempt = 0
item = 55
while max_attempt < 10:
    print(f"You have {10-max_attempt} attempt left.")
    num = int(input("Guess the number: "))
    if num < item:
        print("The number you guess is small.")
    elif num > item:
        print("The number you guess is large.")
    elif num == item:
        print("Victory!!")
        break
    max_attempt = max_attempt + 1




