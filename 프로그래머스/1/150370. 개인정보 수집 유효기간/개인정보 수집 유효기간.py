def cal_date(day, term):
    yyyy, mm, dd = day.split(".")
    yyyy, mm, dd = int(yyyy), int(mm), int(dd)
    
    return 12 * 28 * yyyy + 28 * (mm + term) + dd - 1
    

def solution(today, terms, privacies):
    today_dates = cal_date(today, 0) + 1
    answer = []
    term_dict = {term.split(" ")[0]: int(term.split(" ")[1]) for term in terms}
    for ind, privacy in enumerate(privacies):
        day, temp_term = privacy.split(" ")
        temp_dates = cal_date(day, int(term_dict[temp_term]))
        if today_dates > temp_dates: 
            answer.append(ind+1)
            
    return answer