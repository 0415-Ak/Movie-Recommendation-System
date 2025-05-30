# <font size="6">Movie Recommendation System</font>

<font size="4">A simple movie recommendation system that suggests movies based on movie content and features using machine learning and NLP techniques.</font>

## <font size="5">🎬 Overview</font>

<font size="3">This project analyzes movie data from TMDB (The Movie Database) to recommend similar movies to users. It uses text vectorization and content-based filtering to find movies with similar characteristics.</font>

## <font size="5">✨ Features</font>

<font size="3">
- Movie similarity analysis based on content
- Text processing using NLP vectorization techniques
- Interactive web interface for easy movie search
- Real-time movie recommendations
- Movie details display with posters and information
</font>

## 🛠️ Technologies Used

- **Python** - Main programming language
- **Pandas** - Data preprocessing and manipulation
- **Matplotlib** - Data visualization
- **Scikit-learn** - Machine learning and vectorization
- **Streamlit** - Web interface development
- **NumPy** - Numerical computations

## 📊 Dataset

- **Source**: TMDB (The Movie Database) dataset from Kaggle
- **Content**: Movie titles, overviews, genres, cast, crew, and other metadata
- **Size**: Contains thousands of movie records with detailed information

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/0415-Ak/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install required packages**
   ```bash
   pip install pandas matplotlib scikit-learn streamlit numpy
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and go to `http://localhost:8501`

## 💻 How It Works

### 1. Data Preprocessing
- Loaded TMDB dataset from Kaggle
- Cleaned and processed movie data using Pandas
- Handled missing values and data inconsistencies
- Visualized data patterns using Matplotlib

### 2. NLP Text Processing
- Applied vectorization techniques to convert text data into numerical format
- Processed movie overviews, genres, and other textual features
- Used TF-IDF or similar vectorization methods for text analysis

### 3. Recommendation Engine
- Calculated similarity between movies based on processed features
- Built content-based filtering system
- Generated recommendations for selected movies

### 4. User Interface
- Created simple and intuitive interface using Streamlit
- Added movie search functionality
- Displayed recommendations with movie details

## 📁 Project Structure

```
movie-recommendation-system/
│
├── app.py                 # Main Streamlit application
├── data/                  # TMDB dataset files
├── preprocessing.py       # Data cleaning and processing
├── recommendation.py      # Recommendation logic
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🎯 Usage

1. Run the Streamlit app
2. Select or search for a movie from the dropdown/search box
3. Click "Get Recommendations" button
4. View similar movies with their details and posters
5. Explore different movies to get varied recommendations

## 📈 Features of the System

- **Content-Based Filtering**: Recommends movies based on movie content similarity
- **Text Vectorization**: Converts movie descriptions into numerical vectors
- **Interactive Interface**: Easy-to-use web interface built with Streamlit
- **Real-time Results**: Instant recommendations upon movie selection

## 🔧 Key Components

- **Data Loading**: Reads TMDB dataset from CSV files
- **Text Processing**: Vectorizes movie overviews and genres
- **Similarity Calculation**: Computes cosine similarity between movies
- **Recommendation Generation**: Returns top similar movies
- **Web Interface**: Streamlit-based user interface

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Your Name**
- GitHub: [@0414-Ak](https://github.com/0415-Ak)

## 🙏 Acknowledgments

- TMDB for providing the comprehensive movie dataset
- Kaggle for hosting the dataset
- Streamlit community for the amazing web framework
