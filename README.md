# FRACTRAN Python interpreter

This repo contains a FRACTRAN interpreter written in Python 3. FRACTRAN is an esoteric programming language created by John Conway in 1987. For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/FRACTRAN).

## Usage

```
python fractran.py code.txt [input] [additional optional arguments...]
```

Where `code.txt` is the path to the source code (format explained below) and `input` is the input to the program. If provided, it should be a positive integer. If not provided, the program will prompt the user to enter one (which should also be a positive integer).

The additional arguments are :
 - `-a` (or `--auto`) : does not prompt the user to press Enter between each output. Be careful if it is an infinite loop program, as it will print non-stop.

### Usage examples

`code.txt` is the file found in the `codes` folder.

```bash
> python code.txt 15
You must press enter after every output to continue the program.

15
20
6
8
```


```bash
> python fractran.py code.txt -a
Program input value (positive integer) ? 15

15
20
6
8
```

## Code format

A source code file should contain fractions of the form, where the numerator and denominator are positive integer, and the denominator is not zero :
```
<numerator>/<denominator>
```

They must be separated by spaces and can be on multiple lines. Every line starting with `#`, `!`, `/`, `;` or `%` will be considered as a comment.

## Code examples

The files found in the `codes` folder are all from either [the English](https://en.wikipedia.org/wiki/FRACTRAN) or [the French](https://fr.wikipedia.org/wiki/FRACTRAN) Wikipedia page on FRACTRAN.

Details:
 - `code.txt` : example code, which returns just 14 if the input is 14, and 15, 20, 6 and 8 if the input is 15.
 - `addition.txt` : takes as an input a number of the form $2^a3^b$ and outputs $3^{a+b}$.
 - `multiplication.txt` : takes as an input a number of the form $2^a3^b$ and outputs $5^{ab}$.
 - `euclidian_div.txt` : takes as an input a number of the form $2^a3^b11$ and outputs $5^q7^r$ where $a = bq+r$
 - `primes.txt` : takes 2 as an input, and outputs a sequence containing $2^p$ for all primes $p$ (and reciprocally, the exponent of a power of 2 in the sequence is either 1 or a prime).
 - `fibonacci.txt` : takes 3 as an input and outputs a sequence containing $2^{F_n}3^{F_{n+1}}$ for all $n$ where $F_n$ is the Fibonacci sequence (and reciprocally, if a number in the sequence is of the form $2^a3^b$, then $a$ and $b$ are successive terms of the Fibonacci sequence).
 - `syracuse.txt` : takes as an input a number of the form $2^N$ and outputs a sequence containing $2^{S^N_n}$ where $S^N_n$ is the reduced Syracuse sequence with initial term $N$ (reciprocally, the exponent of a power of 2 in the sequence is always $S^N_k$ for some k).

