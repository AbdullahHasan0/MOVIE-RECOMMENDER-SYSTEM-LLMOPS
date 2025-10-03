from src.dataloader import MovieDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the pipeline")

        # Step 1: Load Data
        loader = MovieDataLoader(orignal_csv="data/movies.csv", processed_csv="data/movies_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info(f"Loaded and processed movies")

        # Step 2: Build Vector Store
        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store built and saved successfully...")

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.error("Error in the pipeline")
        raise CustomException("Error During pipeline execution", e)
    

if __name__=="__main__":
    main()
