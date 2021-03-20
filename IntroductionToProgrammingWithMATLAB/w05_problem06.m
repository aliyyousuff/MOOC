% Problem 06: Write a function called movies that takes the starting times of two movies, hr1, hr2, min1, min2, and
% their durations, durmin1, durmin2, as its input arguments and decides whether we can binge and watch
% both. The criteria are that they must not overlap and that we are not going to wait more than 30 minutes
% between the end of one and the beginning of the next. It returns true if the criteria are both met and
% returns false otherwise. You may assume that movie start times are always after 1 pm and before
% midnight. You may also assume that the first one starts earlier. The order of the input arguments is: hr1,
% min1, durmin1, hr2, min2, durmin2.


% Solution 01:

function mv = movies(hr1,min1,durmin1,hr2,min2,durmin2)

 start_time1 = (hr1*60 + min1);
 start_time2 = (hr2*60 + min2);
 diff_start_time = start_time2 - start_time1;

if diff_start_time >= durmin1 && (diff_start_time - durmin1) <= 30
    mv = 1;
else
    mv = 0;
end

% Solution 02:

function cando = movies(hr1,min1,durmin1,hr2,min2,durmin2)
    cando = false;
    endtime =   hr1*60 + min1 + durmin1;    % convert times to minutes
    starttime = hr2*60 + min2;
    if endtime <= starttime && endtime + 30 >= starttime  % so we can compare them
        cando = true;
    end
end


% Alternative solution:

function cando = movies(h1,m1,d1,h2,m2,d2)
    end1 = h1*60 + m1 + d1;
    st2  = h2*60 + m2;
    cando = (end1 <= st2 && end1+30 >= st2);
end
