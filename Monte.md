# Approximation of pi(π) using the Monte Carlo Method

Monte carlo method is a numerical method that approximates the value of pi(3.14)
Monte carlo method generates random x and y coordinates between 0 and 1
The below equation is used and if true the coordinate is classified as a hit,meaning coordinate lies within circle. If false, coordinate is classified as false,meaning coorindate is outside circle
\[x^2 + y^2\leq 1\]
The value of pi can be approximated via the below equation
\[pi = \frac{Number of hits}{Total Number of points}\]
As the number of points increases, the value of pi becomes more accurate due to the increased number of data points

# Technology used

- Python

# Libaries used

- Random
- matplotlib
- numpy
