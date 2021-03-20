


function sq = square_wave(n)
    t = 0 : 4*pi/1000 : 4*pi;           % setup vector according to the specs
    sq = zeros(1,length(t));            % initialize output to 0
    for ii = 1:2:2*n                    % run for first n odd numbers (2k-1)
        sq = sq + cos(ii*t-pi/2)/ii;    % add the next cosine term
    end
end



function s = square_wave(n)
    t = 0 : 4*pi/1000 : 4*pi;   % setup vector according to the specs
    idx = (2*(1:n)' - 1);       % make column vector of fist n odd numbers (2k-1)
    % idx*t makes a matrix; each row is (2k-1)*t, for a given k
    % idx*ones(size(t)) also makes a matrix; each element of row k is just (2k-1)
    % sum down the columns
    s = sum(sin(idx*t) ./ (idx*ones(size(t))),1);
end

% the second argument to sum is needed in case n is 1
% remember that sum(x) sums x along columns unless x is a row vector!


function a = myprime(n)
    a = false;
    if n > 1                    % 1 is by definition not prime
        for ii = 2:sqrt(n)      % see explanation below
            if ~mod(n,ii)
                return;
            end
        end
        a = true;
    end
end
% x is prime if it is NOT divisible by all integers from 2 to sqrt(x)
% because factors have to come in pairs -- one bigger than sqrt(x) and
% one smaller (or both equal)




function prim = myprime(p)
    v = 2:sqrt(p);
    v = v(rem(p,v) == 0);           % if p is prime, none of the remainders can be 0
    prim = ~length(v) && (p ~= 1);  % so if v has any elements, p is not prime
end     
