import requests
from datetime import datetime  # <--- CRITICAL: Must be at the top

# --- TASK 1: File Operations ---
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

try:
    with open("python_notes.txt", "w", encoding="utf-8") as f:
        for line in notes:
            f.write(line + "\n")
    print("File 'python_notes.txt' created successfully.")
except Exception as e:
    print(f"File Error: {e}")

# --- TASK 2 & 4: API & Error Logging ---
def log_error(msg):
    # This will work now because of the import at the top
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error_log.txt", "a") as f:
        f.write(f"[{timestamp}] ERROR: {msg}\n")
    print(f"Error logged to 'error_log.txt': {msg}")

print("\n--- Fetching API Data ---")
URL = "https://dummyjson.com/products?limit=20"
try:
    # Added timeout=5 to prevent the "hanging" issue
    response = requests.get(URL, timeout=5)
    data = response.json()
    products = data["products"]
    
    print(f"{'ID':<4} | {'Title':<20} | {'Price'}")
    for p in products:
        print(f"{p['id']:<4} | {p['title'][:20]:<20} | ${p['price']}")

except Exception as e:
    log_error(f"API Fetch failed: {e}")

# --- TASK 3: Exception Handling Tests ---
print("\n--- Testing Exception Handling ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    log_error("Attempted to divide by zero.")

try:
    with open("ghost_file.txt", "r") as f:
        pass
except FileNotFoundError:
    log_error("Tried to open a file that doesn't exist.")