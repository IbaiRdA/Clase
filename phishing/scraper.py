import os
# Definir el nombre de la carpeta
folder = "mini_dataset"
# Crear la carpeta si no existe
if not os.path.exists(folder):
    os.mkdir(folder)
path = os.getcwd() + "/" + folder
def save_html_file(to_where, text, name):
	file_name = name + ".html"
	with open(
		os.path.join(to_where, file_name),
		"w",
		encoding="utf-8"
	) as f:
		f.write(text)
import requests
def scrape_content(url):
    response = requests.get(url)
    # Verificar si la conexion HTTP fue exitosa
    if response.status_code == 200:
        print(f"HTTP connection is successful for the url: {url}")
        return response
    else:
        print(f"HTTP connection is not successful for the url: {url}")
        return None
def create_mini_dataset(to_where, url_list):
    for i in range(0, len(url_list)):
        content = scrape_content(url_list[i])
        if content is not None:
            save_html_file(to_where, content.text, str(i))
    print("Mini dataset is created.")
