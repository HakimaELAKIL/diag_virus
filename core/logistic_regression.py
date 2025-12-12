class LogisticRegression:
    def predict(self, x):
        if sum(x) > 0:
            return 1
        return 0
