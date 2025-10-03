from src.vector_store import VectorStoreBuilder
from src.recommender import MovieRecommender
from config.config import GROQ_API_KEY, MODEL_NAME

from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class MovieRecommendationPipeline:
    def __init__(self, persist_dir = "chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="" ,persist_directory = persist_dir)
            retriever = vector_builder.load_vectorstore().as_retriever()
            self.recommender = MovieRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Recommendation Pipeline Initialized Successfully")
        
        except Exception as e:
            logger.error("Error initializing Recommendation Pipeline")
            raise CustomException("Error During pipeline initialization", e) 
    
    def recommend(self, query: str):
        try:
            logger.info("Recieved a query {query}")

            recommendation = self.recommender.get_recommendations(query)

            logger.info("Recommendation generated successfully")
            return recommendation

        except Exception as e:
            logger.error("Error generating recommendation")
            raise CustomException("Error During recommendation generation", e)
    
    





