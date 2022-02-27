from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
def similarity(anime):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(anime['Joined'])
    cosine_sim = cosine_similarity(count_matrix.toarray())
    return cosine_sim