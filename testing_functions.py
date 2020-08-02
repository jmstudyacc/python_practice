header_string = "Our special is " 

def create_special_string(special_item):
  return header_string + special_item + "."
print(create_special_string(input("What is the special today?: ")))
