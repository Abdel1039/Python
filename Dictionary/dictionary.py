
import json

with open('classe.json', 'r+') as file:
    eleves = json.load(file)


question = input("Voulez-vous savoir la note d'un élève (note), l'appreciation de toute la classe (app), ajoutez un élève (add) ou bien de supprimer un élève (supp) ?")

if question == 'note':
    for eleve in eleves:
        print(eleve)
    quelle_eleve = input("Voulez-vous la note de quelle élève ?")
    print(eleves[quelle_eleve]['note'], '/20')

if question == 'app':
    for prenom, appreciation in eleves.items():
        print(f'{prenom} :', eleves[prenom]['appreciation'])

if question == 'add':
    nom = input("Quelle est le prenom du l'élève ?")
    note = int(input("Quelle est sa note ?"))
    app = input("Quelle sa appreciation ?")
    eleves[nom] = {
        'notes': note,
        'appreciation': app
    }
    for eleve in eleves:
        print(eleve)
    print('élève ajoute !')

if question == 'supp':
    for eleve in eleves:
        print(eleve)
    supprime = input('Voulez-vous supprimer quelle élève ?')
    del eleves[supprime]
    for eleve in eleves:
        print(eleve)
    print('élève supprimer !')