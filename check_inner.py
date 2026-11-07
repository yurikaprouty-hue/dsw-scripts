import json, glob, urllib.request
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
obj=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
sg=d["definitions"]["subgraphs"][0]
missing=[]; present=[]
for n in sg["nodes"]:
 t=n["type"]
 (present if t in obj else missing).append((n["id"],t))
print("PRESENT",len(present))
for i,t in sorted(present): print(" OK",i,t)
print("MISSING",len(missing))
for i,t in sorted(missing): print(" NO",i,t)
