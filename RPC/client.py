


import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

number = int(input("Enter an integer to compute factorial for: "))

result = server.compute_factorial(number)

print(f"The factorial of {number} is {result}")