% Problem 03: Write	 a	 function	 called	 halfsum that	 takes	 as	 input	 an	 at	 most	 two-dimensional matrix	 A and	
% computes	 the	 sum	 of	 the	 elements	 of	 A that	 are	 in	 the	 diagonal	 or are to	 the	 right	 of	 it.	 The	
% diagonal	is	defined	as	the	set	of	those	elements	whose	column	and	row	indexes	are	the	same.	 For	
% example,	if	the	input	is [1 2 3; 4 5 6; 7 8 9] ,	 then	the	function	would	return	26.

% Solution:

function s = halfsum(A)
    [row col] = size(A);
    s = 0;
    for ii = 1:row
        for jj = ii:col         % the column index only starts at the current row index
            s = s + A(ii,jj);
        end
    end
end

% Alternative solution:

function s = halfsum(A)
    [nr,~] = size(A);
    s = 0;
    for r = 1:nr                    % for each row
        s = s + sum(A(r,r:end));    % sum adds up the elements right of the diagonal (inclusive)
    end                             % in the current row
end
