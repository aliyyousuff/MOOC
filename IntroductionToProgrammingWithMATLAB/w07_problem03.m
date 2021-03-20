% Problem 03: Write a function called June2015 that returns a cell array of dimensions 30-by-3, whose rows
% correspond to the days of June, 2015. The three elements of each row must be set as follows:

% Solution:

function t1 = June2015
t1 = cell(30,3);
for i = 1:length(t1)
    t1{i} = 'June';
    
    
end

ot = 1:30;
ott = ot';
ottc = num2cell(ott);
t1(1:end,2) = ottc;
t1(1:7:29,3) = {'Mon'};
t1(2:7:30,3) = {'Tue'};
t1(3:7:30,3) = {'Wed'};
t1(4:7:25,3) = {'Thu'};
t1(5:7:26,3) = {'Fri'};
t1(6:7:27,3) = {'Sat'};
t1(7:7:28,3) = {'Sun'};

% Alternative solution:

function m = June2015
    days = [ 'Sun'; 'Mon'; 'Tue'; 'Wed'; 'Thu'; 'Fri'; 'Sat'];
    for ii = 1:30
        m{ii,1} = 'June';
        m{ii,2} = ii;
        m{ii,3} = days(rem(ii,7)+1,:);
    end
end


% Alternative solution:

function x = June2015
    % Make vector of dates for June 2015
    t = datetime(2015,6,1:30);
    % Make a cell array from the components of t
    x = cat(1,month(t,'name'),num2cell(day(t)),day(t,'shortname'))';
end

