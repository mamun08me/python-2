words = [
    "variable",
    "argument",
    "parameter",
    "syntax",
    "syntax",
    "syntax",
    "indent",
    "loop",
    "loop",
    "module",
    "string",
    "boolean",
    "exception"
]

search_word=input("Enter a word to search: ")
word_found=False
frequency=0
for word in words:
    if word==search_word:
        word_found= True
        frequency+=1
    
if word_found:
    print(f" found the word:{search_word}, {frequency} times repeated") 
else:
    print("Word is not found")