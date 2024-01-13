def exclusive_disjunction(p,q):
    return (p and Not(q))or(Not(p) and q)
print("p     q     ans")
for p in [True, False]:
  for q in [True, False]:
    ans = exclusive_disjunction(p,q)
    print(p,q, ans)
