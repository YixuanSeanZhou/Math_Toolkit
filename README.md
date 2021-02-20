# Math_Toolkit
This repo contains some tools that might be handy when doing math problems


## Install

In order to run the code in this repo, one need to run `pip -r requirements.txt`

## Tool List

### Algebraic Tools

#### Euclidean Algorithm
`euclidean_algorithm.py`:
    Implemented the euclidean algorithm with the calculation of Bezout's coeffs and gcd.
    Output:
    ```python
    {
        'input': (a, b),
        'gcd': gcd,
        'Bézout coefficients': (a's coeff, b's coeff),
        'quotients by the gcd:': (a's quotient, b's quotient)
    }
    ```

