import csv
import re

def normalize_phone_number(phone):
    # Remove non-digit characters
    digits = re.sub(r'\D', '', phone)
    # Remove leading zeros or country code
    if digits.startswith('91') and len(digits) == 12:
        digits = digits[2:]
    elif digits.startswith('0'):
        digits = digits[1:]
    return digits

def extract_phone_numbers(row):
    phones = set()
    for field in row:
        potential_numbers = re.findall(r'\+?\d[\d\s\-\(\)]+', field)
        for num in potential_numbers:
            normalized = normalize_phone_number(num)
            if len(normalized) == 10:
                phones.add(normalized)
    return phones

# Load and normalize skip numbers
skip_numbers = set()
with open('skip.csv', newline='', encoding='utf-8') as skipfile:
    reader = csv.reader(skipfile)
    headers = next(reader)
    for row in reader:
        skip_numbers.update(extract_phone_numbers(row))

# Process total.csv and write to total-skip.csv
with open('total.csv', newline='', encoding='utf-8') as totalfile, \
     open('total-skip.csv', 'w', newline='', encoding='utf-8') as outputfile:
    reader = csv.reader(totalfile)
    writer = csv.writer(outputfile)
    headers = next(reader)
    writer.writerow(headers)
    for row in reader:
        row_numbers = extract_phone_numbers(row)
        if not row_numbers.intersection(skip_numbers):
            writer.writerow(row)
