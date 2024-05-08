import subprocess
import csv
import os
import re
import argparse


# Parameters
domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@live.com", "@yahoo.fr", "@hotmail.fr", "@outlook.fr", "@live.fr", "@proton.me"]

# Command line arguments parsing
parser = argparse.ArgumentParser()
parser.add_argument('search_term', nargs="+", help='First name and Last name, or Username to search for')
parser.add_argument('-B', action='store_true', help='Option -B to generate only specified domain addresses')
args = parser.parse_args()

# Check the validity of the search term
if len(args.search_term) > 2:
    print("Error: The search term must be First name and Last name or just Username to search for.")
    exit()
elif len(args.search_term) == 2:
    search_term = ' '.join(args.search_term)
else:
    search_term = args.search_term[0]

regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")")

if re.fullmatch(regex, search_term.replace(' ', '')):
    print("")

else:
    print("Error: The search term contain non authorized caracters in mail address.")
    exit()

# Function to generate probable email addresses
def generate_addresses(search_term, domains):
    addresses = []

    if " " in search_term:
        first_name, last_name = search_term.split(' ', 1)

        for domain in domains:
            email_formats = [
                first_name.lower() + '.' + last_name.lower() + domain,
                first_name.lower()[0] + last_name.lower() + domain,
                first_name.lower() + last_name.lower()[0] + domain,
                first_name.lower()[0] + '.' + last_name.lower() + domain,
                last_name.lower() + '.' + first_name.lower() + domain,
                last_name.lower() + first_name.lower()[0] + domain,
                last_name.lower()[0] + '.' + first_name.lower() + domain,
                first_name.lower() + last_name.lower() + domain,
                last_name.lower() + first_name.lower() + domain,
                first_name.lower() + '.' + last_name.lower()[0] + domain,
                first_name.lower() + '_' + last_name.lower()[0] + domain,  # Added format with underscore
                first_name.lower()[0] + '_' + last_name.lower() + domain,  # Added format with underscore
                first_name.lower() + '_' + last_name.lower() + domain,      # Added format with underscore
                last_name.lower() + '_' + first_name.lower() + domain,      # Added format with underscore
                last_name.lower() + '_' + first_name.lower()[0] + domain,   # Added format with underscore
                last_name.lower()[0] + '_' + first_name.lower() + domain,   # Added format with underscore
            ]

            addresses.extend(email_formats)

    else:
        username = search_term

        for domain in domains:
            email_formats = [
                username.lower() + domain,
            ]

            addresses.extend(email_formats)

    return addresses

# Generate probable email addresses based on the search term
# Check if the -B option is specified to filter addresses by domain name
if args.B:
    domain = []
    domain_input = input("Enter the domain name: ")
    
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+).([-!#-'*+/-9=?A-Z^-~]+)")

    if re.fullmatch(regex, domain_input):
        domain_input = "@" + domain_input
        domain.append(domain_input)
        email_addresses = generate_addresses(search_term, domain)

    else:
        print("Error: The domain name is not correct.")
        exit() 
else:
    email_addresses = generate_addresses(search_term, domains)

# Create directory structure
if " " in search_term:
    first_name, last_name = search_term.split(' ', 1)
else:
    first_name = search_term
    last_name = "[username]"
    
directory_command = f"mkdir {first_name}-{last_name}"
subprocess.run(directory_command, shell=True)
    
# Execute the command to test each email address
for address in email_addresses:
    command_holehe = f"cd {first_name}-{last_name} && holehe {address} -C"
    subprocess.run(command_holehe, shell=True)
    directory = os.path.join(os.getcwd(), f"{first_name}-{last_name}")

# List to store valid file names
valid_files = []

# Iterate through all files in the directory
for file in os.listdir(directory):
    if file.endswith(".csv") and file.startswith("holehe_"):
        # Add the valid file name to the list
        valid_files.append(file)

# Output file path
output_path = os.path.join(directory, 'RESULT.csv')

# Open the output file in write mode
with open(output_path, 'w', newline='') as csvfile:
    writer = None

    # Iterate through valid files
    for file in valid_files:
        # CSV file path
        file_path = os.path.join(directory, file)

        # Extract email address from the file name
        email_address_part1 = file.split("_", 2)[2]
        email_address = email_address_part1.split("_results.csv")[0]

        # Open the CSV file in read mode
        with open(file_path, newline='') as csvfile_in:
            reader = csv.DictReader(csvfile_in)
            fieldnames = reader.fieldnames

            # Add the 'email address' column in the first position
            # Remove the 'name' column (replaced by the 'email address' column)
            fieldnames.remove("name")
            fieldnames.insert(0, 'email address')

            # Create the writer if not already done
            if writer is None:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

            # Read each row from the CSV file and write it to the output file with the corresponding email address
            for row in reader:
                row['email address'] = email_address
                writer.writerow(row)

print("Successfully generated RESULT.csv file.")
