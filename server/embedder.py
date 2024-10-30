from sentence_transformers import SentenceTransformer
import logging
from math import sqrt

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

# The image or text encoding model.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def create_embedding(data):
    #logger.debug(f"Encoding data {data}")
    return model.encode(data)

# Calcuate the Euclidean distance ("distance measured by a ruler") between 2 points. The true
# Euclidean distance involves a square root but since the relative magnitude is all that is
# desired, this can be skipped.
def squaredEuclidean(vect1, vect2):
    magnitude = 0.0
    for i in range(len(vect1)):
        length = vect1[i] - vect2[i]
        magnitude += length * length

    return magnitude

# Calculate the cosine similarity of 2 vectors. The result will be a number in the range [-1, 1]
# with larger numbers being more similar. This method takes into account on the direction of the 
# vectors, not the magnitude. It measures the angle between the vectors seen from an observer
# standing at the origin
def cosineSimilarity(vect1, vect2):
    dotProduct = 0.0
    magnitude1 = 0.0
    magnitude2 = 0.0
    for i in range(len(vect1)):
        dotProduct += vect1[i] * vect2[i]
        magnitude1 += vect1[i] * vect1[i]
        magnitude2 += vect2[i] * vect2[i]

    return dotProduct / sqrt(magnitude1 * magnitude2)


# Code to access
if __name__ == '__main__':
    sentence = "Dont all shout at once."
    vector = create_embedding(sentence)
    print(vector, len(vector))
