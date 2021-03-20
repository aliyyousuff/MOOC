% Problem 08: Write a function called censor whose first input argument is a cell vector (row or column) of
% strings and whose second input argument is a string. It removes each element of the cell vector
% whose string is either identical to the second input argument or contains the second argument
% as a substring. The resulting cell vector is returned as the only output argument. For example,
% suppose each element of the first argument refers to one line of the first verse of the US
% national anthem and the second argument is ' the' . Then the function would return a cell
% vector with a single element containing the string: ' Oh, say does that starspangled banner yet wave' .


% Solution:

function outp = censor(str,ban)
outp = str;
Cnew = str(cellfun('isempty', strfind(str,ban)));
outp = Cnew;
end


% Alternative solution:

function out = censor(strs,str)
    out = {};                               % creates the output from scratch
    for ii = 1:length(strs)                 % for each string in the cell vector
        if isempty(strfind(strs{ii},str))   % if the substring is not found
            out = [out strs{ii}];           % the current string goes into the output
        end
    end
end
