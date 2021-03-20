% Write a function called randomness that takes three input arguments: limit, n, and m, in that
% order. The function returns an n-by-m matrix of uniformly distributed random integers between 1
% and limit inclusive. You are not allowed to use randi, but you can use rand. You will also find
% the built-in function floor useful for obtaining integers. To make sure that your result is indeed
% uniformly distributed, test the output of the function by using the built-in function hist, which
% plots a histogram.

% Solution 01:

function FR = randomness(limit,n,m)
 FR =floor(1 + rand(n,m)*(limit));
end

% Solution 02:

function r = randomness(limit,n,m)
  r = fix(limit * rand(n,m)) + 1;
end

