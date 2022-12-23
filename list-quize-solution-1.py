list1 = ["M", "na", 4, "i", 5, "Ke", 1, 8, "y", "me", 2, 6, "s", 0, "lly", 9]
for item in list1:
    if str(item).isnumeric() and item < 5:
        print(item)

