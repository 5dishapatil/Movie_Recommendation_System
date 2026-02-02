# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests movies similar to the one selected by the user. The application recommends the top 5 movies along with their posters fetched using the OMDB API.

## 🛠️ Tech Stack
* **Python**: Core programming language.
* **Streamlit**: For building the web interface.
* **Pandas**: For data manipulation.
* **Scikit-learn**: For vectorization and calculating cosine similarity.
* **OMDB API**: To fetch movie posters dynamically.

## 🧠 How It Works
This system uses **Content-Based Filtering**:
1.  **Data Cleaning**: Merged datasets (Movies + Credits) and selected key tags (genres, keywords, cast, crew).
2.  **Vectorization**: Used `CountVectorizer` to convert text tags into vectors.
3.  **Similarity**: Calculated **Cosine Similarity** between vectors to find the closest matches.

## 📂 Project Structure
├── data/ # Dataset files (Movies and Credits)
├── model/ # Saved pickle files (movie_dict.pkl, similarity.pkl)
├── Jupyter Notebook for EDA and prototyping
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── Procfile # Configuration for Heroku/Render deployment
├── setup.sh # Shell script for environment setup
└── README.md # Project documentation

## ⚡ How to Run Locally

### 1. Clone the Repository

git clone [https://github.com/5dishapatil/Movie_Recommendation_System.git](https://github.com/5dishapatil/Movie_Recommendation_System.git)
cd Movie_Recommendation_System

### 2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Setup Git LFS (Important)
This project uses large files for the similarity matrix.

git lfs install
git lfs pull

### 5. Run the App

streamlit run app.py

## 🔑 Configuration
To fetch movie posters, you need a OMDB API Key.

Generate an API Key.

Paste your API key inside app.py in the fetch_poster function.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## 📝 License
This project is open-source and available under the MIT License.
