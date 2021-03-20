% Write a function called identity that creates a square identity matrix, which is a matrix whose
% elements are 0 except for ones on the diagonal (from top left to bottom right). The diagonal
% consists of those elements whose row and column indexes are the same: (1,1), (2,2), etc. The
% function takes one positive integer input argument, which is the size of the matrix, and returns the
% matrix itself as an output argument. For example, identity(4) must return a 4-by-4 identity
% matrix. You are not allowed to use the built-in eye or diag functions. (Hint: you can index into a
% matrix with a single index and MATLAB will handle it as if it was a vector using column-major
% order.)

% solution:

function id = identity(i)
 id(1:i,1:i) = 0;
 id(1:i+1:end) = 1;
end

% Solution 02:

function I = identity(n)
 
    I = zeros(n);
    I(1 : n+1 : n^2) = 1;
end
