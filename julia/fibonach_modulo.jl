function my_fibonach_period(p)
  fibo=[1,1]
    while true
      if fibo[end] == 0
        break
      else
        push!(fibo,(fibo[end-1]+ fibo[end])%p)
      end
    end
    nT = length(fibo)
    if fibo[end-1] == 1
      d = 1
    elseif fibo[end-1]^2%p == 1
      d = 2
    else
      d = 4
    end
  return [p,nT, d*nT, d]
end

# for i in 1:100
#   println(my_fibonach_period(prime(n)))

print([my_fibonach_period(prime(i)) for i in 1:30])