
def score(A_score,B_score,s100 = 0,s60 = 230):
    return 0.5*((s60-A_score)*(40/230)+60)+0.5*((s60-B_score)*(40/230)+60)
