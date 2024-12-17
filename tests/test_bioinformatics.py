
# Test for Bioinformatics Module
def test_align_sequences():
    result = align_sequences("ATCG", "TAGC")
    assert result == "Alignment complete.", "Sequence alignment failed."

def test_visualize_genome():
    result = visualize_genome("Sample genome data")
    assert result == "Genome visualization complete.", "Genome visualization failed."
