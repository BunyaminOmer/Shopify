# 1. print

price = 200
tax = price * 0.18
price_width_tax = price + tax

print("*" * 10, "SONUÇ : ", "*" * 10, sep="---", end=':::::::::::::::')
print(price_width_tax)

# 2. help
# help(print)

# 3. type
age = 10
is_active = False
user_name = "user"

print(type(age), type(is_active), type(user_name))
print(type(age) == int)
print(type(is_active) == bool)

# 4. len

print(len(user_name))
print(len(str(age)))

# 5. dir

print(dir(user_name))
print(dir(str))