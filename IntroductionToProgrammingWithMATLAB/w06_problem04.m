% Problem 04: Write	a	function	called	 large_elements that	takes	 as	input	an array named X that is	a	matrix	
% or	a	vector. The	function	 identifies those	elements	of	 X that	are	greater	than	the	sum	of	their	two	
% indexes.	For	example,	if the	element X(2,3) is	6,	 then	that	element would	be	 identified because 6	
% is	 greater	than	2	+	3.		The	output	of	the	function	 gives the indexes of	 such	elements found	in	 rowmajor order.	It	is	a	matrix	with	exactly	two	columns.	The	first	column	contains	the row indexes,	
% while	the	second	 column	 contains	the	corresponding	column	indexes.	For	example,	the	statement	
% indexes = large_elements([1 4; 5 2; 6 0] ,	will	make	 indexes equal	to	 [1 2;
% 2 1; 3 1] . If	no	such	element	exists,	the	function	returns	 an	 empty	 array.

% Solution:

function outp = large_elements(X)
[row col] = size(X);
outp = [];
for i = 1:row
    for ii = 1:col
        sumI = i + ii;
        if sumI < X(i,ii);
        outp = [outp; i ii]
        elseif sumI >= X(i,ii)
            outp = [outp];
        else
            return
            
        end
    end
end

% Alternative solution:

function found = large_element(A)
    [row col] = size(A);
    found = [];
    for ii = 1:row
        for jj = 1:col
            if A(ii,jj) > ii + jj       % if the element is larger than the sum of its indexes
                found = [found; ii jj]; % add a new row to the output matrix
            end
        end
    end
end
