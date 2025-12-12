from core.model import VirusModel


def test_virus_positive():
    model = VirusModel()
    assert model.diagnose([1, 0, 1]) == 1
    

def test_virus_negative():
    model = VirusModel()
    assert model.diagnose([-1, -2]) == 0
