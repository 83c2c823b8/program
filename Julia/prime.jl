function myisprime(n)
  if n <= 1
    return false
  elseif n == 2
    return true
  elseif n%2 == 0
    return false
  else
    i=0
    while 2*i+3 < sqrt(n)
      if n%(2*i+3) == 0
        return false
      else
        i = i + 1
      end
    end
  return true
  end
end

function myprime(n)
  