def conjunction(p,q):
    return(p and q)
print("p     q     ans")
for p in [True, False]:
  for q in [True, False]:
    ans = conjunction(p,q)
    print(p,q, ans)
