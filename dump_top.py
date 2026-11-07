import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
print("TOP_KEYS",list(d.keys()))
for k,v in d.items():
 if isinstance(v,(list,dict)):
  print(k,"LEN",len(v))
 else:
  print(k,"=",repr(v)[:120])
if "definitions" in d:
 print("DEFS",json.dumps(d["definitions"],ensure_ascii=False)[:1500])
if "extra" in d:
 print("EXTRA",json.dumps(d["extra"],ensure_ascii=False)[:800])
