# def add(num1, num2):
#     return num1 + num2
#
#
# addition = lambda num1, num2: num1 + num2
#
# print(add(2, 2))
# print(addition(2, 2))

savings = [234.00, 555.00, 674.00, 78.00]

# bonus = list(map(lambda x: x * 1.1, savings))

bonus = []

for account_balance in savings:
    bonus.append(account_balance * 1.1)

print(bonus)