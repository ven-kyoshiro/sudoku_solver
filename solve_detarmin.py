from funcs import *

def step(ans,debug=False):
    cand = calc_cand(ans)
    status = is_dead(cand,ans)
    if status == 'dead':
        return ans,cand,status
    if debug:
        show_cand(cand,ans)
    founds = find_puts(cand,ans)
    if len(founds)==0:
        status = 'stop'
        return ans,cand,status
    else:
        status = 'success'
        if debug:
            print('founds',founds)
        for [i,j,num] in founds:
            ans[i][j] = num
    return ans,cand,status

def calc_determin(ans,debug=False):
    while True:
        ans,cand,status = step(ans,debug=debug)
        if debug:
            print(status)
        if status == 'stop':
            break
        else:
            if debug:
                print(ans)
    return ans,cand,status


if __name__ == "__main__":
    X = 0
    ans =[
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
    ans,cand,status = calc_determin(ans)
    show_cand(cand,ans)
