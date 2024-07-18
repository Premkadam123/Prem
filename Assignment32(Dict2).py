#Write a Python program to get the key, value and item in a dictionary. 
#input: dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
# Define the dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Print the keys, values, and items
print("Keys:")
for key in dict_num.keys():
    print(key)

print("\nValues:")
for value in dict_num.values():
    print(value)

print("\nItems:")
for item in dict_num.items():
    print(item)
    
    
# Output : 
      
    # Keys:  1,2,3,4,5,6
          
    # Values: 10,20,30,40,50,60                     
          
    # Items :  (1, 10),(2, 20),(3, 30),(4, 40),(5, 50),(6, 60)
                         