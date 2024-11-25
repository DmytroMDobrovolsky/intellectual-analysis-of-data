import os
from PIL import Image

def resize_images_in_directory(directory, target_size=(256, 256), output_directory=None):
    """
    Змінює розмір усіх зображень у папці та підпапках, зберігаючи копії.
    
    :param directory: шлях до основної папки з підкаталогами
    :param target_size: бажаний розмір зображень (в пікселях)
    :param output_directory: шлях до папки, де зберігатимуться нові зображення, або None для збереження в тій самій папці
    """
    if output_directory and not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Створюємо вихідну папку, якщо вона не існує
    
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # перевірка на формат зображення
                image_path = os.path.join(subdir, file)
                try:
                    with Image.open(image_path) as img:
                        img = img.resize(target_size)  # зміна розміру зображення
                        
                        if output_directory:
                            # Якщо вказано вихідну папку, зберігаємо копію в нову папку
                            relative_path = os.path.relpath(subdir, directory)
                            output_subdir = os.path.join(output_directory, relative_path)
                            if not os.path.exists(output_subdir):
                                os.makedirs(output_subdir)
                            img.save(os.path.join(output_subdir, file))
                        else:
                            # Якщо вихідну папку не вказано, зберігаємо в тій самій
                            img.save(image_path)
                        
                    print(f"Зображення {image_path} успішно змінено")
                except Exception as e:
                    print(f"Не вдалося обробити {image_path}: {e}")

# Вкажіть шлях до папки, де знаходяться ваші зображення та підкаталоги
directory_path = 'dataset'
# Вкажіть шлях до вихідної папки, або залиште None для збереження в тій самій папці
output_directory = None
resize_images_in_directory(directory_path, target_size=(256, 256), output_directory=output_directory)
