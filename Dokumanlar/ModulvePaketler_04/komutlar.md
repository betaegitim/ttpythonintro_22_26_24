# Ortam Oluşturmak
## Linux MacOS
* python3 -m venv env
## Windows
* python -m venv env
# Ortamı Aktif Hale Getirmek
## Linux MacOS
* source env/bin/activate
## Windows
* env/Scripts/activate
* env/Scripts/deactivate


#### Kütüphane Listesi Almak
pip freeze > requirements.txt
#### Kütüphane Listesinden Kurulum Yapmak 
pip install -r requirements.txt 