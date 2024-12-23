
import sys
import os

# Ensure correct path for imports
sys.path.insert(0, '/mnt/data/HyCAN-main/HyCAN-main/src')

# Import the functions to test
from src.bioinformatics.sequence_analysis import align_sequences
from src.bioinformatics.genomic_visualization import visualize_genome

def test_align_sequences():
    result = align_sequences("ATCG", "TAGC")
    assert result == "Alignment complete.", "Alignment test failed."

def test_visualize_genome():
    result = visualize_genome("Sample genome data")
    assert result == "Genome visualization complete.", "Genome visualization failed."
