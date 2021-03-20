% Write a function called odd_index that takes a matrix, M, as input argument and returns a matrix
% that contains only those elements of M that are in odd rows and columns. In other words, it would
% return the elements of M at indices (1,1), (1,3), (1,5), …, (3,1), (3,3), (3,5), …, etc. Note that both the
% row and the column of an element must be odd to be included in the output. The following would
% not be returned: (1,2), (2,1), (2,2) because either the row or the column or both are even. As an
% example, if M were a 5-by-8 matrix, then the output must be 3-by-4 because the function omits
% rows 2 and 4 of M and it also omits columns 2, 4, 6, and 8 of M.

% My solution:

function M = bottom_left(N,n)
m = N(end-(n-1):end,1:n);
M = m
end

% Alternative solution:


function out = odd_index(M)
out = M(1:2:end, 1:2:end);
end

