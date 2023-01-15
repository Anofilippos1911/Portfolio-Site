"""
TM112 21D TMA03 Q2 starter code
TM112 Module Team 17/12/2020
"""

from random import *


def show_flashcard():
    """ This flashcard program will bring up a random entry from the glossary
along with two definitions, one that is the correct one and one that is the
incorrect one in random order each time for that particular entry after the
user requested it. Then the user will either press 1 or 2 according to which
definition they consider to be the correct, in accordance with the order the
program randomly shown the 2 definitions. The program then will inform the user
whether they got the answer correct or wrong.
"""

    # Get glossary keys.
    keys = list(glossary)

    # Choose two random glossary keys.
    random_key1 = choice(keys)
    random_key2 = choice(keys)
    # Keep checking random_key2 until
    # it is different from random_key1
    while random_key2 == random_key1:
      random_key2 = choice(keys)  

    # Display random glossary key.
    print('Here is a glossary entry:', random_key1)

    # Choose a random order to display the definitions in
    # '1' means the correct definition
    #  should be printed first.
    #
    # '2' means the correct definition
    # should printed second.
    #
    correct_def = choice(['1', '2'])

    # INSERT YOUR CODE IMMEDIATELY BELOW.
    #print('Here are two possible definitions:')
    #print('1.', glossary[random_key1])
    #print('2.', glossary[random_key2]) 
    # INSERT YOUR CODE IMMEDIATELY BELOW. 
    print('Here are two possible definitions:')
    if correct_def == 1:
        print('1.', glossary[random_key1])
        print('2.', glossary[random_key2]) 
    else: #correct_def == 2:
        print('1.', glossary[random_key2]) 
        print('2.', glossary[random_key1]) 
    #print('1.', glossary[random_key1]) 

    #print('2.', glossary[random_key2]) 

    print(correct_def)

    # The user input for the correct answer 

    user_input = input('Which definition is correct? Enter either 1 or 2:') 
    #print(glossary[random_key1])
    #print(glossary[random_key2])
    #print(random_key1)
    #print(random_key2)
    #print(user_input)
    if user_input and correct_def == 1:
        print('correct(1)!!!')
    elif user_input and correct_def == 2:
        print('correct(2)!!!')
    elif user_input != correct_def:
        print('mikri poullou')
    else:
        print('incorrect')





# DO NOT CHANGE ANYTHING IN THE NEXT SECTION    

# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
                       
