import os
import qrcode
import urllib.parse

# Укажите путь к папке books и ссылку на домен вручную
books_dir = '/var/www/UrIU/media/books'
qr_books_dir = '/var/www/UrIU/media/qr_books'
base_url = 'https://uriu.uz/media/books/'

# Проходим по каждой папке (категории)
for category in os.listdir(books_dir):
    category_path = os.path.join(books_dir, category)
    if os.path.isdir(category_path):
        for file_name in os.listdir(category_path):
            file_path = os.path.join(category_path, file_name)
            if os.path.isfile(file_path):
                # Формируем ссылку на файл с учетом кодирования URL
                encoded_category = urllib.parse.quote(category)
                encoded_file_name = urllib.parse.quote(file_name)
                file_url = f"{base_url}{encoded_category}/{encoded_file_name}"

                # Генерация QR-кода
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(file_url)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')

                # Создание имени файла для QR-кода
                qr_code_filename = f"{os.path.splitext(file_name)[0]}.png"
                qr_code_dir = os.path.join(qr_books_dir, category)

                # Создание папки для QR-кодов, если ее нет
                os.makedirs(qr_code_dir, exist_ok=True)
                
                # Путь для сохранения QR-кода
                qr_code_path = os.path.join(qr_code_dir, qr_code_filename)

                # Сохранение QR-кода
                img.save(qr_code_path)

                print(f"QR-код для {file_name} создан и сохранен по пути: {qr_code_path}")
