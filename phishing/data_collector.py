# Deshabilitar advertencias de solicitudes HTTPS no seguras (comun con sitios de phishing)
from urllib import response
import requests as re
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
# unstructured to structured
from bs4 import BeautifulSoup
import pandas as pd
import feature_extraction as fe
disable_warnings(InsecureRequestWarning)
# url_filename = "top-1m.csv"
url_filename = "verified_online.csv"
df = pd.read_csv(url_filename)
url_list = df['url'].tolist()
# Limitar el numero de URLs para pruebas. Comienzamos haciendo pruebas con una muestra.
begin_index = 0
end_index = 100 # Procesa solo las primeras 100 URLs
collection_list = url_list[begin_index:end_index]
# Aseguramos que las URLs tengan el protocolo
# Las URLs de Tranco pueden venir sin 'http://' o 'https://'
def normalize_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return "http://" + url
collection_list = [normalize_url(url) for url in collection_list]
def create_structured_data(url_list):
    data_list = []
    for i in range(0, len(url_list)):
        try:
            response = re.get(url_list[i], verify=False, timeout=4)
            if response.status_code != 200:
                print(i, ". HTTP connection was not successful for the URL: ", url_list[i])
            else:
                soup = BeautifulSoup(response.content, "html.parser")
                vector = fe.create_vector(soup)
                vector.append(str(url_list[i]))
                data_list.append(vector)
        except re.exceptions.RequestException as e:
            print(i, " --> ", e)
            continue
    return data_list
data = create_structured_data(collection_list)
columns = [
# Caracteristicas binarias
"has_title",
"has_input",
"has_button",
"has_image",
"has_submit",
"has_link",
"has_password",
"has_email_input",
"has_hidden_element",
"has_audio",
"has_video",
# Caracteristicas cuantitativas
"number_of_inputs",
"number_of_buttons",
"number_of_images",
"number_of_option",
"number_of_list",
"number_of_th",
"number_of_tr",
"number_of_href",
"number_of_paragraph",
"number_of_script",
"length_of_title",
"URL"
]
df = pd.DataFrame(data=data, columns=columns)
# --- ANADIR ETIQUETAS (LABELING) ---
# Este es un paso CRUCIAL para el aprendizaje supervisado.
# Si collection_list era de URLs LEGITIMAS:
# df['label'] = 0
# Si collection_list era de URLs de PHISHING:
df['label'] = 1
# df.to_csv("structured_data_legitimate.csv", mode='a', index=False)
df.to_csv("structured_data_phishing.csv", mode='a', index=False)