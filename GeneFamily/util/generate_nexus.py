#!/usr/bin/python3

import sys

def create_nexus_file(og_ids):
    nexus_content = "#nexus\nbegin sets;\n"
    part_number = 1

    for og_id in og_ids:
        og_id = og_id.strip()  # Remove any trailing newline characters
        charset_line = f"    charset part{part_number} = {og_id}.aligned.trimed.fa;\n"
        nexus_content += charset_line
        part_number += 1

    nexus_content += "end;"

    return nexus_content

def main(og_ids_file_path):
    # Read the OG IDs from the file
    with open(og_ids_file_path, 'r') as file:
        og_ids = file.readlines()

    # Create Nexus file content
    nexus_content = create_nexus_file(og_ids)

    # Path for the output Nexus file
    nexus_file_path = og_ids_file_path.replace('.txt', '.nex')


    # Save the Nexus content to a file
    with open(nexus_file_path, 'w') as file:
        file.write(nexus_content)

    print(f"Nexus file saved at {nexus_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <OG_id file path>")
        sys.exit(1)
    
    main(sys.argv[1])
