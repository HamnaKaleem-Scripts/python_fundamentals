# File Handling in Python

# Write to a file
with open("demo.txt", "w") as file:
    file.write("Hello, file!\nThis is a second line.")

# Read from a file
with open("demo.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
