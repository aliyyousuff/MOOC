% Problem 07: Consider the definition: function [s1, s2, sums] = sines(pts,amp,f1,f2) . The input,
% pts, is an integer, but amp, f1, and f2 and are not necessarily integers. Output argument s1 is a row
% function when it is given equally spaced arguments that start at zero and extend through f1 periods of the
% sine. (Note that we ask for full periods, so if f1 is an integer, both the first and the last element of s1 will
% be 0 other than a very small rounding error.) The amplitude of the sine wave equals amp. The vector s2 is
% the same as s1 except that s2 contains f2 periods. The vector sums is the sum of s1 and s2. If f2 is
% omitted, then it should be set to a value that is 5% greater than f1. If f1 is omitted also, then it should be
% set to 100. If amp is not provided, then it should default to 1. Finally, if pts is omitted as well, then it should
% be set to 1000. For example, if you run sines without any input arguments and then you plot the third
% output argument, sums, the figure should look like this (if you stretch the plot window horizontally):

% Solution 01:

function [s1 s2 sums] = sines(pts,amp,f1,f2)
    if nargin < 1, pts = 1000;    end
    if nargin < 2, amp = 1;       end
    if nargin < 3, f1 = 100;      end
    if nargin < 4, f2 = f1*1.05;  end
    t = 0 : 2*pi/(pts-1) : 2*pi;
    s1 = amp * sin(f1*t);
    s2 = amp * sin(f2*t);
    sums = s1 + s2;
end

% The sin() function has a full period between 0 and 2*pi.
% To set up the vector t, dividing by (pts-1) is needed
% because n points in a line define (n-1) consecutive segments
% and not n. For example, two points define a single line segment.
% The function call sin(f1*t) will create exactly f1 full periods
% using vector t defined above

