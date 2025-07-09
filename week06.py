def load_to_list(filepath: str) -> list[float]:
   # Reads temperature values from the file and returns them as a list of floats
    temperatures = [] # Create empty list to store float values
    with open(filepath, 'r') as file:
        for line in file:
            stripped = line.strip() # Remove whitespace
            if stripped != '': # Skip blank lines
                temperatures.append(float(stripped)) # Convert and store
    return temperatures # Return list of temperature values as float



def descriptive_statistics(source_data: list[float]) -> None:
    # Prints summary stats for a list of temperatures
    total_count = len(source_data)
    total_sum = sum(source_data)
    average = round(total_sum / total_count, 3)
    minimum = min(source_data)
    maximum = max(source_data)

    # Display the results
    print(f"There are {total_count} values in the data source.")
    print(f"The average value is {average}")
    print(f"The highest value is {maximum} and the smallest value is {minimum}.")



def apply_markup(filepath: str) -> None:
    with open(filepath, 'r') as file:
        for line in file:
            words = line.strip().split() # Split line into individual words
            formatted_line = "" # To store the final version of the processed line

            for word in words:
                if word.startswith('.'): # Uppercase formatting
                    formatted_word = word[1:].upper()
                elif word.startswith('_'): # Expanded with spaces
                    expanded = ' '.join(list(word[1:])) # Split into letters with space
                    formatted_word = expanded
                else:
                    formatted_word = word # No formatting
                
                if formatted_line == "": # Add space if it's not the first word
                    formatted_line = formatted_word
                else:
                    formatted_line += " " + formatted_word
            
            print(formatted_line) # Output the processed line


    
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

