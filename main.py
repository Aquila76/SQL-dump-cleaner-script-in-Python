import os, shutil

def main():
    """Fonction main."""

    print("Suppression en cours...")
    
    folder = "C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Log\Polybase\dump"
    errorHappened = False
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            os.unlink(file_path)
        except Exception as e:
            print(f"Impossible de supprimer le fichier {file_path} : {e}.")
            errorHappened = True

    print("Suppression terminée.")

    if(errorHappened):
        input("Appuyez sur Entrée pour quitter le programme...")

if __name__ == "__main__":
    main()
