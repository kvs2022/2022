def disjunction(p,q):
    return(p or q)
print("p     q     ans")
for p in [True, False]:
  for q in [True, False]:
    ans = disjunction(p,q)
    print(p,q, ans)
