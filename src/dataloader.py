import pandas as pd

class MovieDataLoader:
    def __init__(self, orignal_csv: str, processed_csv: str):
        self.orignal_csv = orignal_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.orignal_csv, encoding = "utf-8", on_bad_lines='skip').dropna()
        required_columns = {"title","backdrop_path","overview","genres"}
        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        df["combined_info"] = (
            "Title: " + df["title"]+ ".. Overview: " + df["overview"] + ".. Genres: " + df["genres"] + ".. Image_Path: https://image.tmdb.org/t/p/w500/"+ df["backdrop_path"].astype(str) 
        )
    
        df[['combined_info']].to_csv(self.processed_csv, index = False, encoding = "utf-8")

        return self.processed_csv

