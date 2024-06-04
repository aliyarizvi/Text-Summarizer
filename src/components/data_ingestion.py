import os
import urllib.request as request
import zipfile
from src.utils import get_size
from src.logger import logging
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str = os.path.join("data")
    source_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/samsumdata.zip"
    local_data_file: str = os.path.join(root_dir, "data.zip")
    unzip_dir: str = os.path.join(root_dir)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig): 
        self.config = config
    
    def download_file(self): 
        os.makedirs(self.config.root_dir, exist_ok=True)
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

if __name__ == '__main__':
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config) 
    #data_ingestion.download_file()
    data_ingestion.extract_zip_file() 