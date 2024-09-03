#include <stdio.h>

void transpose(int input[][15], int output[][5]) {
    for(int i = 0; i < 15; i++) {
        for(int j = 0; j < 5; j++) {
            output[j][i] = input[i][j];
        }
    }
}

int main() {
    int A[5][3] = {{1,1,1},{1,-1,1},{1,1,1},{1,-1,1},{1,-1,1}};
    int B[5][3] = {{1,1,1},{1,-1,1},{1,1,1},{1,-1,1},{1,1,1}};
    int C[5][3] = {{1,1,1},{1,-1,-1},{1,-1,-1},{1,-1,-1},{1,1,1}};
    int D[5][3] = {{1,1,1},{1,-1,1},{1,-1,-1},{1,-1,1},{1,1,1}};
    int E[5][3] = {{1,1,1},{1,-1,-1},{1,1,1},{1,-1,-1},{1,1,1}};

    int patterns[5][15];
    int transposeMatrix[15][5];
    int weights[15][15] = {0}; 
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 3; j++) {
            patterns[i][j] = A[i][j];
            patterns[i][j+3] = B[i][j];
            patterns[i][j+6] = C[i][j];
            patterns[i][j+9] = D[i][j];
            patterns[i][j+12] = E[i][j];
        }
    }

    transpose(patterns, transposeMatrix);

    int recallPattern[15];

    printf("Enter a 15-element pattern (1 or -1): ");
    for(int i = 0; i < 15; i++) {
        scanf("%d", &recallPattern[i]);
    }

    int closestMatchIndex = -1;
    int maxMatches = -1;

    for(int i = 0; i < 5; i++) {
        int activation = 0;
        for(int j = 0; j < 15; j++) {
            activation += recallPattern[j] * weights[i][j];
        }
        if (activation > maxMatches) {
            maxMatches = activation;
            closestMatchIndex = i;
        }
    }

    printf("Recalled pattern: ");
    for(int i = 0; i < 15; i++) {
        printf("%d ", recallPattern[i]);
    }
    printf("\n");

    // Print the closest resembled letter
    switch (closestMatchIndex) {
        case 0:
            printf("Closely resembled letter: A\n");
            break;
        case 1:
            printf("Closely resembled letter: B\n");
            break;
        case 2:
            printf("Closely resembled letter: C\n");
            break;
        case 3:
            printf("Closely resembled letter: D\n");
            break;
        case 4:
            printf("Closely resembled letter: E\n");
            break;
        default:
            printf("No resemblance found.\n");
            break;
    }

    return 0;
}
