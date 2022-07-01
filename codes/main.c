#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("gau.dat", 1000000);

//Mean of uniform
printf("mean(U) = %lf\n",mean("uni.dat"));

//Variance of uniform (U)
printf("var(U) = %lf\n",variance("uni.dat"));

//Mean of X
printf("mean(X) = %lf\n",mean("gau.dat"));

//Variance of X
printf("variance(X) = %lf\n",variance("gau.dat"));

// V = -2ln(1-U)
//Generating V
other("other.dat", 1000000);

// //Mean of V
// printf("mean(V) = %lf\n",mean("other.dat"));

// //Variance of V
// printf("variance(V) = %lf\n",variance("other.dat"));


//cdf expression 1 - e^{-x/2} x >0, 0 otherwise => theoretical

return 0;

}
