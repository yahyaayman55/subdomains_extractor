import re

# Function to extract subdomains with specific top-level domains from a text file and add a "/"
def extract_subdomains(input_file):
    subdomains = set()
    tlds = ['.com', '.org', '.net']

    with open(input_file, 'r') as file:
        for line in file:
            # Use a regular expression to find subdomains with specific TLDs in each line
            matches = re.findall(r'(https?://)?([a-zA-Z0-9.-]+)(\.\w+)', line)
            for match in matches:
                if match[2] in tlds:
                    if match[0]:
                        subdomains.add(match[1] + match[2] + "/")
                    else:
                        subdomains.add('https://' + match[1] + match[2] + "/")
    return subdomains

# Function to write subdomains to an output file
def write_subdomains(output_file, subdomains):
    with open(output_file, 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '\n')

# Main script
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    subdomains = extract_subdomains(input_file)
    write_subdomains(output_file, subdomains)

    print(f"Subdomains with specific TLDs and a forward slash added, extracted from {input_file} and written to {output_file}")
