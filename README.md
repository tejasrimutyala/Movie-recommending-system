Movie Recommender System
A content-based movie recommendation system built using Python and Streamlit. This application suggests similar movies based on your selection by analyzing metadata such as genres, keywords, cast, and crew. It presents recommendations interactively with movie posters and titles.

Features
Select movies via a searchable dropdown menu

Displays posters and titles with a clean layout

Adjustable number of recommendations using a slider

Fast recommendations powered by cosine similarity

Robust error handling for API requests and data loading

Technologies Used
Python – Core programming language

Streamlit – Web application framework

Pandas – Data manipulation and analysis

Pickle – Serialization for pre-computed similarity data

TMDB API – Movie metadata and poster retrieval

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/sriramp16/movie-recommender-system.git
cd movie-recommender-system
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy
Edit
venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Ensure the following files are available:

movies_dict.pkl

similarity.pkl
(Download or generate them using the provided scripts.)

Dataset
The dataset includes:

Movie titles and TMDB IDs

Genres and keywords

Metadata used for computing similarity

The similarity matrix is pre-computed and stored in similarity.pkl.

Usage
Run the application:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to http://localhost:8501

Search or select a movie, adjust the number of recommendations using the slider, and click "Show Recommendation"

Working Process
User selects a movie from the dropdown

The system identifies the selected movie's index in the dataset

Retrieves pre-computed similarity scores

Fetches poster images via the TMDB API

Displays results in a responsive layout

Future Enhancements
Genre-based filtering

Integration of user ratings and feedback

Support for multi-select movie comparison

Personalized recommendations

Regional cinema support (e.g., Telugu movies)

Author
Tejasri Mutyala

Acknowledgements
The Movie Database (TMDB) for the API

Streamlit for the application framework
