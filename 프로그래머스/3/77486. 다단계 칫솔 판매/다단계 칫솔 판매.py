def sol(man, money, tree, ans):
    money_10 = (money*0.1) // 1
    money_90 = money - money_10
    
    ans[man] += money_90
    
    if tree[man] != '-' and money_10 >= 1:
        sol(tree[man], money_10, tree, ans)
    else:
        return 
    
def solution(enroll, referral, seller, amount):
    n = len(enroll)
    tree = { enroll[i]:referral[i] for i in range(n) }
    answer = { enroll[i] : 0 for i in range(n)}
    m = len(seller)
    
    for i in range(m):
        sol(seller[i], amount[i]*100, tree, answer)
    
    
    return list(answer.values())