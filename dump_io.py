import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
sg=d["definitions"]["subgraphs"][0]
print("SG INPUTS")
for x in sg.get("inputs",[]):
 print(json.dumps(x,ensure_ascii=False))
print("SG OUTPUTS")
for x in sg.get("outputs",[]):
 print(json.dumps(x,ensure_ascii=False))
print("INNODE_FULL",json.dumps(sg.get("inputNode"),ensure_ascii=False))
print("OUTNODE_FULL",json.dumps(sg.get("outputNode"),ensure_ascii=False))
