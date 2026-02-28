
from pathlib import Path

# Always start from a known folder next to this file
base = Path(__file__).parent
data_dir = base / "MyFiles"
data_dir.mkdir(exist_ok=True)

print("Working in:", data_dir)

# 1) Write a new text file (w = write/overwrite)
text_path = data_dir / "orders.txt"
with open(text_path, "w", encoding="utf-8") as f:
    f.write("Order #1001: Burger x2, Fries x1\n")
    f.write("Order #1002: Pizza x1, Coke x2\n")
print("Wrote:", text_path)


# 2) Append to the same file (a = append)
with open(text_path, "a", encoding="utf-8") as f:
    f.write("Order #1003: Sushi x3, Miso Soup x1\n")
print("Appended one line.")


# 3) Read the whole file at once (r = read)
with open(text_path, "r", encoding="utf-8") as f:
    content = f.read()
print("--- File content (read) ---")
print(content)


# 4) Read line by line (good habit for larger files)
print("--- File content (line by line) ---")
with open(text_path, "r", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}:", line)


# 5) Read only the first N characters
with open(text_path, "r", encoding="utf-8") as f:
    first_five = f.read(5)
print("First 5 chars:", repr(first_five))


# find line number of 'Pizza' order in the menu/orders file
line_number = None
search_text = "Pizza"
text_path = data_dir / "orders.txt"
with open(text_path, "r", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        if search_text in line:
            line_number = number
            break
print("Line number of 'Pizza' order:", line_number)

