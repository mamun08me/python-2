words = [
    "variable",
    "argument",
    "parameter",
    "syntax",
    "indent",
    "loop",
    "module",
    "string",
    "boolean",
    "exception"
]

search_word=input("Enter a word to search: ")

word_found=False
for word in words:
    if word==search_word:
        word_found=True
      
if word_found:
    print(f" found the word: {search_word}") 
else:
    print("Word is not found")
