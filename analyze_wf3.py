import glob,json
p=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03*")[0]
d=json.load(open(p))
for n in d["nodes"]:
 print("====NODE", n.get("id"), n.get("type"), n.get("title"))
 for i,v in enumerate(n.get("widgets_values") or []):
  print("  [%d] %r" % (i,v))
 print("  inputs:", [(x.get("name"),x.get("type")) for x in n.get("inputs",[])])
 print("  outputs:", [(x.get("name"),x.get("type")) for x in n.get("outputs",[])])
print("====LINKS")
for L in d.get("links",[]):
 print(L)
