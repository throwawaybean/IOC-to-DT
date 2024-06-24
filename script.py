import csv
import argparse
from urllib.parse import urlparse
from datetime import datetime, timedelta

# Function to clean up URL
def clean_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme:
        url = parsed_url.netloc
    if parsed_url.path:
        url = parsed_url.netloc + parsed_url.path.split('/')[0]
    # Remove www. from the URL if it starts with www.
    if url.startswith("www."):
        url = url.replace("www.", "", 1)
    return url

# Function to process the CSV file
def process_csv(file_name):
    # Set to hold unique domains
    unique_domains = set()

    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Skip first three rows
        for _ in range(3):
            next(reader)

        # Process each row
        for row in reader:
            # Skip empty rows
            if not row:
                continue
            
            # Ensure row has at least 2 columns
            if len(row) >= 2:
                data_type = row[0]
                data_value = row[1]

                if data_type == "URL/URL":
                    # Clean URL
                    domain = clean_url(data_value)
                    unique_domains.add(domain)

                elif data_type == "DOMAIN/DOMAINE":
                    # Remove www. from the domain if it starts with www.
                    if data_value.startswith("www."):
                        data_value = data_value.replace("www.", "", 1)
                    unique_domains.add(data_value)

    # Prepare data for new CSV file
    new_data = [
        {
            "domain": domain,
            "exact hostname": "",
            "description": "IOC from CCCS",
            "strength": 100,
            "source": "Default",
            "expiry": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S"),
            "iagn": "True"
        }
        for domain in unique_domains
    ]

    # Write new data to CSV file
    with open("watched-domains.csv", "w", newline='') as csvfile:
        fieldnames = new_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_data)

    # Print a success message
    print(f"watched-domains.csv was successfully created in the current directory. This file should be imported to Darktrace's Watch Domain under Intel.")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process a CSV file and generate a new CSV file.")
parser.add_argument("-f", "--file", required=True, help="The name of the CSV file to process.")
args = parser.parse_args()

# Call the function to process the CSV file
process_csv(args.file)

