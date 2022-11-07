# Get_square_sum

# Question
A perfect square is a number that can be expressed as a product of an integer with itself.
(For example, 49 is the product of 7 with itself).A function F(N) is defined such that it returns the
sum of all perfect squares less than or equal to N, where N is a positive integer. An advanced
version of F(N), function get_square_sum(M, N) , is defined such that it applies operation
F(N) ’M’ times to the result of the previous operation, starting from N.

Write the function get_square_sum(M, N).You may assume M >= 1, N >= 1.

# Example 1:
get_square_sum(1,10):

here M=1, N=10

Sum of all perfect squares <=10 is:

1 + 4 + 9 = 14

Since M=1, we will stop here.

output = 14

# Example 2:

get_square_sum(2,20):

here M=2, N=20

Sum of all perfect squares <=20 is:

1 + 4 + 9 + 16 = 30

Sum of all perfect squares <=30 is:

1 + 4 + 9 + 16 + 25 = 55

Since M=2, we will stop here.

output = 55
