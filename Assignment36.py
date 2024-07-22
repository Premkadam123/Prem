#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

try:
    with open("D:\\Demo\\abc.txt", 'r') as file:
        total_words = 0
        for line in file:
            words = line.split()
            total_words += len(words)
            print(f"Total number of words: {total_words}")
except FileNotFoundError:
     print(f"The file abc.txt does not exist.")


#output:
#The file abc.txt does not exist.
#Total number of words: 9 #one line words counts
#Total number of words: 16