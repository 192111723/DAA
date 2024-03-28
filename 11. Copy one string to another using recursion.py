def copy_string(source, destination, index=0):
    if index == len(source):
        return destination
    else:
        destination += source[index]
        return copy_string(source, destination, index + 1)
source_string = input("Enter the source string: ")
destination_string = ""
destination_string = copy_string(source_string, destination_string)
print("Source string:", source_string)
print("Destination string:", destination_string)