# file_handling.py
# Writing and reading files

# Writing to a file
file = open("data.txt", "w")
file.write("This is a sample file.\n")
file.write("Learning file handling in Python.")
file.close()

# Reading from a file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
