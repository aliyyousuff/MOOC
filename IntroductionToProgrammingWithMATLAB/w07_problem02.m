% Problem 02: Write a function called May2015 that returns a struct vector (row or column) whose elements
% correspond to the days of May, 2015. Each struct should contain three fields with these (exact)
% field names: “month”, “date”, and “day” (all lower case).

% Solution:

function m = May2015
m.month = 'May',m.date = 1,m.day = 'Fri';
m(2).month = 'May',m(2).date = 2,m(2).day = 'Sat'
m(3).month = 'May', m(3).date = 3,m(3).day = 'Sun'
m(4).month = 'May',m(4).date = 4,m(4).day = 'Mon'
m(5).month = 'May',m(5).date = 5,m(5).day = 'Tue'
m(6).month = 'May',m(6).date = 6,m(6).day = 'Wed'
m(7).month = 'May',m(7).date = 7,m(7).day = 'Thu'
m(8).month = 'May',m(8).date = 8,m(8).day = 'Fri'
m(9).month = 'May',m(9).date = 9,m(9).day = 'Sat'
m(10).month = 'May',m(10).date = 10,m(10).day = 'Sun'
m(11).month = 'May',m(11).date = 11,m(11).day = 'Mon'
m(12).month = 'May',m(12).date = 12,m(12).day = 'Tue'
m(13).month = 'May',m(13).date = 13,m(13).day = 'Wed'
m(14).month = 'May',m(14).date = 14,m(14).day = 'Thu'
m(15).month = 'May',m(15).date = 15,m(15).day = 'Fri'
m(16).month = 'May',m(16).date = 16,m(16).day = 'Sat'
m(17).month = 'May',m(17).date = 17,m(17).day = 'Sun'
m(18).month = 'May',m(18).date = 18,m(18).day = 'Mon'
m(19).month = 'May',m(19).date = 19,m(19).day = 'Tue'
m(20).month = 'May',m(20).date = 20,m(20).day = 'Wed'
m(21).month = 'May',m(21).date = 21,m(21).day = 'Thu'
m(22).month = 'May',m(22).date = 22,m(22).day = 'Fri'
m(23).month = 'May',m(23).date = 23,m(23).day = 'Sat'
m(24).month = 'May',m(24).date = 24,m(24).day = 'Sun'
m(25).month = 'May',m(25).date = 25,m(25).day = 'Mon'
m(26).month = 'May',m(26).date = 26,m(26).day = 'Tue'
m(27).month = 'May',m(27).date = 27,m(27).day = 'Wed'
m(28).month = 'May',m(28).date = 28,m(28).day = 'Thu'
m(29).month = 'May',m(29).date = 29,m(29).day = 'Fri'
m(30).month = 'May',m(30).date = 30,m(30).day = 'Sat'
m(31).month = 'May',m(31).date = 31,m(31).day = 'Sun'
end



% Alternative solution:

function sub_May2015
    days = ['Thu'; 'Fri'; 'Sat'; 'Sun'; 'Mon'; 'Tue'; 'Wed' ];
    for ii = 1:31
        m(ii).month = 'May';
        m(ii).date = ii;
        m(ii).day = days(rem(ii,7)+1,:);  % +1 is needed because 0 is an invalid index
    end
end

