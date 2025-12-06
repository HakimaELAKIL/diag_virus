def diagnose(score: float) -> str:
    """
    Retourne 'positif' si le score > 0.5, sinon 'negatif'.
    """
    if score > 0.5:
        return "positif"
    return "negatif"