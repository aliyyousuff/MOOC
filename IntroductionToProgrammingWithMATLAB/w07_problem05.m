% Problem 05: 


% Solution:

function outp = dial(inp)
outp = [];

for i = 1:length(inp)
    if inp(i) == 'Q' || inp(i) == 'Z'
        outp = [];
        return
    elseif inp(i) == '(' || inp(i) == ')' || inp(i) == '-' || inp(i) == ' '
        outp = [outp ' '];
    elseif inp(i) == 'A' || inp(i) == 'B' || inp(i) == 'C'
        outp = [outp '2'];
    elseif inp(i) == 'D' || inp(i) == 'E' || inp(i) == 'F'
        outp = [outp '3'];
    elseif inp(i) == 'G' || inp(i) == 'H' || inp(i) == 'I'
        outp = [outp '4'];
    elseif inp(i) == 'J' || inp(i) == 'K' || inp(i) == 'L'
        outp = [outp '5'];
    elseif inp(i) == 'M' || inp(i) == 'N' || inp(i) == 'O'
        outp = [outp '6'];
    elseif inp(i) == 'P' || inp(i) == 'R' || inp(i) == 'S'
        outp = [outp '7'];
    elseif inp(i) == 'T' || inp(i) == 'U' || inp(i) == 'V'
        outp = [outp '8'];
    elseif inp(i) == 'W' || inp(i) == 'X' || inp(i) == 'Y'
        outp = [outp '9'];   
        
    elseif inp(i) == '#'
        outp = [outp inp(i)];
    elseif inp(i) == '*'
        outp = [outp '*'];
   elseif inp(i) == '1'
        outp = [outp '1'];
     elseif inp(i) == '0'
       outp = [outp '0'];
    elseif inp(i) == '2'
         outp = [outp '2'];
     elseif inp(i) == '3'
         outp = [outp '3'];
     elseif inp(i) == '4'
         outp = [outp '4'];
     elseif inp(i) == '5'
         outp = [outp '5'];
    elseif inp(i) == '6'
         outp = [outp '6'];
    elseif inp(i) == '7'
         outp = [outp '7'];
     elseif inp(i) == '8'
         outp = [outp '8']
    elseif inp(i) == '9'
         outp = [outp '9'];
    else
        outp = [];
        return
    
end
end


% Alternative solution:

function ph = dial(str)
    code = {'ABC'; 'DEF'; 'GHI'; 'JKL'; 'MNO'; 'PRS'; 'TUV'; 'WXY'};
    ph = str;                       % set the output to the input
    for ii = 1:length(str)
        c = str(ii);                % the current char from the input
        if c == ' ' || c == '-' || c == '(' || c == ')'
            ph(ii) = ' ';           % these characters need to turn into spaces
            continue;
        elseif (c >= '0' && c <= '9') || c == '#' || c == '*'
            continue;               % these need to remain unchanged
        else
            n = -1;
            for jj = 1:length(code)
               if ~isempty(strfind(code{jj},c))   % looking for legal letters
                   n = jj + 1;      % Found it! ABC on the dial maps to 2 not 1, hence the +1
                   break;
               end
            end
            if n == -1              % if we did not find a valid letter
                ph = [];            % need to return []
                return;
            end
            ph(ii) = char('0' + n); % otherwise, add the char for the right number
        end
    end
end


% Alternative solution:

function ph = dial(str)
    % the variable code has the characters' required mapping starting from space, ending with Y
    % x is for illegal input (e.g., see how Q maps to x in-between 7-s)
    code = ' xx#xxxx  *xx xx0123456789xxxxxxx2223334445556667x77888999';
    ph = [];        % default return value in case of illegal input
    n = str-' '+1;  % creates a vector of indexes into code from the input characters
    % the first two sum()-s  check for out-of-range input (smaller than space or larger than Y )
    % the third sum() checks for any input char mapping to x, that is, illegal input
    if ~((sum(n <= 0) + sum(n > length(code))) || sum(code(n) == 'x'))
        ph = code(n);   % a single assignment does the actual transformation of the input string
    end
end
