#Ask the user to enter a sentence using the input() method. Save the user’s
#response in a variable called str_manip.
#● Using this string value, write the code to do the following:
#	○ Calculate and display the length of str_manip.
#	○ Find the last letter in str_manip sentence. Replace every occurrence
#	  of this letter in str_manip with ‘@’.
#		■ e.g. if str_manip = “This is a bunch of words”, the output would
#		be: “Thi@ i@ a bunch of word@”
#	○ Print the last 3 characters in str_manip backwards.
#		■ e.g. if str_manip = “This is a bunch of words”, the output would
#		be: “sdr”.
#	○ Create a five-letter word that is made up of the first three characters
#	  and the last two characters in str_manip.
#		■ e.g. if str_manip = “This is a bunch of words”, the output
#		would be: “Thids”.

#Ask user for input
str_manip = input("Enter your sentence: ")

#Lenght of sentence
length_of_str = len(str_manip)
print(f"Lenght of sentence: {len(str_manip)}")

#Last letter replaced
last_letter = str_manip[-1]
replaced_str_manip = str_manip.replace(last_letter, '@')
print(f"Last letter replaced: {replaced_str_manip}")

#Last three letters reversed
last_three_letters = str_manip[-3:][::-1]
print(f"Last three letter reversed: {last_three_letters}")

#Five-letters word
#print(str_manip[0] + str_manip[1] + str_manip[2] + str_manip[-2] + str_manip[-1])
print(f"Five-letter word: {str_manip[:3]}{str_manip[-2:]}")