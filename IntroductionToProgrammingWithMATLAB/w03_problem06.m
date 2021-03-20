% Write a function called bottom_left that takes two inputs: a matrix N and a scalar n, in that
% order, where each dimension of N is greater than or equal to n. The function returns the n-by-n
% square array at the bottom left corner of N.

% Solution 01:

function M = bottom_left(N,n)
 m = N(end-(n-1):end,1:n);
 M = m
end

% Solution 02:

function M = bottom_left(N,n)
 M = N(end-n+1:end, 1:n);
end

% We need the last n rows and the first n columns. The only trick here is that we need end-n+1, because end-n:end would get us 
% n+1 indexes and not n as required.
