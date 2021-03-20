% Problem 05: Write	a	function	called	 one_per_n that	returns	the	smallest positive	integer n for	which	the	sum	
% 1	+	1/2	+	1/3	+	…	+	1/n	,	is	greater	than or	equal	to x where	 x is	 the	 input	argument. Limit	the	
% maximum	number	 n	 of	 terms	in	the	sum	 to	10,000	and	return	 -1 if	it	is	exceeded. (Note:	if	your	
% program	or	the	grader	takes	a	long	time,	you	may	have	created	an	infinite	loop	and	need	to	hit	CtrlC	on	your	keyboard.)

% Solution:

function n = one_per_n(x)
    n = 0;
    sum = 0;
    while sum < x && n <= 10000
        n = n + 1;
        sum = sum + 1/n;
    end
    if n > 10000
        n = -1;
    end
end

% Solution Alternative:

function n = one_per_n(x)
    s = 0;
    for n = 1:1e4
        s = s + 1/n;
        if s >= x
            return;
        end
    end
    n = -1;
end
