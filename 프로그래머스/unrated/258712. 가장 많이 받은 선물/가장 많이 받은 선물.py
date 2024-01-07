def get_matrix(friends, gifts):
    friends_cnt = len(friends)
    gift_matrix = [[0] * friends_cnt for i in range(friends_cnt) ]
    index_info = {name:ind for ind, name in enumerate(friends)}
    gift_set = [gift.split() for gift in gifts]
    for ind, name in enumerate(friends):
        for i, j in gift_set:
            if i == name:
                temp_index = index_info[j]
                gift_matrix[ind][temp_index] += 1
    give_lst, recieve_lst = [0] * friends_cnt, [0] * friends_cnt
    for i in range(friends_cnt):
        for j in range(friends_cnt):
            recieve_lst[j] += gift_matrix[i][j]
            give_lst[i] += gift_matrix[i][j]
    gift_index = [give - recieve for give, recieve in zip(give_lst, recieve_lst)]
    
    return gift_matrix, gift_index, friends_cnt


def solution(friends, gifts):
    answer = {ind: 0 for ind, name in enumerate(friends)}
    
    gift_matrix, gift_index, friends_cnt = get_matrix(friends, gifts)
    for i in range(friends_cnt):
        for j in range(friends_cnt):
            if i == j:
                continue
            if (gift_matrix[i][j] == gift_matrix[j][i]):
                if gift_index[i] - gift_index[j] == 0:
                    continue
                elif gift_index[i] - gift_index[j] > 0:
                    answer[i] += 1
                else:
                    answer[j] += 1
            elif gift_matrix[i][j] - gift_matrix[j][i] > 0:
                answer[i] += 1
            else:
                answer[j] += 1
        
    return max([j for i, j in answer.items()]) // 2