def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        distance += p[i] != q[i] # python is handy in it's dynamically typed ways :)
    return distance