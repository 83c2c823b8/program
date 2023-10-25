function first_zero(p)
  fibo=[1,1]
    while true
      if fibo[end] == 0
        break
      else
        push!(fibo,(fibo[end-1]+ fibo[end])%p)
      end
    end
  return length(fibo)
end

first_zero(71)