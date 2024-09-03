import math

class SOM:

    def winner(self, weights, sample):
        C = [0, 0, 0]

        for i in range(len(sample)):
            C[0] = C[0] + math.pow((sample[i] - weights[0][i]), 2)
            C[1] = C[1] + math.pow((sample[i] - weights[1][i]), 2)
            C[2] = C[2] + math.pow((sample[i] - weights[2][i]), 2)

        min_distance = min(C)

        if min_distance == C[0]:
            return 0
        elif min_distance == C[1]:
            return 1
        else:
            return 2

    def update(self, weights, sample, J, alpha):
        for i in range(len(weights[0])):
            weights[J][i] = weights[J][i] + alpha * (sample[i] - weights[J][i])

        return weights

def main():

    T = [[0, 0 , 1, 0 ,0,1], [0, 0 , 1, 1 ,0,0], [0, 0 , 0, 1 ,1,0], [0, 0 , 1, 0 ,0,0],[0, 0 , 0, 0 ,1,1],[0, 0 , 0, 1 ,0,0]]

    m, n = len(T), len(T[0])

    weights = [[0.2, 0.6, 0.5, 0.9,0.3,0.7], [0.8, 0.4, 0.7, 0.3,0.2,0.5],[0.7, 0.3, 0.8, 0.6,0.4,0.1]]

    ob = SOM()

    epochs = 5  # Changed to 5 iterations
    alpha = 0.2

    for i in range(epochs):
        print(f"\nIteration {i+1}:")

        for j in range(m):

            sample = T[j]

            J = ob.winner(weights, sample)
            print(f"Winner cluster for sample {j+1}: {J} ")

            weights = ob.update(weights, sample, J, alpha)
            print(f"Updated weights after sample {j+1}: \n")
            for row in weights:
                print(row)

    s = [0, 0, 0, 1,0,0]
    J = ob.winner(weights, s)

    print("\nTest Sample s belongs to Cluster : ", J)
    print("\nTrained weights : \n\n", weights)

if __name__ == "__main__":
    main()
