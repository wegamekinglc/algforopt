import Base.Threads.@spawn


function sub_func()::Float64
    values::Array{Float64, 1} = randn(Float64, 20000000)
    total_values = sum(values)
end


function main()
    tasks = []
    for i = 1:500
        t = @spawn sub_func()
        push!(tasks, t)
    end
    for t in tasks
        wait(t)
    end
end

@time main()