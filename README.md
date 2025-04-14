# 🎬 Movie Recommender System

A content-based movie recommendation system built with Streamlit and Python. This application recommends similar movies based on your selection, displaying movie posters and titles in an interactive interface.

## 📋 Features

- Search or select movies from a dropdown menu
- Adjust number of recommendations via slider control
- View movie posters and titles with clean alignment
- Fast content-based recommendations using similarity metrics
- Error handling for API requests and data loading

## 🛠 Technologies Used

- *Python*: Core programming language
- *Streamlit*: Web application framework
- *Pandas*: Data manipulation and analysis
- *Pickle*: Data serialization for storing pre-computed results
- *TMDB API*: Movie data and poster images

## 🚀 Installation

1. Clone the repository:
   
   git clone https://github.com/sriramp16/movie-recommender-system.git
   cd movie-recommender-system
   

2. Create a virtual environment:
   
   python -m venv venv
   

3. Activate the virtual environment:
   - Windows: venv\Scripts\activate
   - macOS/Linux: source venv/bin/activate

4. Install required packages:
   
   pip install -r requirements.txt
   

5. Download the required pickle files (movies_dict.pkl and similarity.pkl) or generate them using the provided scripts.

## 📊 Dataset

The system uses a dataset containing movie information including:
- Movie titles
- Movie IDs (TMDB)
- Genres
- Other metadata for computing similarities

The similarity between movies is pre-computed and stored in the similarity.pkl file.

## 🔧 Usage

1. Run the Streamlit application:
   
   streamlit run app.py
   

2. Open your browser and navigate to http://localhost:8501

3. Select a movie from the dropdown or type to search

4. Adjust the number of recommendations using the slider

5. Click "Show Recommendation" to get personalized movie suggestions

## 🔄 Working Process

1. User selects a movie from the dropdown menu
2. System finds the selected movie's index in the dataset
3. Pre-computed similarity scores are used to find similar movies
4. TMDB API is queried to fetch movie posters
5. Results are displayed in a responsive grid layout

## 🔮 Future Enhancements

- Genre filtering
- User ratings and feedback
- Multi-select movie comparison
- Personalized recommendations based on user preferences
- Support for regional cinema including Telugu movies


## 👤 Author

Tejasri Mutyala

## 🙏 Acknowledgements

- The Movie Database (TMDB) for providing the API
- Streamlit for the awesome framework**
