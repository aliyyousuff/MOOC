% Problem 04: Write a function called classify that takes one input argument x. That argument will have no more
% than two dimensions. If x is an empty matrix, the function returns -1. If x is a scalar, it returns 0. If x is a
% vector, it returns 1. Finally, if x is none of these, it returns 2. Do not use the built-in functions isempty,
% isscalar, or isvector.

function c = classify(x)
[r, cl] = size(x);
if numel(x) == 0
    c = -1;
elseif numel(x) == 1 
        c = 0;
elseif r == 1 && cl > 1 || r > 1 && cl == 1 % for row vector & column vector
    c = 1;
elseif r > 1 && cl > 1
    c = 2;
else
    return
    
end

% Solution 02:

function c = classify(x)
    [row, col] = size(x);
    if row == 0 || col == 0         % any dim == 0 -> empty
        c = -1;
    elseif row == 1 && col == 1     % both dim == 1 -> scalar
        c = 0;
    elseif row == 1 || col == 1     % none of the above, but one dim == 1 -> vector
        c = 1;
    else
        c = 2;
    end
end
