from bs4 import BeautifulSoup
import os
import features
import pandas as pd
def open_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()
def create_soup(text):
    return BeautifulSoup(text, "html.parser")
def create_vector(soup):
    vector = [
# Caracteristicas binarias
features.has_title(soup),
features.has_input(soup),
features.has_button(soup),
features.has_image(soup),
features.has_submit(soup),
features.has_link(soup),
features.has_password(soup),
features.has_email_input(soup),
features.has_hidden_element(soup),
features.has_audio(soup),
features.has_video(soup),
# Caracteristicas cuantitativas
features.number_of_inputs(soup),
features.number_of_buttons(soup),
features.number_of_images(soup),
features.number_of_option(soup),
features.number_of_list(soup),
features.number_of_TH(soup),
features.number_of_TR(soup),
features.number_of_href(soup),
features.number_of_paragraph(soup),
features.number_of_script(soup),
features.length_of_title(soup)
]
    return vector
folder = "mini_dataset"
def create_2d_list(folder_name):
    directory = os.getcwd() + "/" + folder_name
    data = []
    for file in sorted(os.listdir(directory)):
        soup = create_soup(
            open_file(directory + "/" + file)
        )
        vector = create_vector(soup)
        data.append(vector)
    return data
data = create_2d_list(folder)
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
"length_of_title"
]
df = pd.DataFrame(data=data, columns=columns)
print(df.head())