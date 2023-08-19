import secrets
import string

def main():
   #required length of password defined by user
   req_length = int(input("How long do you want your password to be? "))

   letters = string.ascii_letters #upper and lower case letters
   digits = string.digits #digits from 0-9
   special_characters = string.punctuation #special characters

   #concatenate the above string constants
   alphabet = letters + digits + special_characters

   pwd = ''
   for i in range (req_length):
      pwd +=''.join(secrets.choice(alphabet))

   print(pwd)

main()



'''
1. Start the program.
2. Ask the user how long they want their password to be.
3. Read the user's input for the desired length of the password.
4. Generate a password string that is of the specified length, by:
   a. Creating an empty string variable to hold the password.
   b. Using a loop to generate random characters until the desired length is reached.
   c. For each iteration of the loop, generate a random character (using the random module) and append it to the password string.
5. Print the generated password to the console.
6. End the program.
'''