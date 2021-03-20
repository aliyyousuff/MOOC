% Problem 07: Write a function called roman that takes a string representing an integer between 1 and 20
% inclusive using Roman numerals and returns the Arabic equivalent as a number of type uint8.
% If the input is illegal or its value is larger than 20, roman returns 0 instead. The rules for Roman
% numerals can be found here: http://en.wikipedia.org/wiki/Roman_numerals. Use the definition
% at the beginning of the page under the “Reading Roman Numerals” heading. In order to have
% unambiguous one-to-one mapping from roman to Arabic numbers, consider only the shortest
% possible roman representation as legal. Therefore, only three consecutive symbols can be the
% same (IIII or VIIII are illegal, but IV and IX are fine), and a subtractive notation cannot be
% followed by an additive one using the same symbols making strange combinations, such as IXI
% for 10 or IXX for 19, illegal also.

% Solution:

function outp = roman(rm)
outp = uint8(0);
ind = [];
ca = {'I','II','III','IV','V','VI','VII','VIII','IX','X',...
    'XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX'};
for i = 1:length(ca)
    ind = [ind strcmpi(ca(i),rm)];
end

    if sum(ind) == 0
        return
    elseif sum(ind) == 1;
        for ii = 1:length(ind);
            if ind(ii) == 1
                outp = uint8(ii);
            end
        end
    end
end


% Alternative solution:

function num = roman(rom)
    romans = { 'I' 'II' 'III' 'IV' 'V' 'VI' 'VII' 'VIII' 'IX' 'X' ...
        'XI' 'XII' 'XIII' 'XIV' 'XV' 'XVI' 'XVII' 'XVIII' 'XIX' 'XX'};
    num = uint8(0);
    for ii = 1:20
        if strcmp(rom,romans{ii})
            num = uint8(ii);
            break
        end
    end
end


% Solution:

function ar = roman(str)
    allstr = {'I','II','III','IV','V','VI','VII','VIII','IX','X',...
        'XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX'};
    ar = find(strcmp(allstr,str));  % find() returns the indexes of non-zero elements
    if isempty(ar)                  % if no match, input is bad
        ar = 0;                     % no need to convert to uint8 yet
    end
    ar = uint8(ar);                 % convert to uint8
end
