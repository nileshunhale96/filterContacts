#Google Contacts Filter

Overview

This project filters out contacts from a Google Contacts CSV file (total.csv) by removing any phone numbers that exist in another file (skip.csv). The final filtered contacts are saved in total-skip.csv.

Features

- Supports various phone number formats (e.g., +91 98765-43210, 0 98765 43210, 98765-43210).
- Removes all unwanted numbers found in skip.csv.
- Verifies that no skipped numbers are present in the final output.
- Works with Google Contacts CSV format.
