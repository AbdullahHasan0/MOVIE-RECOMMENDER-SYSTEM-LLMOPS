import streamlit as st
from pipeline.pipeline import MovieRecommendationPipeline
from dotenv import load_dotenv


st.set_page_config(page_title="Movie Recommendation System", page_icon=":clapper:", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return MovieRecommendationPipeline()

pipeline = init_pipeline()

st.title("Movie Recommendation System :clapper:")

query = st.text_input("Enter your movie preferences:", "")

if query:
    with st.spinner("Finding recommendations for you..."):
        recommendations = pipeline.recommend(query)
        st.markdown("### Recommendations:")
        st.write(recommendations)
    