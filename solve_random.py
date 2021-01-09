from funcs import *
from solve_detarmin import *

def get_altanative_list(cand,ans):
    '''
    returns 
    [
        [i,j,num_A],
        [i,j,num_B],...
        [i,j,num_X]
    ]
    '''
    all_list = []
    N = 2
    for i in range(9):
        for j in range(9):
            if ans[i][j]==0:
                if len(cand[i][j]) == N:
                    for num in cand[i][j]:
                        all_list.append([i,j,num])
    return all_list

import random
def one_trial(ans,debug=False):
    if debug:
         pprint.pprint(ans)
    while True:
        ans,cand,status = calc_determin(ans)
        if debug:
            pprint.pprint(ans)

        # 終了はんてい
        if is_end(ans): 
            if is_goal(ans):
                status = 'goal'
                if debug:
                    print("Success!")
            else:
                status = 'dead'
                if debug:
                    print("Dead end!")
            return ans,status
        if status == 'dead':
            if debug:
                print("Failue")
            return ans,statue


        all_list = get_altanative_list(cand,ans)
        if len(all_list)==0:
            status = 'cannot_continue'
            if debug:
                print(cand)
            return ans,status

        [i,j,num] = random.choice(all_list)
        ans[i][j]=num

import pprint
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
    for i in range(10000):
        ans,status = one_trial(copy.deepcopy(ini_ans))
        print(f'[random search] trial:{i} result:{status}')
        if status =='goal':
            pprint.pprint(ans)
            break
