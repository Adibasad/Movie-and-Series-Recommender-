# Movie-and-Series-Recommender-System

Welcome to the Movie Recommender System with Content-Based Filtering ! This project is designed to provide personalized movie recommendations based on the content of the movies you enjoy. The system utilizes machine learning techniques to suggest movies that are similar in content to the ones you like.

## How it Works

The movie recommender system employs a content-based filtering approach, specifically utilizing cosine similarity. Here's a brief overview of how the system works:

1. **Data Collection and Preprocessing:** Movie data, including attributes like genre, plot summary, and cast, is collected and preprocessed. This data forms the basis for understanding the content of each movie.

2. **Feature Extraction:** Textual data such as plot summaries are transformed into numerical representations using techniques like TF-IDF (Term Frequency-Inverse Document Frequency).

3. **Cosine Similarity:** Cosine similarity is used to calculate the similarity between movies based on their feature vectors. This measures the cosine of the angle between the vectors, indicating how closely aligned the movies' content is.

4. **Recommendation Generation:** When a user provides the system with a movie they enjoyed, the system calculates the cosine similarity between that movie's features and all other movies in the database. It then recommends movies with the highest cosine similarity scores.

5. **API with Flask:** The system provides a user-friendly interface through a Flask API. Users can input the title of a movie they like, and the API responds with a list of recommended movies.
  
6. **Streamlit GUI:** This version features a Streamlit-based graphical user interface with the Flask API for ease. Users can input the title of a movie they enjoyed through a web-based interface.

## Getting Started

To run the Movie Recommender System on your local machine, follow these steps:

1. **Clone the Repository:** Start by cloning this repository to your local machine.

2. **Install Dependencies:** Navigate to the project directory and install the required dependencies using the following command:
   
   ```
   pip install -r requirements.txt
   ```

3. **Run the App:** Launch the Flask app by running the following command:
   
   ```
   python app.py
   ```

4. **Access the API:** Once the app is running, open your web browser and navigate to `http://localhost:5000`. You will be greeted with a simple user interface where you can input the title of a movie you like.

5. **Get Recommendations:** Enter the title of a movie you enjoyed and hit "Submit." The app will then provide you with a list of recommended movies based on the content of the movie you entered.

## Customization

You can customize and enhance this system in various ways, such as:

- **Improving Data:** Add more movie attributes like directors, release years, and user ratings for a richer recommendation experience.

- **Advanced Techniques:** Explore other content-based filtering techniques or even hybrid approaches that combine content-based and collaborative filtering.

- **User Experience:** Enhance the user interface by incorporating a frontend framework like React or Vue.js.

## Acknowledgments

This project was developed by Adiba Sadaf as a demonstration of content-based filtering using cosine similarity and API development with Flask.

## Disclaimer

This project is for educational and demonstration purposes only. The movie data used and the quality of recommendations may not be suitable for production-level use.

Feel free to reach out to adibasadaf300@gmail.com with any questions, feedback, or suggestions. Happy Coding!
