%Suppose we have a pile of coins. Write a function called rich that computes how much money we
% have. It takes one input argument that is a row vector whose 4 elements specify the number of
% pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents) that we have (in the
% order listed here). The output of the function is the value of the total in dollars (not cents). For
% example, if we had five coins, four quarters and a penny, the answer would be 1.01

% Solution number 01:

function rr = rich(d)
 rr = (d(1,1)*1+ d(1,2)*5+ d(1,3)*10+ d(1,4)*25)/100;
end


% Solution number 02:

function usd = rich(cent)
 usd = [0.01 0.05 0.10 0.25] * cent';
end

% We use the fact that matrix multiplication sums up a set of products. Multiplying a row vector with a column vector 
% will result in a scalar. Here it performs the exact calculations we need.

