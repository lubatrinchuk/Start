import os
from uploading import uploading_files
from reform import load_key
from reform import encrypt
from logging import logging

source = input("Введите путь к папке, в которой лежат все файлы, которые вы ходите передать: ")
dest = uploading_files(source)
logging(dest, "загрузка")

key = load_key()                            # загрузить ключ

rez = os.listdir(dest)
for item in rez:
    str = "файлы/"
    encrypt(str + item, key)
    logging(item, "преобразование")