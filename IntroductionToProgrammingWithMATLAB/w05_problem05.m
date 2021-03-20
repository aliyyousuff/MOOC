% Problem 05: Write a function called older that takes as its input arguments six positive scalar integers: y1, m1, d1, y2,
% m2, d2, in that order, representing the birthdates of two persons. The variables that start with y stand for
% the year, m for the month and d for the day. The variables that end in 1 correspond to the first person, while
% those that end in 2 correspond to the second person. The function returns 1 if the first person is older, 0 if
% they have the same age, and -1 if the first person is younger. You do not need to check whether the inputs
% have appropriate values. For example, you may assume that both m1 and m2 are positive integers that are
% less than 13 and that the day numbers fit with their months.

% Solution: 

function old = older(y1,m1,d1,y2,m2,d2)
A1 = datenum([y1 m1 d1]);
A2 = datenum([y2 m2 d2]);
if A1 < A2
    old = 1;
elseif A1 > A2
    old = -1;
elseif A1 == A2
    old = 0;
else
    return
end

% Solution:

function a = older(y1,m1,d1,y2,m2,d2)
    a = 1;
    if y1 == y2 && m1 == m2 && d1 == d2
        a = 0;
    elseif (y1 > y2) || (y1 == y2 && m1 > m2) || (y1 == y2 && m1 == m2 && d1 > d2)
        a = -1;
    end
end

% Solution:

function a = older(y1,m1,d1,y2,m2,d2)
    a1 = y1 * 366 + m1 * 31 + d1;     % does not have to be exact date in days...
    a2 = y2 * 366 + m2 * 31 + d2;     % it simply makes a1 and a2 comparable
    a = sign(a2 - a1);                % sign() returns -1, 0 or 1, just what is needed
end
