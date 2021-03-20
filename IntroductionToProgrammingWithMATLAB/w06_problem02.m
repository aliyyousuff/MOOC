% Problem 02: The	function	 replace_me is	defined	like	this:	 function w = replace_me(v,a,b,c) .	 The	
% first	input	argument	 v is	a	vector,	while	 a,	 b,	 and	 c are	all	scalars.	The	function	replaces	 every
% element	of	 v that	 is	 equal	to	 a with	 b and	 c.	For	example,	the	command	
% >>	 x = replace_me([1 2 3],2,4,5) ;
% makes	 x equal	to	 [1 4 5 3] .	If	 c is	omitted,	it	replaces	occurrences	of	 a with	two	copies	of	 b.	If	
% b is	also	omitted,	it	replaces each a with	two	 zeros.

% Solution:

function [result] = replace_me(v,a,b,c)
    if nargin == 3
        c = b;
    end
    if nargin == 2
        c = 0;
        b = 0;
    end
    result = v;
    equ = result == a;
    result = num2cell(result);
    result(equ) = {[b c]};
    result = [result{:}];
end

% Alternative solution:

function w = replace_me(v,a,b,c)
    if nargin < 3
        b = 0;
    end
    if nargin < 4
        c = b;
    end
    w = [];
    for k = 1:length(v);
        if v(k) == a        % if a is found,
            w = [w,b,c];    % we insert b and c at the end of the current w
        else                % otherwise,
            w = [w,v(k)];   % we insert the original element of v
        end
    end
end

% Solution:

function w = replace_me(v,a,b,c)
    if nargin < 3
        b = 0;
    end
    if nargin < 4
        c = b;
    end
    w = v;                                      % make w the same as v
    wi = 1;                                     % wi is used to index into w
    for vi = 1:length(v)
        if v(vi) == a
            w = [w(1:wi-1) b c w(wi+1:end)];    % insert b and c at position wi
            wi = wi + 1;                        % increment wi
        end
        wi = wi + 1;                            % wi is incremented in either case
    end
end
