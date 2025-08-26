import random
import time
import hashlib

# ===============================
# Utility Functions
# ===============================
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

# ===============================
# Database (in-memory for demo)
# ===============================
user_db = {}

# ===============================
# Registration
# ===============================
def register_user():
    print("\n=== User Registration ===")
    username = input("Enter username: ")
    
    if username in user_db:
        print("Username already exists! Try login.")
        return

    # 1. Textual Password
    password = input("Set textual password: ")
    hashed_password = hash_text(password)

    # 2. Graphical Password
    images = ["🍎", "🍌", "🍇", "🍓", "🍍", "🍊", "🥭", "🍉"]
    print("\nSelect 3 images as your graphical password:")
    for i, img in enumerate(images, 1):
        print(f"{i}. {img}")
    choices = input("Enter 3 numbers separated by spaces: ").split()
    chosen_images = [images[int(c) - 1] for c in choices]

    # 3. Behavioral (Typing Speed)
    print("\nBehavioral Password Setup")
    input("Type the word 'secure' and press Enter to record speed: ")
    start = time.time()
    typed = input("Now type 'secure' again: ")
    end = time.time()
    if typed != "secure":
        print("Behavioral setup failed. Try again.")
        return
    typing_speed = end - start

    # Store user
    user_db[username] = {
        "password": hashed_password,
        "graphical": chosen_images,
        "behavior": typing_speed
    }
    print("✅ Registration successful!")

# ===============================
# Login
# ===============================
def login_user():
    print("\n=== User Login ===")
    username = input("Enter username: ")
    
    if username not in user_db:
        print("User not found. Please register first.")
        return
    
    user = user_db[username]

    # 1. Textual Check
    password = input("Enter textual password: ")
    if hash_text(password) != user["password"]:
        print("❌ Wrong textual password!")
        return
    
    # 2. Graphical Check with shuffled images
    images = ["🍎", "🍌", "🍇", "🍓", "🍍", "🍊", "🥭", "🍉"]
    random.shuffle(images)
    print("\nGraphical Authentication - Select your chosen images")
    for i, img in enumerate(images, 1):
        print(f"{i}. {img}")

    choices = input("Enter 3 numbers separated by spaces: ").split()
    chosen_now = [images[int(c) - 1] for c in choices]

    if chosen_now != user["graphical"]:
        print("❌ Graphical authentication failed!")
        return
    
    # 3. Behavioral Check
    print("\nBehavioral Authentication")
    input("Type the word 'secure' and press Enter to test speed: ")
    start = time.time()
    typed = input("Now type 'secure' again: ")
    end = time.time()
    if typed != "secure":
        print("❌ Wrong word typed!")
        return
    
    test_speed = end - start
    if abs(test_speed - user["behavior"]) > 1.5:
        print("❌ Behavioral check failed! Typing speed mismatch.")
        return

    print(f"✅ Welcome back, {username}! Login successful.")

# ===============================
# Main Menu
# ===============================
def main():
    while True:
        print("\n=== Three-Level Password System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

# Run
if __name__ == "__main__":
    main()
