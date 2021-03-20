% Write a function called checkerboard that takes as input two positive integer scalars, n and m,
% in that order. The function must create and return board, which is an n-by-m matrix. Every
% element of board is either 0 or 1. The first element, board(1,1) is 1. No direct neighbors in the
% matrix, vertically or horizontally, can be equal. That is, a 1 element cannot have 1 immediately
% preceding or following it in the same row or column.

%Solution 01:

function ch = checkerboard(n,m)
 ch(1:n,1:m) = 1;
 ch(1:2:n,2:2:m) = 0;
 ch(2:2:n,1:2:m) = 0;
end

% Solution 02:

function b = checkerboard(n,m)
 
    b = ones(n,m);
    b(1:2:n,2:2:m) = 0;
    b(2:2:n,1:2:m) = 0;
end
