import pandas as pd
import requests
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------------------------------------
# EASY-TO-CHANGE SETTINGS
# Change these values any time — no other code needs to be touched.
# ----------------------------------------------------------------------
CSV_PATH = "/Users/amarjeet/Desktop/Streamlit/learning-streamlit/tmdb_top_rated_movies.csv"    # path to your movies CSV
NUM_RECOMMENDATIONS = 5              # how many similar movies to show
TRENDING_COUNT = 10                  # how many movies in the "Trending Now" row
COLUMNS_PER_ROW = 5                  # poster grid width
APP_TITLE = "🎬 Movie Recommender"
APP_SUBTITLE = "Pick a movie you like — get similar ones based on plot, title & language."
ACCENT_COLOR = "#e50914"             # Netflix-style red, change to any hex color
POSTER_SIZE = "w342"                 # TMDB poster size: w92, w154, w185, w342, w500, original

# Get a free TMDB API key at https://www.themoviedb.org/settings/api
# and paste it below to enable real movie posters.
TMDB_API_KEY = "a0cb040b0b8ecebf9f845ebb878e3821"
# ----------------------------------------------------------------------

PLACEHOLDER_POSTER = "https://placehold.co/342x513/1a1d24/9aa0a6?text=No+Poster"

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: #0e1117; }}
    .movie-card {{
        background-color: #1a1d24;
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 10px;
        border-left: 4px solid {ACCENT_COLOR};
    }}
    .movie-title {{ font-size: 16px; font-weight: 700; color: white; margin-bottom: 2px; }}
    .movie-meta {{ color: #9aa0a6; font-size: 12px; margin-bottom: 6px; }}
    .movie-overview {{ color: #d0d3d8; font-size: 13px; line-height: 1.45; }}
    .rating-badge {{
        display: inline-block; background-color: {ACCENT_COLOR}; color: white;
        border-radius: 6px; padding: 1px 8px; font-weight: 700; font-size: 12px;
    }}
    .section-header {{ color: white; font-size: 22px; font-weight: 700; margin: 18px 0 10px 0; }}
    img {{ border-radius: 8px; }}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """Load and clean the movies dataset (mirrors the notebook's preprocessing)."""
    df = pd.read_csv(path)
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

    df1 = df.drop(columns=["adult", "original_title", "vote_count"], errors="ignore")
    df1.dropna(subset=["overview"], inplace=True)
    df1.drop_duplicates(keep="first", inplace=True)
    df1["release_date"] = df1["release_date"].ffill()
    df1.reset_index(inplace=True, drop=True)

    df1["data"] = df1["overview"] + " " + df1["title"] + " " + df1["original_language"]
    return df1


@st.cache_resource
def build_model(df1: pd.DataFrame):
    tfidf = TfidfVectorizer(stop_words="english", token_pattern="[a-zA-Z]{2,}")
    tf_vec = tfidf.fit_transform(df1["data"])
    return tf_vec


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id, api_key: str) -> str:
    """Look up a movie's poster on TMDB. Falls back to a placeholder on any failure."""
    if not api_key:
        return PLACEHOLDER_POSTER
    try:
        resp = requests.get(
            f"https://api.themoviedb.org/3/movie/{int(movie_id)}",
            params={"api_key": api_key},
            timeout=5,
        )
        data = resp.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/{POSTER_SIZE}{poster_path}"
    except Exception:
        pass
    return PLACEHOLDER_POSTER


def recommend(title: str, df1: pd.DataFrame, tf_vec, n: int = NUM_RECOMMENDATIONS) -> pd.DataFrame:
    idx_lookup = pd.Series(df1.index, index=df1["title"])
    movie_idx = idx_lookup[title]
    if isinstance(movie_idx, pd.Series):
        movie_idx = movie_idx.iloc[0]

    sim_scores = cosine_similarity(tf_vec[movie_idx], tf_vec).flatten()
    top_indices = sim_scores.argsort()[::-1][1 : n + 1]

    results = df1.iloc[top_indices].copy()
    results["similarity"] = sim_scores[top_indices]
    return results


def render_poster_grid(movies_df: pd.DataFrame, key_prefix: str, columns_per_row: int = COLUMNS_PER_ROW):
    """Renders posters in a grid; clicking a movie's button selects it."""
    rows = [movies_df.iloc[i : i + columns_per_row] for i in range(0, len(movies_df), columns_per_row)]
    for row_df in rows:
        cols = st.columns(columns_per_row)
        for col, (_, movie) in zip(cols, row_df.iterrows()):
            with col:
                poster_url = fetch_poster(movie["id"], TMDB_API_KEY)
                st.image(poster_url, width="stretch")
                if st.button(movie["title"], key=f"{key_prefix}_{movie['id']}", width="stretch"):
                    st.session_state.selected_movie = movie["title"]
                    st.rerun()


# ---- Load data & model ----
try:
    df1 = load_data(CSV_PATH)
    tf_vec = build_model(df1)
    data_loaded = True
except FileNotFoundError:
    data_loaded = False

st.title(APP_TITLE)
st.caption(APP_SUBTITLE)

if not data_loaded:
    st.warning(f"Couldn't find **{CSV_PATH}**. Upload your CSV below to continue.")
    uploaded = st.file_uploader("Upload movies CSV", type=["csv"])
    if uploaded is not None:
        with open(CSV_PATH, "wb") as f:
            f.write(uploaded.getbuffer())
        st.rerun()
    st.stop()

if not TMDB_API_KEY:
    st.info(
        "Posters are showing placeholders. Get a free key at "
        "themoviedb.org/settings/api and paste it into TMDB_API_KEY at the top of app.py.",
        icon="🖼️",
    )

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# ---- Trending Now ----
st.markdown('<div class="section-header">🔥 Trending Now</div>', unsafe_allow_html=True)
trending_df = df1.sort_values("popularity", ascending=False).head(TRENDING_COUNT)
render_poster_grid(trending_df, key_prefix="trend")

st.write("")

# ---- Search ----
st.markdown('<div class="section-header">🔍 Search a movie</div>', unsafe_allow_html=True)
titles = sorted(df1["title"].unique())
current_index = titles.index(st.session_state.selected_movie) if st.session_state.selected_movie in titles else None

selected_from_box = st.selectbox(
    "Choose a movie you like:",
    options=titles,
    index=current_index,
    placeholder="Start typing a movie title...",
)
if selected_from_box:
    st.session_state.selected_movie = selected_from_box

num_results = st.slider("Number of recommendations", min_value=3, max_value=15, value=NUM_RECOMMENDATIONS)

selected_title = st.session_state.selected_movie

if selected_title:
    with st.spinner("Finding similar movies..."):
        results = recommend(selected_title, df1, tf_vec, n=num_results)

    st.markdown(
        f'<div class="section-header">Because you liked <i>{selected_title}</i></div>',
        unsafe_allow_html=True,
    )
    render_poster_grid(results, key_prefix="rec")

    with st.expander("Show details"):
        for _, row in results.iterrows():
            release_year = row["release_date"].year if pd.notnull(row["release_date"]) else "N/A"
            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">{row['title']}</div>
                    <div class="movie-meta">
                        {release_year} &nbsp;•&nbsp; {row['original_language'].upper()} &nbsp;•&nbsp;
                        <span class="rating-badge">★ {row['vote_average']:.1f}</span>
                        &nbsp;•&nbsp; match {row['similarity']*100:.0f}%
                    </div>
                    <div class="movie-overview">{row['overview'][:220]}{'...' if len(row['overview']) > 220 else ''}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
else:
    st.info("Click a trending poster above, or search for a movie, to get recommendations.")

with st.expander("Browse all movies in the dataset"):
    st.dataframe(
        df1[["title", "release_date", "original_language", "vote_average", "popularity"]].sort_values(
            "popularity", ascending=False
        ),
        width="stretch",
        hide_index=True,
    )
