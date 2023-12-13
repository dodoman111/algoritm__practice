def solution(bandage, health, attacks):
    health_limit  = health
    answer = 0
    success_action = 0
    for t in range(1, attacks[-1][0] + 1):
        for attack in attacks :
            if t == attack[0] :
                attacks.pop(0)
                health -= attack[1]
                success_action = 0
                if health <= 0 :
                    return -1
                break
            else:
                health += bandage[1]
                success_action += 1
                if success_action == bandage[0]:
                    health += bandage[2]
                    success_action = 0
                if health >= health_limit:
                    health = health_limit
                break
            if health <= 0 :
                return -1
            
    return health