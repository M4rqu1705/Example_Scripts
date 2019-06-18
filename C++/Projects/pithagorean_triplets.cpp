/* Tripletas pitagóricas en C++ */
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool are_coprime(int a, int b);
bool previous_factors(int a, int b);

vector<vector<int>> factors;
int last_factor = 10;
int result = 0;

int main(void){

    for(int a=1; a<last_factor; a++){
        for(int b=1; b<last_factor; b++){

            // c = sqrt(a^2 + b^2)
            result = pow((pow(a, 2) + pow(b, 2)), 0.5);

            // Check if 
            if(result == int(result) &&         // The result is a whole number
                    are_coprime(a,b) &&         // a and b are coprime
                    !previous_factors(a,b)){    // a and b are not repeated

                // Prepare a temporary vector
                vector<int> temp{a,b};

                // To then store those factors inside the factors vector
                factors.push_back(temp*);

                // Print out the pithagorean triplet
                cout<< "(" << a << ", " << b << ", " << result << ")"<<endl;
            }
        }
    }

    return(0);
}


bool are_coprime(int a, int b){

    // Check if both are even
    if(a%2==0 && b%2 == 0)
        return(false);

    // Check the other possible uneven factors
    for(int c = 3; c<=min(a,b); c+=2)
        if(a%c==0 && b%c==0)
            return(false);

    // Every test passed, so numbers are coprime
    return(true);
}



bool previous_factors(int a, int b){

    // Check every element of the factors vector
    for(int c=0; c<factors.size(); c++){

        // If a and b are both found in the same factor element, return true
        if((factors[c][0] == a || factors[c][1] == a) &&
                (factors[c][0] == b || factors[c][1] == b))
            return(true);
    }

    // a and b were not found in the same factor element
    return(false);
}
