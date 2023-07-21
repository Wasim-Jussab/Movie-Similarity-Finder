import spacy

nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    movies = []
    with open('movies.txt', 'r') as file:
        movies = file.read().splitlines()

    similarity_scores = []
    target_doc = nlp(description)
    
    for movie in movies:
        movie_doc = nlp(movie)
        similarity = target_doc.similarity(movie_doc)
        similarity_scores.append(similarity)
    
    max_similarity_index = similarity_scores.index(max(similarity_scores))
    return movies[max_similarity_index]

# Example usage
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print("Next movie to watch:", similar_movie)
