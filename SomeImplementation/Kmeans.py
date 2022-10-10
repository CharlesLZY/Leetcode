import numpy as np
import random

X = np.random.rand(10, 2)
K = 3
r = random.sample(range(9), K)

centroids = [X[i] for i in r]

def converge(centroids1, centroids2):
    for i in range(len(centroids1)):
        if centroids1[i].all() != centroids2[i].all():
            return False
    return True

while True:
    clusters = [[] for _ in range(K)]
    for x in X:
        label = 0
        minDist = float("inf")
        for k in range(K):
            d = np.linalg.norm(x-centroids[k])
            if d < minDist:
                minDist = d
                label = k
        clusters[label].append(x)

    ### new centroids
    newCentroids = []
    for k in range(K):
        meanX = np.mean([clusters[k][i][0] for i in range(len(clusters[k]))])
        meanY = np.mean([clusters[k][i][1] for i in range(len(clusters[k]))])
        newCentroids.append(np.array([meanX, meanY]))

    

    if converge(newCentroids, centroids):
        centroids = newCentroids
        break
    else:
        centroids = newCentroids

print(centroids)
