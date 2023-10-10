# My Wordle Helper
 
<!-- TABLE OF CONTENTS -->
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#tools-and-versions">Tools and Versions</a></li>
        <li><a href="#word-lists">Word Lists</a></li>
        <li><a href="#code-files">Code Files</a></li>
      </ul>
    </li>
    <li><a href="#how-to-run">How to Run</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>



<!-- ABOUT THE PROJECT -->
## About the Project
This Python program is a Wordle solver that outputs a list of possible words for each try based on your input and the Wordle response. For each try, you provide a word and receive feedback in the form of "g" (green, for a correct letter in the correct position), "y" (yellow, for a correct letter in the wrong position), or "w" (white/grey, for an incorrect letter). The code helps you narrow down the possible words that match the given feedback.

### Tools and Versions
- python/3.11.4

### Word Lists
* **All Answers List**: This list contains 2309 possible answers to NYT's implementation of the Wordle game. You can find this list [here](https://gist.github.com/cfreshman/a7b776506c73284511034e63af1017ee).
* **Valid Guesses List**: This list contains allowed guesses, which may include plurals and rare words. It's important to note that this list excludes the possible answers to the NYT's Wordle. You can find this list [here](https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c).

### Code Files
* wordle_functions.py: This file contains the core functions used to play the Wordle game. It includes the following functions:
    1. input_word(valid_guesses, all_answers): Gets user input for a five-letter word, validates it against the valid_guesses and all_answers lists, and returns the input word.
    2. wordle_output(): Gets user input for Wordle output (using "g" for green, "y" for yellow, and "w" for white/grey), validates it, and returns the Wordle response.
    3. filter_possible_words(word, response, candidate_words): Filters the possible words based on the user's input word and Wordle response, returning a list of candidate words.
* wordle_solver.py: This is the main script that orchestrates the Wordle game. It uses the functions from wordle_functions.py to interact with the user, manage the game flow, and display the possible word lists for each attempt.

## How to Run
1. Clone the repository with Python installed
2. Run the code by executing: python wordle_solver.py
3. Follow the on-screen prompts to input your guesses and Wordle feedback.
4. The code will provide you with a list of possible words for each try, helping you solve the Wordle puzzle within the six allowed attempts.

## Acknowledgments
The word lists are from [Cyrus Freshman](https://gist.github.com/cfreshman) on GitHub Gist, see links in the word list section above. 

Shout out to my roommates for test-running the program in actual gameplay and providing feedback!