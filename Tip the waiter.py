def tipCalc(b, tipPerc):
    total = b * 0.01 * tipPerc
    return total

bill = int(input("Enter Your Bill: "))
tipPercentage = int(input("Enter Your Tip Percentage: "))

res = tipCalc(bill, tipPercentage)
print(f"Bill: {bill}")
print(f"Tip: {tipPercentage}%")
print(f"Total: {bill + res}")

