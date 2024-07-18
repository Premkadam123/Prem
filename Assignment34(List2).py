# Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 
# Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red

def traverse_list_reverse(original_list):
    for index in range(len(original_list)-1, -1, -1):
        print(f"Original index: {index}, Element: {original_list[index]}")

# Example usage
colors = ['red', 'green', 'white', 'black']
print("Traverse the list in reverse order with original indices:")
traverse_list_reverse(colors)


     #  Output : 
     #  Traverse the list in reverse order with original indices:
     #        Original index: 3, Element: black
     #        Original index: 2, Element: white
     #        Original index: 1, Element: green
     #        Original index: 0, Element: red  

