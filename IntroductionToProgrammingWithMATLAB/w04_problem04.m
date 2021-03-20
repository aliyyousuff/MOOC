% Write a function called mtable that returns mt an n-by-m matrix corresponding to the
% multiplication table (n is the first and m is the second input argument). That is, the element of mt at
% row ii and column jj equals to ii*jj . The function also has a second output, s, a scalar that
% equals the sum of all the elements of mt.

% Solution

function [t s] = mtable(n,m)
 t = (1:n)' * (1:m);
 s = sum(t(:));
end
