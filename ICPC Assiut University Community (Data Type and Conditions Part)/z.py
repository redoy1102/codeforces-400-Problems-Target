import math

a, b, c, d = map(int, input().split())

if b * math.log(a) > d * math.log(c):
    print("YES")
else:
    print("NO")
    
    
    
    
# The last solution I provided for the problem uses logarithms to compare a^b and c^d. This is different from the first two solutions, which use the built-in pow() function or the ** operator to compute a^b and c^d.

# The main advantage of using logarithms is that they can avoid issues with floating point precision that can arise when using the pow() function or the ** operator. In particular, when a^b and c^d are very large or very small numbers, computing them directly can lead to overflow or underflow errors, which can cause incorrect results or crashes.

# By taking the logarithm of both sides of the inequality, we can avoid these issues, since logarithms reduce the range of the values being compared. Moreover, computing logarithms is generally faster and more accurate than computing exponentials, especially for large numbers.

# In the solution that uses logarithms, we first import the math module, which provides a log() function that computes the natural logarithm of a number. We then use this function to compute the logarithms of a and c, and multiply them by b and d, respectively. Finally, we compare the products using the > operator to determine whether a^b > c^d.
