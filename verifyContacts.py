import csv
import re

def normalize_phone_number(phone):
    """Normalize Indian phone numbers to a standard 10-digit format."""
    digits = re.sub(r'\D', '', phone)  # Remove non-digit characters
    if digits.startswith('91') and len(digits) > 10:
        digits = digits[2:]  # Remove country code +91
    elif digits.startswith('0') and len(digits) > 10:
        digits = digits[1:]  # Remove leading 0
    return digits if len(digits) == 10 else None  # Return only valid 10-digit numbers

def extract_phone_numbers_from_row(row):
    """Extract and normalize all phone numbers from a given row."""
    phone_numbers = set()
    for field in row.values():  # Iterate over all columns
        potential_numbers = re.findall(r'[\d\+\-\s]+', field) if field else []
        for num in potential_numbers:
            normalized = normalize_phone_number(num)
            if normalized:
                phone_numbers.add(normalized)
    return phone_numbers

def load_phone_numbers_from_csv(filename):
    """Extract phone numbers from every cell of a given CSV file."""
    phone_numbers = set()
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            phone_numbers.update(extract_phone_numbers_from_row(row))
    return phone_numbers

# Load phone numbers from total-skip.csv
total_skip_numbers = load_phone_numbers_from_csv('total-skip.csv')

# Load all possible phone numbers from skip.csv (any column)
skip_numbers = load_phone_numbers_from_csv('skip.csv')

# Check if any number in total-skip.csv exists in skip.csv
invalid_numbers = total_skip_numbers.intersection(skip_numbers)
breakpoint()
# Print results
if invalid_numbers:
    print("Verification Failed: The following numbers are still in total-skip.csv but should have been removed:")
    for num in sorted(invalid_numbers):
        print(f"- {num}")
else:
    print("Verification Passed: No unwanted numbers found in total-skip.csv.")
