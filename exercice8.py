convert_to = input("Quelle devise veux-tu convertir ? (Entrer $ ou E) ")
amount = float(input("Quel montant veux-tu convertir ? "))
euros_to_dollars = 1.09
dollars_to_euros= 0.92
if convert_to == "$":
    converted_amount = amount * dollars_to_euros
    print(f"{amount} $ est égal à {converted_amount} E")
elif convert_to == "E":
    converted_amount = amount * euros_to_dollars
    print(f"{amount} E est égal à {converted_amount} $")
else:
    print("Vous devez choisir entre $ et E.")
    
   
