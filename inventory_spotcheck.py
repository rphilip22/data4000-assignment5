import requests

# Step 1 — Student Key
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

total_skus = 0
reorder_count = 0

# Step 2 — SKU Entry Loop
while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("Invalid SKU. Try again.")
        continue

    # Step 3 — On-Hand Quantity Validation
    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand < 0:
                print("Inventory must be 0 or greater.")
                continue
            break
        except ValueError:
            print("Invalid number. Enter an integer.")

    total_skus += 1

    # Step 4 — Threshold Logic (based on seed)
    if seed % 3 == 0:
        threshold = 15
    elif seed % 3 == 1:
        threshold = 12
    else:
        threshold = 9

    # Step 5 — Reorder Decision
    if on_hand < threshold:
        reorder_count += 1

# Step 6 — Select API Term
if seed % 2 == 0:
    term = "weezer"
else:
    term = "drake"

api_status = "FAILED"
song_count = "N/A"

url = "https://itunes.apple.com/search"
params = {
    "entity": "song",
    "limit": 5,
    "term": term
}

# Step 7–9 — API Request + Exception Handling
try:
    response = requests.get(url, params=params, timeout=5)

    if response.status_code != 200:
        api_status = "FAILED"
    else:
        data = response.json()

        if "results" not in data:
            api_status = "INVALID_RESPONSE"
        else:
            api_status = "OK"
            song_count = 0

            for item in data["results"]:
                if item.get("kind") == "song":
                    song_count += 1

except requests.exceptions.RequestException:
    api_status = "FAILED"
except ValueError:
    api_status = "INVALID_RESPONSE"

# Step 10 — Final Output
print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {term}")
print(f"Songs returned: {song_count}")
print(f"API status: {api_status}")