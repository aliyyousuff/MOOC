% Write a function called hulk that takes a row vector v as an input and returns a matrix H whose
% first column consist of the elements of v, whose second column consists of the squares of the
% elements of v, and whose third column consists of the cubes of the elements v. For example, if you
% call the function likes this, A = hulk(1:3) , then A will be [ 1 1 1; 2 4 8; 3 9 27 ] .

% Solution 01:

function H = hulk(v)
 first_col = v;
 second_col = (v).^2;
 third_col = (v).^3;
 mt = [first_col; second_col; third_col];
 H = mt'
end

% Solution 02:

function H = hulk(v)
 H = [v' (v').^2 (v').^3];
end
