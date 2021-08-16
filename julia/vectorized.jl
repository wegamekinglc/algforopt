f(x) = 3x.^2 .+ 5x .+ 2

vec(x) = f(2x.^2 + 6x.^3 - sqrt.(x))

newvec(x) = f.(2 .*x.^2 .+ 6 .* x.^3 .- sqrt.(x))

function devec(x)
    x_new = x[:]
    @simd for i in eachindex(x)
        @inbounds x_bar = x[i]
        x_new[i] = f(2x_bar^2 + 6x_bar^3 - sqrt(x_bar))
    end
    return x
end

using BenchmarkTools
BenchmarkTools.DEFAULT_PARAMETERS.seconds = 10

x = abs.(randn(10^6))

t_vec = @benchmark vec(x)