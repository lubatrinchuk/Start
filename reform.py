from cryptography.fernet import Fernet

def write_key():  # Создаем ключ единожды и сохраняем его в файл
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key():  # Загружаем ключ 'crypto.key' из текущего каталога
    return open('crypto.key', 'rb').read()

def encrypt(filename, key):                     # Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:          # прочитать все данные файла
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)       # шифрование данных
    with open(filename, 'wb') as file:          # записать зашифрованный файл
        file.write(encrypted_data)



