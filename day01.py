# Lists
fruits = ["apple", "banana", "mango"]
fruits.append("grape")
print(fruits)
print(fruits[1])

# Dictionaries
user = {"name": "Arjun", "age": 22, "city": "Varanasi"}
print(user["name"])
user["email"] = "arjun@example.com"
print(user)

# Loop over dict
for key, value in user.items():
    print(f"{key}: {value}")

# List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

# Filter with comprehension
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)
