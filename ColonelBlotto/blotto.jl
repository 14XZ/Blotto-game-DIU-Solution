# https://github.com/Soben713/ColonelBlotto
# yezheng: do necessary modification in payoff(  ) and Model( )

using JuMP, Clp
using Mosek
#using DelimitedFiles
using CSV, DataFrames

#
# @param k: the battlefield
# @p

"""
The payoff function of the first player (we assume that the game is zero-sum)

@param k: the battlefield index
@param x: the number of troops that player A puts in the battlefield
@param y: the number of troops that player B puts in the battlefield
"""
function payoff(k,x,y)
    if x<y
        return -k
    elseif x>y
        return k
    else
        return 0
    end
end


m = Model(solver=ClpSolver())
K=10   # The total number of battlefields
N=110      # Troops of player A
N2=100    # Troops of player B
#K=2   # The total number of battlefields
#N=4      # Troops of player A
#N2=3    # Troops of player B

# Read the proof of the LP in the following paper,
# https://arxiv.org/abs/1612.04029

@variable(m, U)
@variable(m, D[0:K,0:N2])
@variable(m, W[0:K,0:N2,0:N2])
@variable(m, P[1:K,0:N] >= 0)
@variable(m, E[0:K,0:N,0:N] >= 0)

@objective(m, Min, U)

for b in 1:K
    for t in 0:N2
        for t2 in 0:t
            @constraint(m, D[b, t] >= D[b-1, t2] + W[b-1, t2, t])
        end
    end
end

for b in 0:K-1
    for x in 0:N2
        for y in x:N2
            @constraint(m, W[b, x, y] == -sum(P[b+1, i]*payoff(b, i, y-x) for i=0:N))
        end
    end
end

for t in 0:N2
    @constraint(m, D[0,t]==0)
end

@constraint(m, D[K,N2]<=U)

for b in 1:K
    for t in 0:N
        @constraint(m, P[b,t] == sum(E[b-1,i,t] for i=0:N-t))
    end
end

for b in 1:K-1
    for t in 0:N
        @constraint(m, sum(E[b-1, t-i, i] for i=0:t) == sum(E[b, t, i] for i=0:N-t))
    end
end

@constraint(m, sum(E[0, i, j] for i=1:N for j=0:N-i) == 0)
@constraint(m, sum(E[0, 0, j] for j=0:N) == 1)
@constraint(m, sum(E[K-1, j, N-j] for j=0:N) == 1)

solve(m)

println("Player A's optimum payoff: $(-getvalue(U))")
println("P[i,j] determines the probability that player A puts j troops in the i-th battlefield")
val = getvalue(P);
#val =convert(Array{Float64,2, Tuple{UnitRange{Int64},UnitRange{Int64}} }, val)

println(val);

val2 = zeros(Float64, K, N);
for i in 1:K
    for j in 1:N
        val2[i,j] = val[i,j];
    end
end

#open("distri.csv","w") do io
#    for i in 1:K
#        CSV.write(io,val[i,:]);
#    end
#end
#------
filename = "distri_"*string(N)*"_"*string(N2)*".csv"
println(filename)
#writedlm(filename, val, ',')
#------
CSV.write(filename,  DataFrame(val2), writeheader=false)