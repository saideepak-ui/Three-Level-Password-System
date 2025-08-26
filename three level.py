import hashlib
import random
import time

# ===== Utility Functions =====
def hash_text(text):
    """Return SHA256 hash of a given text."""
    return hashlib.sha256(text.encode()).hexdigest()

# ===== User Database (in-memory for demo) =====
users = {}

# ===== Registration =====
def register():
    username = input("Enter a username: ").strip()
    if username in users:
        print("❌ Username already exists! Try logging in.")
        return

    # 1. Textual password
    password = input("Enter a textual password: ").strip()
    password_hash = hash_text(password)

    # 2. Graphical password (numbers instead of emojis)
    print("\nChoose your graphical password by selecting 3 numbers from 1 to 9.")
    print("Grid:\n1 2 3\n4 5 6\n7 8 9")
    graphical = input("Enter 3 numbers (space-separated): ").strip().split()
    while len(graphical) != 3 or not all(num in '123456789' for num in graphical):
        print("⚠️ Invalid input. Enter exactly 3 numbers between 1-9.")
        graphical = input("Enter 3 numbers (space-separated): ").strip().split()
    graphical_hash = hash_text(" ".join(graphical))

    # 3. Behavioral password (reaction time)
    print("\nBehavioral Password Test: Press Enter as quickly as possible after 'GO!'")
    input("Press Enter to start...")
    time.sleep(random.randint(2, 5))
    print("GO!")
    start = time.time()
    input()
    reaction_time = round(time.time() - start, 2)
    print(f"Your reaction time recorded: {reaction_time} sec")

    users[username] = {
        "password": password_hash,
        "graphical": graphical_hash,
        "behavioral": reaction_time
    }
    print(f"\n✅ User '{username}' registered successfully!\n")


# ===== Login =====
def login():
    username = input("Enter username: ").strip()
    if username not in users:
        print("❌ Username not found!")
        return

    # 1. Textual password
    password = input("Enter textual password: ").strip()
    if users[username]["password"] != hash_text(password):
        print("❌ Incorrect textual password!")
        return

    # 2. Graphical password
    print("\nRe-enter your graphical password numbers (e.g., 1 5 9)")
    graphical = input("Enter numbers: ").strip().split()
    if users[username]["graphical"] != hash_text(" ".join(graphical)):
        print("❌ Incorrect graphical password!")
        return

    # 3. Behavioral password
    print("\nBehavioral Password Test: Press Enter as quickly as possible after 'GO!'")
    input("Press Enter to start...")
    time.sleep(random.randint(2, 5))
    print("GO!")
    start = time.time()
    input()
    reaction_time = round(time.time() - start, 2)

    stored_time = users[username]["behavioral"]
    if abs(stored_time - reaction_time) > 1.0:  # 1 sec tolerance
        print("❌ Behavioral check failed!")
        print(f"Expected ~{stored_time}s, but you gave {reaction_time}s")
        return

    print(f"\n✅ Welcome back, {username}! Login successful 🎉\n")


# ===== Main Menu =====
def main():
    while True:
        print("===== Three Level Password System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again!\n")


# ===== Run program =====
if __name__ == "__main__":
    main()
