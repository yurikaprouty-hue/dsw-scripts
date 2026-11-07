import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
sg=d["definitions"]["subgraphs"][0]
print("SG_KEYS",list(sg.keys()))
print("NAME",sg.get("name"))
for key in ("nodes",):
 for n in sg.get(key,[]):
  print("INNER ID",n.get("id"),"TYPE",n.get("type"),"TITLE",n.get("title"))
  wv=n.get("widgets_values")
  if wv is not None: print("  W",json.dumps(wv,ensure_ascii=False)[:500])
print("LINKS",json.dumps(sg.get("links"),ensure_ascii=False)[:1200])
