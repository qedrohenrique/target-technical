string = "Hello World!"
reversed_string = ""
for i in range(1,len(string)+1):
    reversed_string += string[-i]
print(string)
print(reversed_string)