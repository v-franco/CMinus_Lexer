from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
u = np.array([[1,2,3,4]])
v = np.array([[1,2,3,4]])
print(cosine_similarity(u,v))
