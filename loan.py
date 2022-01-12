money_owed = float(input("How much do you owe, in dollars?\n")) #50,000
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be, in dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

#Divid apr by 100 to make it a percent, then divid by 12 to make it monthly
monthly_rate = apr/100/12
for i in range(months):
    #Add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    #Make Payment
    money_owed = money_owed - payment

    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
    #print results
    print("Paid", payment, "of which", interest_paid, "was interest", end= ' ')
    print("Now I owe", money_owed)