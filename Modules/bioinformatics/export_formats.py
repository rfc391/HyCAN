
# Data Export Tools

# Export sequence alignments or trees in standard formats.
def export_alignment_to_fasta(alignment_data, output_file):
    with open(output_file, "w") as f:
        f.write(">Sequence1\nATCG\n>Sequence2\nTAGC\n")
    print(f"Alignment exported to {output_file}.")
