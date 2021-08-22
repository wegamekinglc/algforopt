using Base.MathConstants

function bracket_minmimum(f, x=0; s=1e-2, k=2.0)
    a, ya = x, f(x)
    b, yb = a + s, f(a + s)
    if yb > ya
        a, b = b, a
        ya, yb = yb, ya
        s = -s
    end

    while true
        c, yc = b + s, f(b + s)
        if yc > yb
            return a < c ? (a, c) : (c, a)
        end
        a, ya, b, yb = b, yb, c, yc
        s *= k
    end
end


function fibonacci_search(f, a, b, n; ϵ=0.02)
    s = (1 - √5) / (1 + √5)
    ρ = 1 / (φ * (1 - s^(n + 1)) / (1 - s^n))
    d = ρ * b + (1 - ρ) * a
    yd = f(d)
    for i in 1:n-1
        if i == n - 1
            c = ϵ * a + (1 - ϵ) * d
        else
            c = ρ * a + (1 - ρ) * b
        end
        yc = f(c)
        if yc < yd
            b, d, yd = d, c, yc
        else
            a, b = b, c
        end
        ρ = 1 / (φ * (1 - s^(n - i + 1)) / (1 - s^(n - i)))
    end
    return a < b ? (a, b) : (b, a)
end


function golden_section_search(f, a, b, n)
    ρ = φ-1
    d = ρ * b + (1 - ρ) * a
    yd = f(d)
    for i in 1:n-1
        c = ρ * a + (1 - ρ) * b
        yc = f(c)
        if yc < yd
            b, d, yd = d, c, yc
        else
            a, b = b, c
        end
    end
    return a < b ? (a, b) : (b, a)
end


f(x) = (x - 3.0) ^ 2

using BenchmarkTools
BenchmarkTools.DEFAULT_PARAMETERS.seconds = 10

@benchmark bracket_minmimum(f)

a, b = bracket_minmimum(f)

@benchmark fibonacci_search(f, a, b, 100)