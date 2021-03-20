% Problem 01: Write a function called generationXYZ that takes as its only input argument one positive integer
% specifying the year of birth of a person and returns as its only output argument the name of the generation
% that the person is part of ('X', 'Y', or 'Z ') according to the table below. For births before 1966, return 'O' for
% Old and for births after 2012, return 'K' for Kid . Remember that to assign a letter to a variable, you need to
% put it in single quotes, as in: gen = 'X'.

% Solution 01:

% Write a function that will return different age gruop following your
% given Names.

function x = generationXYZ(n)
if n < 1966                    % age is less than 1966
    x = 'O';                   % if then it would reply 'O'
    fprintf('\n',x);
elseif n >= 1966 && n <= 1980  % Age is between 1966 & 1980
    x = 'X';                   % if then it would reply 'X'
elseif n >= 1981 && n <= 1999  % Age is between 1981 & 1999
                               % if then it should reply 'Y'
       x = 'Y';
elseif n >= 2000 && n <= 2012  % Age is between 2000 & 2012
    x = 'Z';                   % If then it should reply 'Z'
elseif n > 2012                % Age is greater than 2012
    x = 'K';                   % If then it should reply 'K'
else
    return
end


% Solution 02:

function gen = generationXYZ(year)
    if year < 1966
        gen = 'O';
    elseif year < 1981
        gen = 'X';
    elseif year < 2000
        gen = 'Y';
    elseif year < 2013
        gen = 'Z';
    else
        gen = 'K';
    end
end


% Solution 03:

function gen = generationXYZ(yr)
    opts = {'O','X','Y','Z','K'};  % Create cell array of options
    idx = 1 + sum(yr >= [1966,1981,2000,2013]); % Calculate index by comparing year to edge values
    gen = opts{idx};
end

