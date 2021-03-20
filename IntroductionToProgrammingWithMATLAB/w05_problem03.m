% Problem 03: Write a function called sort3 that takes three scalar arguments. It uses if-statements, possibly nested, to
% return the three values of these arguments in a single row-vector in increasing order (or more precisely,
% non-decreasing order), i.e., element one of the output vector equals the smallest input argument and
% element three of the output vector equals the largest input argument. NOTE: Your function may not use any
% built-in functions, e.g., sort.

% Solution 01:

function nw = sort3(s,m,l)

v = [s m l ] ; %// group all variable in one array

if (v(1)==v(2) & v(1) == v(3) & v(2)==v(3)) %// check just in case they are all the same value
    nw = v ;
else
    [~,ix(1)] = min( v ) ; %// assign the index of the smallest value
    [~,ix(3)] = max( v ) ; %// assign the index of the largest value
    ix(2) = 6 - sum(ix) ;  %// find the middle index by difference (because cumsum([1 2 3]) = 6 )
    nw = v(ix) ;           %// assign the output vector based on indices collected
end

% Solution 02: 

function v = sort3(a, b, c)
    if a <= b
        v = [a b];
    else
        v = [b a];
    end
    if c >= v(2)            % a and b in v are ordered. Where to insert c?
        v = [v c];          % at the end
    elseif c <= v(1)
        v = [c v];          % at the beginning
    else
        v = [v(1) c v(2)];  % in the middle
    end
end


% Solution 03:

function v = sort3 (a,b,c)
    v = [a b c];                                % unordered
    v = [min(v(1),v(3)) v(2) max(v(1),v(3))];   % the 1st and 3rd are in order
    v = [min(v(1),v(2)) max(v(1),v(2)) v(3)];   % move 2nd left if necessary
    v = [v(1) min(v(2),v(3)) max(v(2),v(3))];   % move 2nd right if necessary
end
