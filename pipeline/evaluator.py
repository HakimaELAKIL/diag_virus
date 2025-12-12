from core.model import VirusModel


def evaluate(sample):
    model = VirusModel()
    return model.diagnose(sample)
