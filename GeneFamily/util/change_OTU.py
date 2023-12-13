#!/usr/bin/python3

import sys

# Function to parse the TSV file and create a mapping from gene IDs to species names
def parse_tsv_for_mapping(tsv_content):
    mapping = {}
    lines = [line.strip().split('\t') for line in tsv_content]
    species_names = lines[0][1:]  # Extract species names from the first line

    for line in lines[1:]:
        og, *gene_ids = line
        for species, gene_id in zip(species_names, gene_ids):
            mapping[gene_id] = species

    return mapping

# Function to replace gene IDs in the FASTA file with species names
def replace_gene_ids_in_fasta(fasta_content, mapping):
    modified_fasta = []
    for line in fasta_content:
        if line.startswith('>'):
            gene_id = line[1:].strip().split()[0]  # Extract gene ID
            species_name = mapping.get(gene_id, "Unknown_Species")
            modified_fasta.append(f"> {species_name}\n")
        else:
            modified_fasta.append(line)
    return modified_fasta

def main(og_single_copy_file_path, fasta_file_path):
    with open(og_single_copy_file_path, 'r') as file:
        og_single_copy_content = file.readlines()

    with open(fasta_file_path, 'r') as file:
        fasta_content = file.readlines()

    gene_to_species_mapping = parse_tsv_for_mapping(og_single_copy_content)
    modified_fasta_content = replace_gene_ids_in_fasta(fasta_content, gene_to_species_mapping)

    modified_fasta_file_path = fasta_file_path.replace('.fa', '_Modified.fa')
    with open(modified_fasta_file_path, 'w') as file:
        file.writelines(modified_fasta_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <OG_SingleCopy.tsv file path> <FASTA file path>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])
