import os
import csv

# Define the path to the profile folder
profile_folder = 'profiles'

# List to store cleaned email addresses
cleaned_emails = []

# Iterate through each file in the profile folder
for filename in os.listdir(profile_folder):
    if filename.endswith('.md'):
        # Remove the .md extension
        cleaned_email = filename.replace('.md', '')
        cleaned_emails.append(cleaned_email)

# Define the CSV file name
csv_file = 'cleaned_emails.csv'

# Write the cleaned email addresses to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email'])  # Write the header
    for email in cleaned_emails:
        writer.writerow([email])

print(f"Cleaned email addresses have been written to {csv_file}")
