Three-Level Password Authentication System 🔐
📌 Overview

This project implements a multi-factor authentication system with three distinct password levels:

Textual Password → A regular username & password (like standard login).

Graphical Password → Instead of remembering an image, the user remembers a sequence of numbers from a randomized grid of images with serial numbers. Each time the grid is displayed, the numbers are shuffled, providing higher security.

Behavioral Password → The system measures typing behavior (time intervals between keystrokes) to ensure that even if someone knows the password, they must type it in the same rhythm as the original user.

This layered approach enhances security by requiring something the user knows, something the user remembers visually, and something the user does behaviorally.

🛠️ Features

Registration and Login options

Stores hashed textual passwords for security

Randomized graphical password grid on every login attempt

Captures keystroke dynamics for behavioral authentication

Step-by-step verification process:

User enters textual credentials

User provides the correct sequence of numbers from the graphical grid

User must replicate their typing speed (keystroke timing) pattern

🚀 How to Run
1. Clone the Repository
git clone https://github.com/your-username/three-level-password-system.git
cd three-level-password-system

2. Install Dependencies

Make sure you have Python 3.x installed. Install required libraries:

pip install ipywidgets

3. Run in Jupyter Notebook

Open Jupyter Notebook inside VS Code or Anaconda:

jupyter notebook


Open the .ipynb file for the project.

Run all cells.

Use the UI (buttons, input boxes) to Register or Login.

🧩 Example Workflow

Register

Enter a username and textual password.

Choose a graphical sequence by entering the serial numbers displayed on images.

Type your behavioral password so that keystroke timing is recorded.

Login

Enter username and textual password.

Re-enter the graphical sequence (serial numbers may have changed positions).

Type the behavioral password with the same rhythm.

If all checks pass → ✅ Login Successful.

📂 Project Structure
three-level-password-system/
│── three_level_final.py  # Main Jupyter Notebook
│── README.md                    # Project Documentation
│── data/                        # (Optional) Store user data JSON/CSV

🔒 Security Notes

Textual passwords are stored hashed (not plain text).

Graphical password uses randomized sequence mapping each login.

Behavioral data ensures attackers cannot simply steal credentials.

🎯 Future Enhancements

Replace number grid with actual images.

Store user data in a database (SQLite/Postgres) instead of in-memory.

Add more behavioral biometrics (mouse movement, pressure).

Create a Streamlit web app version for deployment.

👨‍💻 Author

Munja Sai Deepak
B.Tech CSE (Data Science) | Data Analyst & Developer
GitHub: saideepak-ui
