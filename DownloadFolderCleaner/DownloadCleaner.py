# Import module os to access different functions that allow to work with out operative system
import os
# Import module shutil to do complex operations in the repositories like move, copy files etc
import shutil

# Define main and add the routes for our different folders
# Will decide where to move each file depending on the extension

# Define the function that will check if the folders exist and move the files to them
def organizar_descargas(ruta_descargas, carpetas_destino, carpeta_otros):

    # First we check if the folders exist. If they dont we create them
    for carpeta in carpetas_destino.values():
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

    # Now we do the same with the "others" folder (for unknown extensions)

    if not os.path.exists(carpeta_otros):
        os.makedirs(carpeta_otros)


def main():
    # 
    ruta_descargas = "C:/Users/Diego/Downloads"  # Route to download folder (The one we want to clean and organize)

    carpetas_destino = {
        ('.jpg', '.jpeg', '.png', '.gif', '.bmp'): "F:/DESCARGAS/imagenes",
        ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'): "F:/DESCARGAS/documentos",
        ('.mp4', '.avi', '.mkv', '.mov'): "F:/DESCARGAS/videos",
        ('.mp3', '.wav', '.aac', '.flac'): "F:/DESCARGAS/musica",
        ('.zip', '.rar', '.7z', '.tar', '.gz'): "F:/DESCARGAS/comprimidos",
    } # We specify which files we will move to each folder

    carpeta_otros = "F:/DESCARGAS/otros"  # All the files with non-specified extensions will go to this folder

    # Call the function we defined and use our routes as atributes
    organizar_descargas(ruta_descargas, carpetas_destino, carpeta_otros)
    print("Organización completada.")


# Call main to run the program
if __name__ == "__main__":
    main()