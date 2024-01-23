
#Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as asingle string.
#Reprint this sentence as “The quick brown fox jumps over the lazy dog.” 
#using the replace() function to replace every “!” exclamation mark with a blank space.
#Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” 
#using the upper() function
#Print the sentence in reverse. (Hint: review what you learned about slicing!)

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence)

#Character replaced
spaced_sentence = sentence.replace("!", " ")
print(spaced_sentence)

#Upper case sentence
upper_sentence = spaced_sentence.upper()
print(upper_sentence)

#Reversed upper sentence
reversed_sentence = upper_sentence[::-1]
print(reversed_sentence)
