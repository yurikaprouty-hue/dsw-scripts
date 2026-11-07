import json, glob, urllib.request
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
obj=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
sg=d["definitions"]["subgraphs"][0]
for n in sg["nodes"]:
 if n.get("id") in (138,139):
  t=n["type"]
  print(n["id"],repr(t),"in_obj=",t in obj)
