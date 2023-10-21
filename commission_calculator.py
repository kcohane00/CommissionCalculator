name = input("What is your name: ")
sales = input("What were your monthly sales (Don't include the $): ")
sales = float(sales)

commission = round(sales * 13/100, 2)

print(f"Congratulations, {name}! Your commission for this month are ${commission}.")

