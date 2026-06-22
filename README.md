# 🎬 Movie Recommendation System

A content-based movie recommender built with **Streamlit**, powered by cosine similarity and the **TMDB API** for live poster fetching.

🔗 **Live Demo:** [movie-recommender-app1.streamlit.app](https://movie-recommender-app1.streamlit.app/)

---

## ✨ Features

- 🔍 Search from thousands of movies
- 🎯 Content-based filtering using cosine similarity
- 🖼️ Live movie posters fetched from TMDB
- ⚡ Parallel API calls for fast poster loading
- 💾 Cached data loading for snappy performance

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| ML | scikit-learn (cosine similarity) |
| Data | pandas, numpy |
| API | TMDB API |
| Deployment | Streamlit Cloud |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/subhanu06/movie-recommender-app.git
cd movie-recommender-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your TMDB API key

Create a `.env` file in the root directory:

```
TMDB_API_KEY=your_api_key_here
```

Get a free API key at [themoviedb.org](https://www.themoviedb.org/settings/api).

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
movie-recommender-app/
├── app.py                  # Main Streamlit app
├── movies.pkl              # Preprocessed movie metadata
├── similarity.npz          # Compressed cosine similarity matrix
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
└── README.md
```

---

## 🧠 How It Works

1. Movie metadata (genres, cast, crew, keywords) is vectorized using **CountVectorizer**
2. **Cosine similarity** is computed between all movie vectors
3. When you pick a movie, the top 5 most similar movies are returned
4. Posters are fetched **in parallel** from the TMDB API using `ThreadPoolExecutor`

---

## 📦 Requirements

```
streamlit
requests
python-dotenv
numpy
pandas
scikit-learn
```

---

## 🙏 Acknowledgements

- Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) on Kaggle
- Poster data: [The Movie Database (TMDB)](https://www.themoviedb.org/)
