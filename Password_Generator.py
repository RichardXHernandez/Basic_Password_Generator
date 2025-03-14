import random 
import string

asc_char = string.ascii_letters # variable for easier use of the static ascii string
digits = string.digits # variable for the easier use of static digit string
punctuation =  string.punctuation # variable for the easier use of static punctuation string




while True: 
    asc_char_list = [] # list of ascii characters that will be added to the password. 
    
    digits_list = [] # list of numbers/digits that will be added to the password. 
    
    punctuation_list = [] # list of punctuation marks/characters that will be added to the password. 

    # All are appended in the for loop after each question of how many of each you want. 
    
    print("-" * 40) #just to draw a line

    code_works = input("\nWelcome to the password generator, would you like to use this program? Enter y/n:\n").lower() # beginning input that dictates if you want to use the program or to exit
    if code_works == 'y': #first if statement argument that checks if the user entered a y to begin
        
        num_of_ascii = int(input("\nHow many letters would you like? Please enter a number\n")) #input variable that takes the integer for the range of ascii characters the user wants
        for x in range(num_of_ascii):
            ascii_characters = random.choice(asc_char) # Uses random to select ascii characters from the static variable asc_char
            asc_char_list.append(ascii_characters) # appends the random selected ascii character to the list 

        num_of_digits = int(input("\nHow many numbers would you like? Please enter a number\n")) # input for number of digits/numbers wanted by user. 
        
        for y in range(num_of_digits):
            digits_selected = random.choice(digits) # selects random numbers from static string of numbers. 
            digits_list.append(digits_selected) # appends list of digits/numbers wanted with the randomly selected numbers
        
        num_of_punctuation = int(input("\nHow many punctuation marks would you like? Please enter a number\n")) # Input for number of punctuation marks the user wants. 
        
        for z in range(num_of_punctuation):
            punctuation_chars = random.choice(punctuation) #random choice from list of punctuation marks
            punctuation_list.append(punctuation_chars) #appends the punctuation list with the randomly selected punctuation marks
        
        password = ''.join(asc_char_list + digits_list + punctuation_list) # joins the lists of each variable. 
        print(password) #prints the password variable
            
    elif code_works == 'n': # if user input is n then the program closes. 
        exit()
    else: # else statement to keep the while loop from breaking. 
        print("\n that is not an option. Please try again.\n") 