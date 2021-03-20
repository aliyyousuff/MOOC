% Problem 06: Write a function called replace that takes three inputs: a cell vector (row or column) of
% strings and two characters: c1 and c2. The function returns the cell vector unchanged except
% that each instance of c1 in each string is replaced by c2. You are not allowed to use the built-in
% function strrep.

% Solution:

function outp = replace(trs,ch1,ch2)
[r c] = size(trs);

outp{c} = [];  %// this is just preallocation
for i = 1:c
    temp = trs{i};
    idx = temp==ch1 %// Get a logical matrix of which characters match
    temp(idx)=ch2; %// Use logical indexing to replace all the characters that match in this string in one go!
    outp{i} = temp;
end


% Alternative solution:

function strs = replace(strs,c1,c2);
    for ii=1:length(strs)                   % for each string in the cell vector
        strs{ii}(strs{ii} == c1) = c2;      % replace all c1-s with c2-s at once
    end
end
