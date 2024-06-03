import os
import zipfile

def extract_zip(zip_file_path, extract_to_folder):
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)

    print(f"Extracted files to {extract_to_folder}")

def save_files(extracted_folder, data_folder):
    
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    
    for file_name in os.listdir(extracted_folder):
        full_file_name = os.path.join(extracted_folder, file_name)
        if os.path.isfile(full_file_name):
            os.rename(full_file_name, os.path.join(data_folder, file_name))
    
    print(f"Saved files to {data_folder}")

def ingest_data(zip_file_path, data_folder):
    extract_to_folder = "temp_extracted_files"
    
   
    extract_zip(zip_file_path, extract_to_folder)
    
    
    save_files(extract_to_folder, data_folder)
    
    
    if os.path.exists(extract_to_folder):
        os.rmdir(extract_to_folder)


zip_file_path = 'data.zip'
data_folder = 'data'
ingest_data(zip_file_path, data_folder)



