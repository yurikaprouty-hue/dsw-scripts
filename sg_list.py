import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
sg=d["definitions"]["subgraphs"][0]
for n in sorted(sg["nodes"],key=lambda x:x.get("id",0)):
 print(n.get("id"),n.get("type"),n.get("title") or "")
print("INNODE",json.dumps(sg.get("inputNode"),ensure_ascii=False)[:300])
print("OUTNODE",json.dumps(sg.get("outputNode"),ensure_ascii=False)[:300])
