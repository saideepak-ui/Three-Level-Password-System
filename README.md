<a href="https://colab.research.google.com/drive/1mjvsd9QNfxzWiTZ-k0Oj0ZjRC7-Z76X1?usp=sharing" target="_blank">Three-Level Password System

## Description
The Three-Level Password System is designed to provide a high level of security through a multi-factor authentication process. This system leverages three distinct authentication methods—textual, graphical, and behavioral—to ensure that only legitimate users gain access. It is user-friendly and offers a console-based interface, making it easy to maintain and resistant to bot attacks or hacking attempts.

## Key Features
- **Textual Authentication:** Users are required to enter a secure textual password.
- **Graphical Authentication:** Users must select images in the correct sequence.
- **Behavioral Authentication:** Users must type a specific phrase accurately and within a set time limit.
- **Multi-Factor Security:** Combines different types of authentication to maximize security.
- **No External Dependencies:** Operates entirely within a console, requiring no database or frontend.

## Process Flow
1. **Textual Authentication:** The user enters a password. If correct, they proceed to the next level.
2. **Graphical Authentication:** The user selects images in the correct order. Success leads to the final level.
3. **Behavioral Authentication:** The user types a phrase. If all levels are passed, access is granted.

## Technologies Used
- **Python:** Handles the entire authentication process, including hashing and timing.
- **Hashlib:** Provides secure hashing for textual passwords.
- **Random:** Shuffles the images for graphical authentication.
- **Time:** Measures typing speed for behavioral authentication.


