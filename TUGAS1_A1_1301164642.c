#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    float x1;
    float x2;
    float E;
    float x1_best;
    float x2_best;
    float E_best;
    x1 = -10 + (rand() % 20);
    x2 = -10 + (rand() % 20);
    E = -(sin(x1)*cos(x2)+(4/5)*exp(1-sqrt(x1*x1+x2*x2)));
    x1_best = x1;
    x2_best = x2;
    E_best = E;
    printf("==========         awal        ==========\n");
    printf("x1 = %f\n", x1);
    printf("x2 = %f\n", x2);
    printf("Best_so_far = %f, %f\n", x1_best, x2_best);
    printf("E_best = %f\n", E_best);
    printf("=========================================\n\n\n");

    float T = 1000;
    while (T>=0) {
        printf("=========================================\n");
        float x1b, x2b;
        x1b = -10 + (rand() % 20);
        x2b = -10 + (rand() % 20);
        printf("x1 baru = %f\n", x1b);
        printf("x2 baru = %f\n", x2b);
        float Eb = -(sin(x1b)*cos(x2b)+(4/5)*exp(1-sqrt(x1b*x1b+x2b*x2b)));
        printf("E baru = %f\n", Eb);
        float deltaE = Eb - E;
        printf("delta E = %f\n", deltaE);
        if (deltaE < 0) {
            x1 = x1b;
            x2 = x2b;
            E = Eb;
            if (Eb < E_best) {
                x1_best = x1;
                x2_best = x2;
                E_best = E;
                printf("\n\nBest_so_far = %f, %f\n", x1_best, x2_best);
                printf("E_best = %f\n", E_best);
            }
        } else {
            float p = exp(-deltaE/T);
            double r = (double)rand() / (double)RAND_MAX;
            if (r < p) {
                x1 = x1b;
                x2 = x2b;
                E = Eb;
            }
        }
        printf("=========================================\n\n\n");
        float deltaT = 0.1;
        T = T-deltaT;
    }
    printf("\n\nHasil akhir : \n");
    printf("Best_so_far = %f, %f\n", x1_best, x2_best);
    printf("E best = %f\n", E_best);
}
