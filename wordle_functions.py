# Function to get user input for a five-letter word
def input_word(valid_guesses, all_answers):
    while True:
        response = input("Input a five letter word: ")
        word = response.lower().strip()

        # Return None if the user presses Enter
        if response == "":
            return None
        
        # Check if user input is a valid word
        elif word in valid_guesses or word in all_answers:
            print("You entered:", word)
            return word
        else: 
            print("Invalid word:", word)


# Function to get user input for wordle output
def wordle_output():
    while True:
        # g = green (letter is in the correct position)
        # y = yellow (letter is in the word, but not in the correct position) 
        # w = white/grey (letter is not in the word)
        colors = ['g', 'y', 'w']
        response = input("Input five letters corresponding to wordle's output \ng for green, y for yellow, w for white/grey: ")
        output = response.lower()

        # Return None if the user presses Enter
        if response == "":
            return None
        
        # Check if user input is a valid wordle output
        if len(output) == 5 and all(i in colors for i in output):
            print("wordle output:", response)
            return output
        else: 
            print("invalid wordle output:", response)

# Function to filter possible words based on user input and Wordle output
def filter_possible_words(word, response, candidate_words):
    if word is None or response is None:
        return None
    
    filtered_words = []
    for candidate in candidate_words:
        valid = True
        
        # check each letter
        for i in range(5):
            if response[i] == 'g':
                if word[i] != candidate[i]:
                    valid = False
            elif response[i] == 'y':
                if (word[i] not in candidate) or (word[i] == candidate[i]):
                    valid = False
            else: # response[i] == 'w'
                if word[i] in candidate:
                    valid = False
        if valid:
            filtered_words.append(candidate)
    
    return filtered_words