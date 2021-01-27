def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, thats enough for a party.")
    print("Get a blanket. \n")


print("We can just give the function numbers derectly:")
cheese_and_crackers(20, 33)


print("OR, we could use varibles from our script.")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, varibles and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)