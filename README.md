# FRACTRAN Python interpreter

This repo contains a FRACTRAN interpreter written in Python 3. FRACTRAN is an esoteric programming language created by John Conway in 1987. For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/FRACTRAN).

## Usage

```
python fractran.py code.txt [input] [additional optional arguments...]
```

Where `code.txt` is the path to the source code (format explained below) and `input` is the input to the program. If provided, it should be a positive integer or a sequence of positive integers. If not provided, the program will prompt the user to enter it (which should also be a positive integer or a sequence).

The additional arguments are :
 - `-a` (or `--auto`) : does not prompt the user to press Enter between each output. Be careful if it is an infinite loop program, as it will print non-stop.
 - `-p` (or `--prime_mode`) : switch the input and output to "prime mode". This mean the number will be represented as a sequence of prime powers. E.g. 2 is [1], 75 is [0, 1, 2] and 23 is [0, 0, 0, 0, 0, 0, 0, 0, 1]. In this case, the input can be a sequence of positive integers.
 - `-n` (or `--hide_number`) : if in prime mode, hides the real number and only prints the prime powers representation.
 - `-f` (or `--filter`), followed by a sequence of space-separated `0`, `+` or `*` : filter what numbers will be printed based on their prime power representation. `0` forces the prime to not be present in the number, `+` forces the prime to be at least present once, and `*` allows everything. If this argument is provided, everything after the last character will be considered `0`, and the number will be filtered accordingly. E.g. `-f +` will only prints powers of 2, and `-f * + 0 +` will prints numbers of the forme $2^a3^b7^c$ where $a \ge 0$, $b > 0$ and $c > 0$. Anything divisible by 5 or a prime greater than 7 will be filtered out.

### Usage examples

`code.txt` is the file found in the `codes` folder.

```bash
> python fractran.py codes\code.txt 15
You must press enter after every output to continue the program.

15
20
6
8
```


```bash
> python fractran.py codes\code.txt -a
Program input value (positive integer) ? 15

15
20
6
8
```
```bash
> python fractran.py codes\code.txt 0 1 1 -p -a

[15]    0 1 1
[20]    2 0 1
[6]     1 1
[8]     3
```
```bash
> python fractran.py codes\primes.txt 1 -p -f + -a

[2]     1
[4]     2
[8]     3
[32]    5
[128]   7
[2048]  11
[8192]  13
[131072]        17
[524288]        19
[8388608]       23
[536870912]     29
[2147483648]    31
[137438953472]  37
[2199023255552] 41
[8796093022208] 43
```
```bash
> python fractran.py codes\primes.txt 1 -p -f + -a -n

1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
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

