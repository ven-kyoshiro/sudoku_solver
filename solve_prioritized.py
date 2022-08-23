from funcs import *
from solve_detarmin import *

import pprint
from copy import deepcopy as dc

"""
# list管理で解くやつ
分岐すべき場所を登録してく、openしたら、２つのそれぞれ、次に泊まるとこまで進めてまた登録する
版面,どこに、分岐数、盤面何個埋まってるか
"""
MAX_ITR = 10000
def priority_func(numcand,numfilled):
    # small -> prioriti hi
    # [0,9] 9~80
    return numcand + numfilled/10000

def count_filled(ans):
    sum_filled = 81
    for i in range(9):
        for j in range(9):
            if ans[i][j]==0:
                sum_filled -=1
    return sum_filled

def update_list(main_list,ans,cand):
    for i in range(9):
        for j in range(9):
            if ans[i][j]==0:
                num_cand = len(cand[i][j])
                if not num_cand ==0:
                    main_list.append([
                        ans,
                        [i,j],
                        cand[i][j],
                        num_cand,
                        count_filled(ans)
                        ])

def solve_prioritized_search(ini_ans):
    ans,cand,status = calc_determin(ini_ans)

    ans_ij_candset_numcand_numfilled = []
    update_list(ans_ij_candset_numcand_numfilled,ans,cand)

    itr_max = MAX_ITR
    for itr in range(itr_max):
        ans_ij_candset_numcand_numfilled.sort(key=lambda x:priority_func(x[3],x[4]))
        read_ans,[i,j],candset,numcand,numfilled = ans_ij_candset_numcand_numfilled.pop(0)
        for c_num in candset:
            base_ans = dc(read_ans)
            base_ans[i][j] = c_num
            ret_ans,cand,status = calc_determin(base_ans)
            if status == "goal" or is_goal(ret_ans) :
                return ret_ans
            elif status == "stop" or status == "success":
                if not is_dead(cand,ret_ans):
                    update_list(ans_ij_candset_numcand_numfilled,ret_ans,cand)
            else:
                raise
    return None


if __name__ == "__main__":
    X = 0
    ini_ans =[
        [X,X,X,8,4,5,X,X,X],
        [X,X,9,X,X,X,1,X,X],
        [X,3,X,X,X,9,X,2,X],
        [4,X,7,X,X,X,X,X,3],
        [5,X,X,X,1,X,X,X,4],
        [2,X,X,X,X,X,9,X,5],
        [X,8,X,3,X,X,X,6,X],
        [X,X,6,X,X,X,7,X,X],
        [X,X,X,5,2,6,X,X,X]
    ]
    final_ans = solve_prioritized_search(ini_ans)
    pprint.pprint(final_ans)

