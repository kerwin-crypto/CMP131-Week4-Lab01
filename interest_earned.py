princ= int(input("The principal balance of the savings account: "))
interest= float(input("What is the interest rate?: "))
comp= int(input("How many times is the interest compounded?: "))
print(f"Interest Rate: {interest}%")
print("Times Compounded: ", comp)
print("Principal: $",princ)

interest=interest/100
amount= princ*(1+interest/comp)**comp
sint= amount-princ
print(f"Interest: ${sint:.2f}")
print(f"Amount In Savings: ${amount:.2f}")