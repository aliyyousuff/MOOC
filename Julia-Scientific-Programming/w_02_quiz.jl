using Plots
pyplot() # Use PyPlot as a backend (may already be the default)

#x = collect(1:7)
#y = []

#for item in x
    #push!(y, 2 - 2*item + item^2/4)
#end



#plot(x,y)
#plot!(x, y, marker = :diamond, linewidth=2)
#plot!(title = "Sample plot", leg=false)

x = [1 2 3 4 5 6]'
#y = (x-3).^2/4
y = []

for item in x
    push!(y, (item-3).^2/4)
end

plot(x,y, marker = :hex, leg=false, linewidth = 2, linecolor=:black)
plot!(title="Plot for graded quiz")
gui()    # To show plot on atom