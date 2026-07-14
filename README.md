#  Python Password Generator

A simple Python program that generates strong random passwords based on the length entered by the user.

##  Features

- Generates random passwords of any length
- Includes:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- Allows users to generate multiple passwords without restarting the program
- Handles invalid input using exception handling (`try-except`)

##  Technologies Used

- Python 3
- `random` module
- PyCharm 

##  How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Vigneswaran-SL/password-generator.git
   ```

2. Navigate to the project folder:
   ```bash
   cd password-generator
   ```

3. Run the program:
   ```bash
   python password_generator.py
   ```

##  Example Output

```
Enter the length of the password: 12
xA7#pL9@qT2!

Do you want to enter another password? (y/n): y

Enter the length of the password: 8
M$8zQ2@a

Do you want to enter another password? (y/n): n
Thank you for using Password Generator!
```

##  What I Learned

- Using Python's `random` module
- Working with strings and loops
- Handling user input with `try-except`
- Building interactive console applications
- Generating random data

##  Future Improvements

- Ensure at least one uppercase, one lowercase, one number, and one special character in every password
- Allow users to choose which character types to include
- Add password strength indicator
- Copy generated password to clipboard
- Save generated passwords to a file


 If you found this project helpful, consider giving it a star!
