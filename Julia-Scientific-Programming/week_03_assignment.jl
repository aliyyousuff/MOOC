# author: aliyyousuf@gmail.com

# assignment of week_03.


data_to_fit = readdlm("Week3_PR_Data.dat",',')

# Converting data into Float64

data_to_fit_2 = zeros(Float64, 15,2)
for r = 1:15
    for c = 1
        data_to_fit_2[r,c] = parse(Float64,split(data_to_fit[r,c])[1])
        data_to_fit_2[r,2] = parse(Float64,split(data_to_fit[r,c])[2])
    end
end

# "For loop" to show all the values of data:

for r = 1:15
    for c = 1:2
        #println(data_to_fit_2[r,c])
    end
end

# assign the values from first column to variable x
# and second column to variable y.

x = data_to_fit_2[:,1]
y = data_to_fit_2[:,2]




using Plots
pyplot()
plot(x,y, title = "Model versus Data",label = "Actual values from given data",
xlabel = " x values",
ylabel = "y values",
line =:scatter)
gui()

function parab_fit(x)
    return a * (x)^2 + b * x + c
end

a = -0.789
b = 2.988
c = -1.5
plot!(parab_fit,title = "Model versus Data",-10,10,
label = "Model values")
gui()
