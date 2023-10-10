# Import wordle_functions containing functions input_word, wordle_output, and filter_possible_words
import wordle_functions

# possible NYT wordle answers 
# https://gist.github.com/cfreshman/a7b776506c73284511034e63af1017ee
answers_file = open('all_answers.txt', 'r')
lines = answers_file.readlines()
all_answers = [line.strip() for line in lines]

# allowed guesses (include plurals and rare words, EXCLUDE possible answers)
# https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c
guesses_file = open('valid_guesses.txt', 'r')
lines = guesses_file.readlines()
valid_guesses = [line.strip() for line in lines]

# Function to run wordle helper
def run_wordle(valid_guesses, all_answers):
    max_tries = 6
    num_tries = 0
    filtered_words = all_answers

    while num_tries < max_tries:
        print(f"\nAttempt {num_tries+1} of {max_tries}")
        
        # Get the user's input
        user_word = wordle_functions.input_word(valid_guesses, all_answers)

        if user_word is not None:
            # Get the Wordle response
            wordle_response = wordle_functions.wordle_output()
            # Filter words
            filtered_words = wordle_functions.filter_possible_words(user_word, wordle_response, filtered_words)

            if filtered_words:
                if len(filtered_words) == 1:
                    print("you found it! The word is:", filtered_words[0])
                    return
                print("Number of possible word(s):", len(filtered_words))
                print(", ".join(filtered_words))
            else:
                print("No matching words found")
                return
        else:
            print("User chose to skip")
            return

        num_tries += 1

    # Allows for 6 tries
    if num_tries == max_tries:
        print("You've reached the maximum number of tries")

run_wordle(valid_guesses, all_answers)