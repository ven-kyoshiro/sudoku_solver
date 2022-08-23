import csv
import pathlib
import time
import numpy as np
from solve_random import solve_random
from solve_prioritized import solve_prioritized_search
from funcs import show_cand
import pprint

def read_from_csv(p):
    with open(p,mode="r") as f:
        reader = list(csv.reader(f))
    return [[ float(r) if r!= "" else 0. for r in row ]for row in reader]

p_temp = pathlib.Path('problems')
result_dict = dict(
        name=[],
        method=[],
        is_success=[],
        time=[]
        )

solvers = [solve_prioritized_search,solve_random]
methods = ["prioritized","random"]
for solver,method in zip(solvers,methods):
    for p in list(p_temp.iterdir()):
        result_dict["name"].append(str(p).split("/")[-1].split(".")[0])
        print(result_dict["name"][-1],end=": ")
        ini_ans = read_from_csv(p)
        st = time.time()
        ret =solver(ini_ans)
        result_dict["time"].append(time.time()-st)
        result_dict["method"].append(method)
        if ret == None:
            result_dict["is_success"].append(False)
            print("Failure!")
        else:
            result_dict["is_success"].append(True)
            print("Success!")
            if result_dict["name"][-1] == "marumen_hard":
                pprint.pprint(ret)

success =[result_dict["is_success"][i] for i,mth in enumerate(result_dict["method"]) if mth == method]
print(f"{method} Success={sum(success)}/{len(success)}",)
tm =[result_dict["time"][i] for i,mth in enumerate(result_dict["method"]) if mth == method]
print(f"{method} time max={np.max(tm)} median={np.median(tm)}",)
