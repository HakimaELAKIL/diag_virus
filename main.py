from virus_diag import diagnose

if __name__ == "__main__":
    score = float(input("Entrer un score entre 0 et 1 : "))
    print("Résultat :", diagnose(score))