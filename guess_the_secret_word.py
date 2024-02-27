#Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
word = input("Write a word to leave the loop: ")
while word.lower() != 'chupacabra':
    word = input("Let's try again: ")
print("You've successfully left the loop")
