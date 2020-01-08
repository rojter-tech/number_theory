# RSATools.jl
#=
General notation
p   : large prime number
q   : another large prime number
m   : p x q
k   : (p-1) x (q-1)
e   : a large number relativley prime to k
W   : converted message, relativley prime to m
      and less than m

Base equation
eq  : ex - ky = 1

Public shared
e, m
=#

__precompile__()
module RSATools
    using Primes

    function EncryptionParams()

        function gen_primes(lo::Int, hi::Int)
            return primes(lo,hi)
        end

        function prime_pair(generated_primes)
            prime_one = rand(generated_primes)
            prime_two = rand(generated_primes)
            while prime_two == prime_one
                prime_two = rand(generated_primes)
            end
            return (prime_one,prime_two)
        end

        function gen_e(k)
            e = rand(100000:200000)
            while gcd(e,k) != 1
                e = rand(100000:200000)
            end
            return e
        end

        secret_primes = prime_pair(gen_primes(10000,20000))
        p = secret_primes[1]
        q = secret_primes[2]
        m = p*q
        k = (p-1)*(q-1)
        e = gen_e(k)
        
        return p, q, m, k, e
    end

    p, q, m, k, e = EncryptionParams()

    function encrypt(Msg::String)
        W = Vector{Int}()
        C = Vector{Int}()
        for chr in Msg
            w = Int(chr)
            append!(W, w)
            append!(C, mod(w^e,m))
        end
        
        return C
    end

    function decrypt()
        Nothing
    end

    export encrypt, decrypt, m, e
end