# Movie Similarity Finder

This is a Python program that uses spaCy's word embeddings to find the most similar movie to a given movie description. It reads a list of movie descriptions from "movies.txt", processes the input description using spaCy's pre-trained word embeddings, and calculates the similarity between the input description and each movie description. The program then returns the movie with the highest similarity score.

## Introduction

Word embeddings are dense vector representations of words that capture semantic relationships between words. In this program, we leverage spaCy's pre-trained word embeddings to compute the similarity between a given movie description and a list of movie descriptions.

## Dependencies

Before running the program, make sure you have the spaCy library and the "en_core_web_md" model installed:

```bash
pip install spacy
python -m spacy download en_core_web_md
```

## How the Program Works

1. Import the spaCy library and load the "en_core_web_md" model:

The program starts by importing the spaCy library and loading the medium-sized English model "en_core_web_md," which includes word vectors.

2. Define the function `find_similar_movie(description)`:

The function takes a movie description as input and returns the most similar movie from the list in "movies.txt".

3. Read and process the movie descriptions:

The program reads the movie descriptions from "movies.txt" and tokenizes them using spaCy's NLP pipeline. It then converts each description into a spaCy Doc object, which includes word embeddings.

4. Compute similarity scores:

The function `find_similar_movie` computes the similarity between the input movie description and each movie description in the list using spaCy's `.similarity()` method. The similarity scores are stored in a list.

5. Find the most similar movie:

The function determines the index of the movie description with the highest similarity score and returns the corresponding movie name from the list.

## How to Use

1. Ensure you have Python and the spaCy library with the "en_core_web_md" model installed on your machine.

2. Create a text file named "movies.txt" and populate it with movie descriptions, each on a separate line. (Or use mine to test)

3. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/wasim-jussab/movie-similarity-finder.git
```

4. Change to the project directory:

```bash
cd movie-similarity-finder
```

5. Run the program:

```bash
python movie_similarity.py
```

6. The program will process the input movie description and calculate the similarity with each movie in the "movies.txt" file. It will then return the most similar movie.

## Contributing

If you'd like to contribute to this project or report any issues, please feel free to open a pull request or submit an issue on the GitHub repository.

---
Created by [Wasim Jussab](https://github.com/wasim-jussab)
```
