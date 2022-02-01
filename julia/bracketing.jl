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


function quadratic_fit_search(f, a, b, c, n)
    ya, yb, yc = f(a), f(b), f(c)
    for i in 1:n-3
        x = 0.5 * (ya * (b^2 - c^2) + yb * (c^2 - a^2) + yc * (a^2 - b^2)) / (ya * (b -c) + yb * (c - a) + yc * (a - b))
        yx = f(x)

        if x >= b
            if yx > yb
                c, yc = x, yx
            else
                a, ya, b, yb = b, yb, x, yx
            end
        elseif x < b
            if yx > yb
                a, ya = x, yx
            else
                c, yc, b, yb = b, yb, x, yx
            end
        end
    end
    return (a, b, c)
end


function bisection(df, a, b; ϵ=1e-14)
    if a > b
        a, b = b, a
    end

    ya, yb = df(a), df(b)
    if ya == 0
        b = a
    end
    if yb == 0
        a = b
    end

    while b - a > ϵ
        x = (a + b) / 2
        y = df(x)
        if y == 0
            a, b = x, x
        elseif y * ya > 0
            a = x
        else
            b = x
        end
    end
    return (a, b)
end


function bracket_sign_change(df, a, b; k=2)
    if a > b
        a, b = b, a
    end

    center, half_width = (a + b) / 2, (b - a) / 2
    while df(a) * df(b) > 0
        half_width *= k
        a = center - half_width
        b = center + half_width
    end

    return(a, b)
end


f(x) = (x - 3.0) ^ 2
df(x) = 2.0 * (x - 3.0)

using BenchmarkTools
BenchmarkTools.DEFAULT_PARAMETERS.seconds = 20

@benchmark bracket_minmimum(f)

a, b = bracket_minmimum(f)

@benchmark fibonacci_search(f, a, b, 100)

@benchmark quadratic_fit_search(f, 0.0, 2.0, 5.0, 10)
