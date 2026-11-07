import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
print("FILES",ps)
d=json.load(open(ps[0]))
for n in d["nodes"]:
 print("ID",n.get("id"),"TYPE",n.get("type"),"TITLE",n.get("title"))
 if n.get("id")==148:
  print(" KEYS",list(n.keys()))
  print(" PROPS",json.dumps(n.get("properties",{}),ensure_ascii=False)[:500])
