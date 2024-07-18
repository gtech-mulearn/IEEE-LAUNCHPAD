#!/bin/bash

# to run first ` chmod +x ./get_muids.sh`

# Define the path to the profile folder
profile_folder="profiles"

# Define the CSV file name
csv_file="muids.csv"

# Create the CSV file and write the header
echo "MuId" > "$csv_file"

# Iterate through each file in the profile folder
for filename in "$profile_folder"/*.md; do
  if [ -f "$filename" ]; then
    # Remove the .md extension
    cleaned_email=$(basename "$filename" .md)
    # Append the cleaned email to the CSV file
    echo "$cleaned_email" >> "$csv_file"
  fi
done

echo "Cleaned muid have been written to $csv_file"
