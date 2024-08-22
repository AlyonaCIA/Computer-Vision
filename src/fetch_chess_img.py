import zipfile
import os

# Definir la ruta del archivo ZIP y el directorio de destino
zip_path = '../data/chessman-image-dataset.zip'
extract_dir = 'data/chessman-image-dataset'

# Crear el directorio de destino si no existe
os.makedirs(extract_dir, exist_ok=True)

# Descomprimir el archivo
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"Dataset descomprimido en {extract_dir}")
