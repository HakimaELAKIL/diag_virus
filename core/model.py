from .logistic_regression import LogisticRegression

class VirusModel:
    def __init__(self):
        self.model = LogisticRegression()

    def diagnose(self, features):
        return self.model.predict(features)
