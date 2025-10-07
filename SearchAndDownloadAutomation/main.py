import os
import sys

from results_parser import ResultsProcessor
from file_downloader import FileDownloader
from browserautosearch import BrowserAutoSearch


def main():
    

    query = input("Busqueda con Selenium. Introduce la consulta: ")
    
    # Realizar la búsqueda con Selenium
    browser = BrowserAutoSearch()
    browser.search_google(query=query)
    resultados = browser.google_search_results()
    browser.quit()

    # Parsear los resultados obtenidos por selenium y preguntar por las descargas
    rparser = ResultsProcessor(resultados)

    output_html = input("Si quieres descargar los resultados en html escribe el nombre del fichero, si no pulsa INTRO: ")
    output_json = input("Si quieres descargar los resultados en json escribe el nombre del fichero, si no pulsa INTRO: ")

    # Mostrar los resultados en la línea de comandos
    rparser.mostrar_pantalla()

    # Exportar resultados en formato HTML si se especifica
    if output_html != "":
        rparser.exportar_html(output_html)

    # Exportar resultados en formato JSON si se especifica
    if output_json != "":
        rparser.exportar_json(output_json)



    # Descarga los documentos especificados que se encuentren en los resultados
    download = input("Si quieres descargar documentos adjuntos especifica las extensiones, si no pulsa INTRO. (Ej: pdf,doc,jpeg): ").lower
    if download != "":
        file_types = download.split(",")
        urls = [resultado['link'] for resultado in resultados]
        fdownloader = FileDownloader("Descargas")
        fdownloader.filtrar_descargar_archivos(urls, file_types)


if __name__ == "__main__":
    
    main()