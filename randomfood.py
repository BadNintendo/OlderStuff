import random
import json
from datetime import datetime

# Main food types
main_foods = ["Burger", "Chicken", "Steak", "Sushi", "Chow Mein", "Fried Rice"]

# Sides
sides = {
    "Burger": ["Fries", "Onion Rings", "Salad"],
    "Chicken": ["Mashed Potatoes", "Coleslaw", "Biscuit"],
    "Steak": ["Baked Potato", "Steamed Vegetables", "Garlic Bread"],
    "Sushi": ["Miso Soup", "Edamame", "Seaweed Salad"],
    "Chow Mein": ["Spring Rolls", "Dumplings", "Wonton Soup"],
    "Fried Rice": ["Egg Roll", "Sweet and Sour Pork", "Hot and Sour Soup"]
}

# Additional pairings
additional_pairings = {
    "Burger": ["Soda", "Milkshake"],
    "Chicken": ["Lemonade", "Iced Tea"],
    "Steak": ["Red Wine", "Beer"],
    "Sushi": ["Green Tea", "Sake"],
    "Chow Mein": ["Hot Tea", "Plum Wine"],
    "Fried Rice": ["Bubble Tea", "Soft Drink"]
}

log_file = "meal_log.json"

def load_log():
    try:
        with open(log_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_log(log):
    with open(log_file, 'w') as file:
        json.dump(log, file, indent=4)

def create_log_file_if_not_exists():
    try:
        with open(log_file, 'x') as file:
            json.dump({}, file)
    except FileExistsError:
        pass

def get_random_meal():
    create_log_file_if_not_exists()
    
    log = load_log()
    today = datetime.today().strftime('%Y-%m-%d')
    time_stamp = datetime.now().strftime('%H:%M:%S')

    if today not in log:
        log[today] = []

    previous_sides = [entry["side"] for entry in log[today]]
    previous_pairings = [entry["pairing"] for entry in log[today]]

    main_food = random.choice(main_foods)
    available_sides = [side for side in sides[main_food] if side not in previous_sides]
    available_pairings = [pairing for pairing in additional_pairings[main_food] if pairing not in previous_pairings]

    if not available_sides or not available_pairings:
        return None, None, None

    side = random.choice(available_sides)
    pairing = random.choice(available_pairings)

    log[today].append({"main_food": main_food, "side": side, "pairing": pairing, "time": time_stamp})
    save_log(log)

    return main_food, side, pairing

def display_log():
    log = load_log()
    for date, entries in log.items():
        print(f"Date: {date}")
        for entry in entries:
            print(f"  Time: {entry['time']}, Main Food: {entry['main_food']}, Side: {entry['side']}, Pairing: {entry['pairing']}")

# Generate and print a random meal, ensuring no repeat sides or pairings on the same day
main_food, side, pairing = get_random_meal()
if main_food and side and pairing:
    print(f"Main Food: {main_food}")
    print(f"Side: {side}")
    print(f"Pairing: {pairing}")
else:
    print("No available combinations that avoid repeats found for today.")

# Display the logged results with timestamps
display_log()
