from virus_diag import diagnose

def test_positive():
    assert diagnose(0.8) == "negatif"

def test_negative():
    assert diagnose(0.3) == "negatif"