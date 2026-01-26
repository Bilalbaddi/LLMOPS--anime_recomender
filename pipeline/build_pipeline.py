import os
from pathlib import Path

from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logging import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

# Get project root directory (parent of pipeline folder)
PROJECT_ROOT = Path(__file__).parent.parent

def main():
    try:
        logger.info("Starting to build pipeline...")

        data_dir = PROJECT_ROOT / "data"
        loader = AnimeDataLoader(str(data_dir / "anime_with_synopsis.csv"), str(data_dir / "anime_updated.csv"))
        processed_csv = loader.load_and_process()

        logger.info("Data  loaded and processed...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store Built sucesfully....")

        logger.info("Pipelien built sucesfuly....")
    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise CustomException("Error during pipeline " , e)
    
if __name__=="__main__":
     main()