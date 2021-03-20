# __author__:aliyousuuf@gmail.com

# This file contains all the codes from lecture, pactise quizzes, and assesment
# of week 02.

# Assume that we've downloaded the EBola data from wiki's website,
# and save it as csv format under file name epidata.csv.

epidata = readdlm("epidata.csv", ',')

col1 = epidata[:,1]
for date = 1:54
    col1[date] = DateTime(col1[date], "d u y")
end

#println(col1)
#println(Dates.datetime2rata(col1[1]))

dayssincemar22(x) = Dates.datetime2rata(x)
epidays = Array(Int64, 54)
for i = 1:54
    epidays[i] = dayssincemar22(col1[i])
end

epidata[:,1] = epidays
writedlm("epidata_converted.csv", epidata, ',')
epidata_converted = readdlm("epidata_converted.csv",',')

# Now we're going to plot epidemic days vs all the cases.

epidays = epidata_converted[:,1]
allcases = epidata_converted[:,2]

# akkcases contains two types of data--string and Int--we've to convert them
# into one type.

for item = 1:54
    if typeof(allcases[item,1]) == SubString{String}
        allcases[item,1] = parse.(Int64,replace(allcases[item,1], ",", ""))
    end
end

using Plots
#Plots.PyPlotBackend()
#pyplot()
#using Gadfly
#plot(epidays, allcases)

# Week_02_Practice Quiz: Q.2

f(x) = 3 * x^2 + 6 * x - 9
for x = -5:5
  #println((,x, ", ", f(x), ")")
end
using Plots
#plot(f, -4, 3) # plot f over [-4,4]
#plot!(zero, -4, 3)

#Week_02_Practice Quiz: Q.3

data = [1.6800483  -1.641695388;
        0.501309281 -0.977697538;
        1.528012113 0.52771122;
        1.70012253 1.711524991;
        1.992493625 1.891000015;
        2.706075824 -0.463427794;
        2.994931927 -0.443566619;
        3.491852811 -1.275179133;
        3.501191722 -0.690499597;
        4.459924502 -5.516130799;
        4.936965851 -6.001703074;
        5.023289852 -8.36416901;
        5.04233698 -7.924477517;
        5.50739285 -10.77482371;
        5.568665171 -10.9171878]

x,y = data[:,1] , data[:,2]
Plots.PyPlotBackend()
#plot(x, y, linetype = :scatter, leg = false)

#Week_02_Practice Quiz: Q.7
n = 20
x = sort(rand(20)); y = rand(20)
#plot!(x,y, leg=false, title = "A sample plot")

# gui()

# replace all the instances of "-" and "--" into 0, and "," into "".
row,col = size(epidata_converted)
for r = 1:row
    for c = 1: col
        if typeof(epidata_converted[r,c]) == SubString{String}
            epidata_converted[r,c] = replace(epidata_converted[r,c], ",", "")
            if isnumber(string(epidata_converted[r,c])) == false
                epidata_converted[r,c] = 0
            end
        end
    end
end

# Convert all the string into integer
for r = 1:row
    for c = 1: col
       if isnumber(string(epidata_converted[r,c])) == true
           epidata_converted[r,c] = parse(Int64,string(epidata_converted[r,c]))
       end
   end
end
