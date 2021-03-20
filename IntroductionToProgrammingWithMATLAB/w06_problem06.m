% problem 06: Write	a	function	called	 approximate_pi that	uses the	following	approximation	of π:	
Instead	of	going	to	infinity,	the	function	 stops	at the	smallest	 k for	which the	approximation differs	
from	 pi (i.e.,	the	value	returned	MATLAB’s	built-in	function)	by	no	more	than	the	positive	scalar,	
delta,	 which	is	the	only	input	argument. The	first	output	of	the	function	is	the	approximate	value	
of	π,	while	the	second	is	 k. (Note:	if	your	program	or	the	grader	takes	a	long	time,	you	may	have	
created	an	infinite	loop	and	need	to	hit	Ctrl-C	on	your	keyboard.)

% Solution:

function [a,k] = approximate_pi(delta)
    k = 0;
    f = sqrt(12);                       % compute sqrt(12) only once
    a = f;                              % the value of a for k == 0
    while abs(pi-a) > delta             % while we are further away than delta
        k = k + 1;                      % increment k
        a = a + f*(-3)^(-k)/(2*k+1);    % add increment to current value of a
    end
end

