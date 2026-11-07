import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
sg=d["definitions"]["subgraphs"][0]
for n in sorted(sg["nodes"],key=lambda x:x.get("id",0)):
 i=n.get("id")
 wv=n.get("widgets_values")
 wn=n.get("widgets_values_named")
 print("NODE",i,n.get("type"))
 if wv is not None: print(" WV",json.dumps(wv,ensure_ascii=False)[:400])
 if wn is not None: print(" WN",json.dumps(wn,ensure_ascii=False)[:400])
