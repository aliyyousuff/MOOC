% Write a function called int_col that has one input argument, a positive integer n that is greater
% than 1, and one output argument v that is a column vector of length n containing all the positive
% integers smaller than or equal to n, arranged in such a way that no element of the vector equals its
% own index. In other words, v(k) is not equal to k for any valid index k.

Solution no. 01:

function v = int_col(n)
v = [n 1:n-1]';
end

