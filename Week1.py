print("Hello World!")

print("wWhat is your name?")

name = input()


print("Hello", name)

#3 Welcome to <city>, from file
cityname = open("cityname.txt", "r")

file = cityname.readline()
#actually read a line

print(f"Welcome to {file}!")

