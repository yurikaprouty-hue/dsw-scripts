import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
sg=d["definitions"]["subgraphs"][0]
L=sg["links"]
print("SAMPLE",json.dumps(L[0],ensure_ascii=False))
print("NLINKS",len(L))
for x in L:
 print(json.dumps(x,ensure_ascii=False))
