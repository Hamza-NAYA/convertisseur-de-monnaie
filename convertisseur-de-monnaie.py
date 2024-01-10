from forex_python.converter import CurrencyRates, CurrencyCodes

# Fonction pour convertir la devise en utilisant le taux de change ou la nouvelle devise personnalisée
def convert_currency(cr, cc, new_currencie, history, amount, source_currency, target_currency):
    try:
        # Vérifier si la source_currency est une nouvelle devise personnalisée
        if source_currency in new_currencie:
            rate = new_currencie[source_currency]
        else:
            # Obtenir le taux de change à partir de la bibliothèque forex-python
            rate = cr.get_rate(source_currency, target_currency)
        
        # Calculer le montant converti
        converted_amount = round(amount * rate, 2)

        # Obtenir les symboles des devises pour l'affichage
        source_currency_symbol = cc.get_symbol(source_currency)
        target_currency_symbol = cc.get_symbol(target_currency)

        # Construire le résultat de la conversion et l'ajouter à l'historique
        conversion_result = f"{amount} {source_currency_symbol} ({source_currency}) = {converted_amount} {target_currency_symbol} ({target_currency})"
        history.append(conversion_result)

        return conversion_result

    except:
        # Gérer les erreurs de conversion
        return "Conversion impossible, veuillez vérifier les devises saisies"

# Fonction pour ajouter une nouvelle devise personnalisée
def add_currency(new_currencie):
    code = input("Entrez le code de la nouvelle devise: ").upper()
    rate = float(input("Entrez le taux de change par rapport à l'euro: "))
    new_currencie[code] = rate
    print(f"La devise {code} a été ajoutée avec succès")

# Fonction pour afficher l'historique des conversions
def display_history(history):
    if not history:
        print("Aucune conversion enregistrée.")
    else:
        print("Historique des conversions:")
        for conversion in history:
            print(conversion)

# Fonction principale
def main():
    # Initialisation des objets pour obtenir les taux de change et les symboles des devises
    cr = CurrencyRates()
    cc = CurrencyCodes()

    # Initialisation de la liste pour l'historique des conversions et du dictionnaire pour les nouvelles devises
    history = []
    new_currencie = {}

    while True:
        # Affichage du menu principal
        print("\n1. Convertir une devise")
        print("2. Ajouter une devise préférée")
        print("3. Afficher l'historique des conversions")
        print("4. Quitter\n")

        # Demande à l'utilisateur de choisir une option
        choice = input("Choisissez parmis les options (1/2/3/4): ")

        if choice == "1":
            # Conversion de devise
            print("\nListe des devises utilisables : EUR, IDR, BGN, ILS, GBP, DKK, CAD, JPY, HUF, RON, MYR, SEK, SGD, HKD, AUD, CHF, KRW, CNY, TRY, HRK, NZD, THB, USD, NOK, RUB, INR, MXN, CZK, BRL, PLN, PHP, ZAR\n")
            amount = float(input("Entrez le montant à convertir: "))
            source_currency = input("Entrez la devise source: ").upper()
            target_currency = input("Entrez la devise cible: ").upper()

            result = convert_currency(cr, cc, new_currencie, history, amount, source_currency, target_currency)
            print(result)

        elif choice == "2":
            # Ajout d'une nouvelle devise personnalisée
            add_currency(new_currencie)

        elif choice == "3":
            # Affichage de l'historique des conversions
            display_history(history)

        elif choice == "4":
            # Sortie du programme
            print("Merci d'avoir utilisé le convertisseur de devises")
            break

        else:
            # Gestion d'une option non valide
            print("Option non valide, veuillez réessayer.")

# Appel de la fonction principale pour exécuter le programme
main()
