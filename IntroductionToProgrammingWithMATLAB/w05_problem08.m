% Problem 08:

% Write a function called moving_average that takes a scalar called x as an input argument and
% returns a scalar. The value it returns depends not only on the input but also on previous inputs to this same
% function when the function is called repeatedly. That returned value is a “moving average” of those inputs.
% The function uses a “buffer” to hold previous inputs, and the buffer can hold a maximum of 25 inputs.
% Specifically, the function must save the most recent 25 inputs in a vector (the buffer) that is a persistent
% variable inside the function. Each time the function is called, it copies the input argument into an element of
% the buffer. If there are already 25 inputs stored in the buffer, it discards the oldest element and saves the
% current one in the buffer. After it has stored the input in the buffer, it returns the mean of all the elements
% in the buffer. Thus, for each of the first 24 calls to the function, the function uses only the inputs it has
% received so far to determine the average (e.g., the first call simply returns x, the second call averages x and
% the input from the first call, etc.), and after that, it returns the average of the most recent 25 inputs.
% Solution:
function a = moving_average(x)
    persistent xp;
    if isempty(xp)
        xp = x;                 % first time, the buffer simply contains x
    elseif length(xp) < 25
        xp(end+1) = x;          % while fewer than 25 elements, keep adding x to the buffer
    else
        xp = [xp(2:end),x];     % replace first (oldest) element by shifting to the left
    end                         % and inserting x at the end
    a = mean(xp);
end

% Alternative solution:

function avg = moving_average (in)
    persistent buffer;
    buffer = [in buffer(1:end-(length(buffer) == 25))];
    avg = mean(buffer);
end

% This is an illustration of a short, but tricky solution. However,
% a longer, but more readable solution is always preferred, therefore,
% the first solution is better!
%
% This one works by realizing that we do not need to check whether the
% buffer is empty or not, since [x buffer] will work either way.
% The tricky part is how the length is handled. While the buffer is
% shorter than 25, buffer(1:end) is used. Once it reaches 25, it turns
% into buffer(1:end-1), exactly what is needed.
