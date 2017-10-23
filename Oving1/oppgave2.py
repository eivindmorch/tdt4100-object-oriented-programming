def faculty(n):
 result = 1
 while(n > 0):
  result *= n
  n -= 1
 return result

def binomial(n,k):
 return faculty(n)/(faculty(k)*faculty(n-k))

print("Sannsynligheten for to par i Texas Hold'em er: " , binomial(13,2)*binomial(4,2)*binomial(4,2)*binomial(11,1)*binomial(4,1)/2598960)
