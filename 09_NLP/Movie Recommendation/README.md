# Movie Recommender

A content-based movie recommendation system built with Python, NLP, and Streamlit.

I started this project by exploring and cleaning the TMDB movie dataset in `Untitled.ipynb`. After performing EDA and preparing the movie data, I used TF-IDF and Cosine Similarity to build the recommendation system and then turned it into an interactive Streamlit application.

## What I Did

* Performed EDA on the movie dataset
* Cleaned and prepared the data
* Combined movie overview, title, and language for text processing
* Converted movie text into numerical vectors using **TF-IDF**
* Used **Cosine Similarity** to find similar movies
* Built an interactive **Streamlit** web app
* Integrated **TMDB API** to display movie posters
* Added trending movies and movie search

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* TMDB API
* TF-IDF
* Cosine Similarity


## Files

* `Untitled.ipynb` – EDA, data cleaning, exploration, and model preparation
* `app.py` – Final Streamlit movie recommendation application

## How It Works

When a movie is selected, the application compares its TF-IDF vector with the vectors of other movies using cosine similarity. The movies with the highest similarity scores are then shown as recommendations.

## What I Learned

This project helped me understand how NLP techniques can be used in a real application, especially how text can be converted into numerical vectors and compared to build a recommendation system.


