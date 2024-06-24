# Aventail IOC Processor for Darktrace

This Python script processes a CSV file of Indicators of Compromise (IOCs) from Aventail and generates a new CSV file with specific modifications. The generated file is suitable for import into the Darktrace's Watch Domain under Intel.

## Description

The script reads a CSV file, cleans up URLs and domains, removes duplicates, and writes the modified data to a new CSV file named `watched-domains.csv`. The new CSV file includes the following columns:

- `domain`: Extracted data from the original file.
- `exact hostname`: Empty.
- `description`: "IOC from CCCS".
- `strength`: 100.
- `source`: "Default".
- `expiry`: A date and time a month from the current date, formatted as "YYYY-MM-DD HH:MM:SS".
- `iagn`: "True".

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed. This script was developed using Python 3.8.

## Usage

Run the script from the command line and provide the name of the CSV file to process using the `-f` or `--file` switch:

```bash
python script.py -f yourfile.csv
