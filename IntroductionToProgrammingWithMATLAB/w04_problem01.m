% Write a function called quadrants that takes as its input argument a scalar integer named n. The
% function returns Q, a 2n-by-2n matrix. Q consists of four n-by-n submatrices. The elements of the
% submatrix in the top left corner are all 1s, the elements of the submatrix at the top right are 2s, the
% elements in the bottom left are 3s, and the elements in the bottom right are 4s.

% Solution01:

function Q = quadrants(n)
 Q = [ones(n)*1 ones(n)*2; ones(n)*3 ones(n)*4];
end

% Solution02:

function Q = quadrants(n)
 a = ones(n);
 Q = [a 2*a ; 3*a 4*a];
end

