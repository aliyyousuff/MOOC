% Write a function called mean_squares that returns mm, which is the mean of the squares of the
% first nn positive integers, where nn is a positive integer and is the only input argument. For
% example, if nn is 5, your function needs to compute the average of the numbers 1, 4, 9, 16, and 25.
% You may use any built-in functions including, for example, sum.

% Solution 01:

function mm = mean_squares(nn)
 input_vector = 1:nn;
 sq_input_vector = (input_vector).^2;
 sum_sq_input_vector = sum(sq_input_vector);
 mm = sum_sq_input_vector/length(input_vector)
end


% Solution 02:

function mm = mean_squares(nn)
 mm = mean((1:nn).^2);
end
