% Write a function called light_time that takes as input a row vector of distances in miles and
% returns two row vectors of the same length. Each element of the first output argument is the time
% in minutes that light would take to travel the distance specified by the corresponding element of
% the input vector. To check your math, it takes a little more than 8 minutes for sunlight to reach
% Earth which is 92.9 million miles away. The second output contains the input distances converted
% to kilometers. Assume that the speed of light is 300,000 km/s and that one mile equals 1.609 km.

% solution 01:

function [time distance] = light_time(miles)
 time = miles/((300000/1.609)*60)
 distance = miles * 1.609
end

% Solution 02:

function [mins km] = light_time(mile)
 
  km = mile * 1.609;
  mins =  km / 3e5 / 60;
end
