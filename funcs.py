'''
one = '12356'#str 1~9# can be set
cand = [[one,one,one,...,one],...,[one,one,one,...,one]]

'''

sepa = '|'
def show_cand(cand,ans=None):
    tx = ''
    tx += sepa*(9*(3+1)+1) +'\n'
    for ans_i,cc in enumerate(cand):
        # 行
        for i3 in range(3):
            tx +=sepa
            for ans_j,one in enumerate(cc):
                for i1 in range(3):
                    j = i3*3+i1+1
                    if str(j) in one or j in one:
                        t = str(j)
                    else:
                        t=' '
                    if ans!=None:# ansが既に決定済みの場合
                        if ans[ans_i][ans_j]!=0:
                            t = str(ans[ans_i][ans_j])
                    tx += t
                tx += sepa
            tx += '\n'
        tx += sepa*(9*(3+1)+1) +'\n'
    tx += '\n'
    print(tx)


def get_ban_set(ans,i,j):
    ban_set = set(ans[i])
    ban_set = ban_set | set([ans[ii][j] for ii in range(9)])
    st_i = (i//3)*3
    st_j = (j//3)*3
    box_ban_list = [ans[st_i+ii][st_j+jj] for ii in range(3) for jj in range(3)]
    ban_set = ban_set | set(box_ban_list)
    return ban_set

import copy
def calc_cand(ans):
    U = {1,2,3,4,5,6,7,8,9}
    cand = []
    for i in range(9):
        row = []
        for j in range(9):
            ban_set = get_ban_set(ans,i,j)
            row.append(U-ban_set)
        cand.append(row)
    return cand

def is_dead(cand,ans):
    all_cand = 0
    for cc,an in zip(cand,ans):
        for c,a in zip(cc,an):
            if a == 0: # 空欄箇所の候補数
                all_cand += len(c)
    return all_cand == 0

def get_unique_num(valid_cand,i,j):
    # 重そう
    knock_out_cand = copy.deepcopy(valid_cand)
    knock_out_cand[i][j] = set()
    # 自分以外の集合の和集合を計算Tset
    colT = set()
    rowT = set()
    for ij in range(9):
        colT = colT | knock_out_cand[i][ij]
        rowT = rowT | knock_out_cand[ij][j]
    boxT = set()
    st_i = (i//3)*3
    st_j = (j//3)*3
    for ii in range(st_i,st_i+3):
        for jj in range(st_j,st_j+3):
            boxT = boxT | knock_out_cand[ii][jj]

    # 自分以外の和の集合のなかにはない自分i,jの数字を返す
    for Tset in [colT,rowT,boxT]:
        cup = valid_cand[i][j] | Tset
        unique_set = cup - Tset
        l = len(unique_set)
        #assert l<2,f'(i,j):({i},{j})１つのマスに２つ以上のユニーク候補が期待されています'
        if l == 1:
            return [list(unique_set)[0]]
    return []




import copy
def find_puts(cand,ans):
    # ansが決まってるところを空集合に
    valid_cand = copy.deepcopy(cand)
    for i in range(9):
        for j in range(9):
            if ans[i][j] > 0:
                valid_cand[i][j] = set()

    # 候補がもう１つしかない場合
    founds = []
    for i in range(9):
        for j in range(9):
            if len(valid_cand[i][j])==1:
               founds.append([i,j,list(valid_cand[i][j])[0]])
    # ansが決まってるところに自分自身を入れとく
    for i in range(9):
        for j in range(9):
            if ans[i][j] > 0:
                valid_cand[i][j] = set([ans[i][j]])


    # 集合の中で，自分だけが持ってる数字がある
    for i in range(9):
        for j in range(9):
            if ans[i][j]==0:
                new = get_unique_num(valid_cand,i,j)
                if len(new)>0:
                    founds.append([i,j,new[0]])
    return founds

def is_end(ans):
    # 0がなければ終了はしてる
    for an in ans:
        for a in an:
            if a == 0:
                return False
    return True

def is_goal(ans):
    all_set = set([1,2,3,4,5,6,7,8,9])
    for i in range(9):
        if not set(ans[i]) == all_set:
            return False
        if not set([ans[j][i] for j in range(9)]) == all_set:
            return False
    for i in range(3):
        for j in range(3):
            box_set = set()
            for ii in range(3):
                mini_set = set([ans[i*3+ii][j*3+jj] for jj in range(3)])
                box_set = box_set | mini_set
            if not box_set == all_set:
                return False
    return True
    

if __name__ == "__main__":
    # test of show_cand
    one = '12346789'
    one = {1,2,3,4,5,6,7,8,9}
    cand = [[one]*9]*9
    show_cand(cand)

    # test of calc_cand
    X = 0
    #ans = [
    #        [5,X,X,3,X,1,X,X,X],
    #        [X,6,X,X,2,X,X,7,X],
    #        [X,X,7,X,X,X,8,X,X],
    #        [X,4,X,X,X,X,X,5,X],
    #        [3,X,X,X,5,X,X,X,9],
    #        [X,2,X,X,X,X,X,8,X],
    #        [X,X,6,X,X,X,9,X,X],
    #        [X,8,X,X,3,X,X,2,X],
    #        [X,X,X,9,X,6,X,X,7]
    #        ]

   
    ans = [
            [5,9,8,3,7,1,2,6,4],
            [4,6,3,8,2,9,1,7,5],
            [2,1,7,4,6,5,8,9,3],
            [8,4,9,6,1,3,7,5,2],
            [3,7,1,2,5,8,6,4,9],
            [6,2,5,7,9,4,3,8,1],
            [7,3,6,5,4,2,9,1,8],
            [9,8,4,1,3,7,5,2,6],
            [1,5,2,9,8,6,4,3,7]
            ]
    print('is_end,True',is_end(ans))
    print('is_goal,True',is_goal(ans))
    ans[0][0] = 9
    print('is_end,True',is_end(ans))
    print('is_goal,False',is_goal(ans))
   
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
    print('is_end,False',is_end(ans))
    print('is_goal,False',is_goal(ans))
    cand = calc_cand(ans)
    print(is_dead(cand,ans))
    show_cand(cand,ans)
    print(find_puts(cand,ans))

