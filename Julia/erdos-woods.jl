function erdos_woodsQ(a,n)
  list = [j for j in a:a+n]
  for i in list
    if gcd(a,i)==1  && gcd(a+n,i)==1
      return false
    else
      end
  end
  return true
end

for a = 1:10000000
  if erdos_woodsQ(a,22)
    print(a)
    break
  else
    end
end
