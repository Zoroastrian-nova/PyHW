#提交分数要求。A/B榜机制，加权分数0.5*A榜+0.5*B榜，baseline-A榜248、B榜258、加权分数253。以加权分数为准，换算为百分制，rmse=0、对应100分， rmse=230、对应60分。其余分数线性插值。
def score(A_score,B_score = A_score,s100 = 0,s60 = 230):
    return 0.5*((s60-A_score)*(40/230)+60)+0.5*((s60-B_score)*(40/230)+60)
