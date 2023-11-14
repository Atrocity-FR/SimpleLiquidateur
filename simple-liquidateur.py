def supprimer_lignes_fichier2_si_presentes(fichier1, fichier2):
    try:
        with open(fichier1, 'r') as f1, open(fichier2, 'r') as f2:
            lignes_fichier1 = set(line.strip() for line in f1.readlines())
            lignes_fichier2 = [line.strip() for line in f2.readlines()]

        lignes_supprimees = 0
        with open(fichier2, 'w') as f2:
            for ligne in lignes_fichier2:
                if ligne not in lignes_fichier1:
                    f2.write(ligne + '\n')
                else:
                    lignes_supprimees += 1

        print(f"Opération terminée avec succès. {lignes_supprimees} lignes du fichier2 ont été supprimées car elles étaient présentes dans le fichier1.")
    except FileNotFoundError:
        print("Erreur: Un des fichiers n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur inattendue: {e}")

# Remplacez 'fichier1.txt' et 'fichier2.txt' par les noms de vos fichiers
fichier1 = 'fichier1.txt'
fichier2 = 'fichier2.txt'

supprimer_lignes_fichier2_si_presentes(fichier1, fichier2)
