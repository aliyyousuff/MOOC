# author: aliyyousuf@gmail.com



using Distributions
using DataFrames

srand(1234)

array_1 = zeros(Float64,30,3)

nd1 = Normal(0.0,1.0)
nd2 = Normal(10.0,2.0)

array_1[:,1] = rand(nd1, 30)
array_1[:,2] = rand(nd2, 30)
array_1[:,3] = rand(5:15,30)


println("Column 1 mean: ", mean(array_1[:,1]), ", variance: ", var(array_1[:,1]))
println("Column 2 mean: ", mean(array_1[:,2]), ", variance: ", var(array_1[:,2]))
println("Column 3 mean: ", mean(array_1[:,3]), ", variance: ", var(array_1[:,3]))


df = convert(DataFrame, array_1)

# Change the name of the columns in df


# Reanaming the columns's name of the dataframe:

rename!(df, f => t for (f, t) = zip([:x1, :x2, :x3], [:Var1, :Var2, :Var3]))


# Declaring array df2:

df2 = df[11:end,:]
describe(df2)


# Adding a new column to df2 named "Cat1":
df2[:Cat1] = rand(["GroupA", "GroupB"], 20)


# Declaring another DataFrame named as df3:
df3 = DataFrame(A = 1:20, B = 21:40, C = 41:60)


# Changing some row's values to NA:
df3[10,1] = df3[15,2] = df3[19,3] = NA



#Remove all rows that contain the NA values:

df4 = completecases!(df3)
