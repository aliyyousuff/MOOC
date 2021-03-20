% Problem 08: Write	 a	 function	 called	 divvy that	 takes	 a	 matrix	 A of	 positive	 integers	 and	 a	 single	 positive	
integer	 k as	its	two	inputs	 and	returns	a	matrix	 B that	has	the	same	size	as	 A.	The	elements	of	 B are	
all	divisible	by	 k.	If	an	element	of	 A is	divisible	by	 k,	 then	 the	corresponding	element	in	 B must	
have	the same value.	If	an	element	of	 A is	not	divisible	by	 k,	 then	 the	corresponding	element	of	 B
must	be	the	product	of	the	given	element	of	 A and	 k.	You	are	not	allowed	to	use	any	 for-loops or	
while-loops.	 For	example,	the	call	 X = divvy([1 2 ; 3 4], 2) would	make	 X equal	to								
[2 2 ; 6 4] .

% Solution:

function A = divvy (A,k)
    L = (mod(A,k) ~= 0);    % creates a logical matrix based on divisibility by k
    A(L) = k * A(L);        % changes only the non-divisible elements of A by multiplying them by k
end

% Solution:

function I = divvy(I,k)
    I(mod(I,k) ~= 0) = I(mod(I,k) ~= 0) * k;
end
% same solution as above, but it repeats the modulo computation

