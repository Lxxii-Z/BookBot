#Write a new function that accepts the text from the book as a string, 
#and returns the number of words in the string. The .split() method will be helpful here.
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters = {}
    for letter in text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sorted_data(dict):
    #List of dictionaries
    letters = []
    for char, count in dict.items():
        letters.append({"char": char, "num": count})
    
    #Sort by count
    def sort_on(dict):
        return dict["num"]
    
    letters.sort(reverse=True, key=sort_on)
    return letters
