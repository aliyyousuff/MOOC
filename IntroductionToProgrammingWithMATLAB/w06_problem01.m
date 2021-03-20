% Problem 01: Write	a	function	called	 neighbor that	takes	 as	 input a row vector	called	 v and	creates	another	
% row	 vector	 as	 output	 that	 contains	 the	 absolute	 values	 of	 the	 differences between	 neighboring	
% elements	of	 v.	For	example,	if	 v == [1 2 4 7] ,	 then the	output	of	the	function	would	be	 [1
% 2 3] .	Notice	that	the	length	of	the	output	vector	is	one	less	than	that	of	the	input.	Check	that	the	
% input	 v is	indeed	a	vector and	has at	least	two	elements and	 return	 an	empty	array	 otherwise. You	
% are	not	allowed	to	use	the	 diff built-in	function.

% Solution 01:

function out = neighbor(v)
out = [];
[r c] = size(v);

    for i = 1:length(v)-1
        if (r == 1) && (c >= 2)
        rnce = abs(v(i+1) - v(i));
        out = [out rnce]
        else
            out = []
        end
    end
end

% Alternative solution:

function w = neighbor(v)
    w = [];
    if min(size(v)) == 1                    % must be a vector
        for ii = 1:length(v)-1              % if length is less than 2, loop won't do anything
            w(ii) = abs(v(ii+1) - v(ii));
        end
    end
end

% Alternative solution:

function w = neighbor(v)
    if length(v) < 2 || min(size(v)) ~= 1  % must be a vector of at least two elements
        w = [];
    else
        w = abs(v(1:end-1)-v(2:end));      % take the difference of two subvectors
    end                                    % of length (n-1)
end
