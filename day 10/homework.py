academy = input("შემოიტანეთ იმ აკადემის სახელი სადაც ამჟამად სწავლობთ: ")
if academy == "GOA":
    print("მაგარ აკადემიაში სწავლობ!")
else:
    print("ბანძი ხარ")

print(academy)



budget = int(input("please enter your budget: "))
price = int(input("please enter price: "))

if budget >= price:
    print("you have enough money to buy thing")
else:
    print("you need",price - budget)


number = int(input("please enter number: "))

if number >= 5:
    print(number * 2)
else:
    print(number * 4)


ticket_price = 10
ticket_count = int(input("please enter how many ticket do you want to buy: "))
if ticket_count < 5:
    print(ticket_price * ticket_count)
else:
    discount = ticket_price -((30 / 100) * ticket_price)
print(discount * ticket_count)





     