% Problem 01: Write a function called integerize that takes as its input a matrix A of non-negative integers
% of type double, and returns the name of the “smallest” unsigned integer class to which A can
% be accurately converted. If no such class exists, the string 'NONE' is returned. For example, if
% the largest integer A is 14, then the function would return 'uint8' , but if the largest integer
% in A is 1e20, then the function would return 'NONE'.

% Solution: 
function outp = integerize(A)
Arr = 0;
[r, c] = size(A);

mn = min(A);
mx = max(A);
if r > 1 && c >1
    mn = min(A(:)');
    mx = max(A(:)');
end
if mn >= 0 && mx <= 255;
   outp = 'uint8';
elseif mn >=0 && mx <= 65535
    outp = 'uint16';
elseif mn >= 0 && mx <= 4294967295
    outp = 'uint32';
 elseif mn >= 0 && mx <= (2^64-1)
    outp = 'uint64';
else
    outp = 'NONE';
end
end



% Alternative solution:

function name = integerize(A)
    mx = max(A(:));
    name = 'NONE';
    if mx <= intmax('uint8')
        name = 'uint8';
    elseif mx <= intmax('uint16')
        name = 'uint16';
    elseif mx <= intmax('uint32')
        name = 'uint32';
    elseif mx < intmax('uint64')
        name = 'uint64';
    end
end


% Alternative solution:

function cl = integerize(A)
    cls = {'uint8'; 'uint16'; 'uint32'; 'uint64'};
    cl = 'NONE';
    mx = max(A(:));
    for ii = 1:length(cls)
        if intmax(cls{ii}) >= mx
            cl = cls{ii};
            break;
        end
    end
end


% Alternate solution:

function iclass = integerize(A)
    c = {'uint8','uint16','uint32','uint64','NONE'};
    % Array of maximum values for each class
    x = 2.^[8,16,32,64] - 1;
    % Index into names, based on size of largest element of A
    iclass = c{sum(max(A(:))>x)+1};
end
