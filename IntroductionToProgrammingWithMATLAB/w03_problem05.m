% Write a function called pitty that takes a matrix called ab as an input argument. The matrix ab
% has exactly two columns. The function should return a column vector c that contains positive
% values each of which satisfies the Pythagorean Theorem, a2 + b2 = c2, for the corresponding row of
% ab assuming that the two elements on each row of ab correspond to one pair, a and b,
% respectively, in the theorem. Note that the built-in MATLAB function sqrt computes the square
% root and you are allowed to use it.

% Solution 01:

function c = pitty(ab)
 c = sqrt(ab(:,1).^2 + ab(:,2).^2)
end
