% Problem 07: Write	a	function	called	 separate_by_two that	takes a	matrix A of	positive	integers	 as	an	input	
% and	returns	two	row	vectors.	The	first	one	contains	all	the	even	elements	of	 A and	nothing	else,	
% while	the	second	contains	all	the	odd	elements	of	 A and	nothing	else,	 both	 arranged	 according	to
% column-major	order of	 A.	You	are	not	allowed	to	use	for-loops	 or	while-loops.

% Solution:

function [outp1 outp2] = separate_by_two(A)
 keepers = mod(A,2);
 keep_odd = keepers == 0;
 oddn = A(keep_odd);
 outp1 = [oddn'];
 keep_even = keepers == 1;
 evenn = A(keep_even);
 outp2 = [evenn'];
end

% Alternative solution:


function [even,odd] = separate_by_two(A)
    even = A(fix(A/2) == A/2)';  % if A is even, rounding does not do anything to A/2
    odd  = A(fix(A/2) ~= A/2)';  % if A is odd, it gets rid of the .5 part, so they won't be equal
end
% note that this will put non-integers into odd
