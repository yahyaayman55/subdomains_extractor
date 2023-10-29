import re
def extract_subdomains(input_file):
    subdomains = set()
    tlds = ['.com', '.org', '.net']

    with open(input_file, 'r') as file:
        for line in file:
            matches = re.findall(r'(https?://)?([a-zA-Z0-9.-]+)(\.\w+)', line)
            for match in matches:
                if match[2] in tlds:
                    if match[0]:
                        subdomains.add(match[1] + match[2] + "/")
                    else:
                        subdomains.add('https://' + match[1] + match[2] + "/")
    return subdomains
def write_subdomains(output_file, subdomains):
    with open(output_file, 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '\n')
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    subdomains = extract_subdomains(input_file)
    write_subdomains(output_file, subdomains)

    print(f"Subdomains with specific TLDs and a forward slash added, extracted from {input_file} and written to {output_file}")
