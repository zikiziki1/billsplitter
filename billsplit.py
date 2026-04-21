depenses = []

while True:
    montant_dep = None  # initialisation avant la boucle

    while True:
        try:
            montant_dep = float(input("Entrez le montant de la dépense: "))
            break
        except ValueError:
            print("Veuillez entrer un montant numérique valide (ex: 12 ou 12.50):")

    depenses.append(montant_dep)

    reponse = input("Souhaitez-vous entrer une dépense supplémentaire ? (Y/N): ").strip().upper()
    if reponse == "N":
        break

somme_depenses = sum(depenses)
print(f"Somme totale des dépenses : {somme_depenses}€")

while True:
    try:
        nombre_pers = int(input("En combien voulez vous diviser la note ?: "))
        break
    except ValueError:
        print("Veuillez entrer un nombre:")
        

montant_pay=somme_depenses/nombre_pers

print(f"Chaque personne doit payer: {montant_pay}€")