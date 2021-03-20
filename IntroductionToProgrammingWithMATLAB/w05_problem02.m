% Problem 02:  Write a function called letter_grade that takes a positive integer called score as its input argument
% and returns a letter grade according to the following scale: A: 91 and above; B: 81-90; C: 71-80; D: 61-70; F:
% below 61. Remember that to assign a letter to a variable, you need to put it in single quotes, as in: 
% grade = 'A'.

% Solution 01:

% Function for grading


function grade = letter_grade(scores)
if scores >= 91
    grade = 'A';
elseif scores >= 81 && scores <= 90
    grade = 'B';
elseif scores >= 71 && scores <= 80
    grade = 'C';
elseif scores >= 61 && scores <= 70
    grade = 'D';
elseif scores < 61
    grade = 'F';
else
    return;
end
    
% Solution 02:

function G = letter_grade(score)
    if score >= 91
        G = 'A';
    elseif score >= 81
        G = 'B';
    elseif score >= 71
        G = 'C';
    elseif score >= 61
        G = 'D';
    else
        G = 'F';
    end
end
