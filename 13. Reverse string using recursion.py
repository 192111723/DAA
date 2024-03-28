def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reverse of the string:", reversed_string)