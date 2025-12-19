from scraper import save_html_file
from scraper import scrape_content
from scraper import create_mini_dataset
from features import *
import os
folder = "mini_dataset"
path = os.getcwd() + "/" + folder
url_list = [
"https://www.kaggle.com",
"https://stackoverflow.com",
"https://www.researchgate.net",
"https://www.python.org",
"https://www.w3schools.com",
"https://github.com",
"https://scholar.google.com",
"https://www.mendeley.com",
"https://www.overleaf.com",
"https://www.ehu.eus"
]
#create_mini_dataset(path, url_list)
with open("mini_dataset/1.html", "r", encoding="utf-8") as f:
    test = f.read()
soup = BeautifulSoup(test, "html.parser")
print("has_title --> ", has_title(soup))
print("has_input --> ", has_input(soup))
print("has_button --> ", has_button(soup))
print("has_image --> ", has_image(soup))
print("has_submit --> ", has_submit(soup))
print("has_link --> ", has_link(soup))
print("has_password --> ", has_password(soup))
print("has_email_input --> ", has_email_input(soup))
print("has_hidden_element --> ", has_hidden_element(soup))
print("has_audio --> ", has_audio(soup))
print("has_video --> ", has_video(soup))
print("number_of_inputs --> ", number_of_inputs(soup))
print("number_of_buttons --> ", number_of_buttons(soup))
print("number_of_images --> ", number_of_images(soup))
print("number_of_option --> ", number_of_option(soup))
print("number_of_list --> ", number_of_list(soup))
print("number_of_TH --> ", number_of_TH(soup))
print("number_of_TR --> ", number_of_TR(soup))
print("number_of_href --> ", number_of_href(soup))
print("number_of_paragraph --> ", number_of_paragraph(soup))
print("number_of_script --> ", number_of_script(soup))
print("length_of_title --> ", length_of_title(soup))