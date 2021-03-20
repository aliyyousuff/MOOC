% Problem 04: Write a function called codeit that takes a string txt as input and returns another string
% coded as output. The function reverses the alphabet: It replaces each 'a' with 'z', each 'b' with
% 'y', each 'c' with 'x', etc. The function must work for uppercase letters the same way, but it must
% not change any other characters. Note that if you call the function twice like this str =
% codeit(codeit(txt)) then str and txt will be identical.

% Solution:

function coded = codeit(in_str)

upper_mask = in_str>=65 & in_str<=90 ; 
lower_mask = in_str>=97 & in_str<=122;
coded = in_str;
coded(upper_mask) = char(in_str(upper_mask) + 2*(78-in_str(upper_mask))-1);
coded(lower_mask) = char(in_str(lower_mask) + 2*(110-in_str(lower_mask))-1);
end

% Alternative solution:

function out = codeit(in)
    for ii = 1:length(in)
        if in(ii) <= 'z' && in(ii) >= 'a'       % lower case
            out(ii) = 'a' + 'z' - in(ii);       % encrypt it
        elseif in(ii) <= 'Z' && in(ii) >= 'A'   % upper case
            out(ii) = 'A' + 'Z' - in(ii);       % encrypt it
        else                                    % everything else
            out(ii) = in(ii);                   % no change needed
        end
    end
end


% Alternative solution:
function txt = codeit (txt)
    U = txt > 64 & txt < 91;    % identify uppercase
    L = txt > 96 & txt < 123;   % identify lowercase
    txt(U) = char(155-txt(U));  % encrypt uppercase
    txt(L) = char(219-txt(L));  % encrypt lowercase
end



