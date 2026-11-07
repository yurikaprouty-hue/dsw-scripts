import glob,json
d=json.load(open(glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03*")[0]))
ns={n["id"]:n for n in d["nodes"]}
for n in d["nodes"]:
 t=n["type"]; w=n.get("widgets_values") or []
 print("NODE",t)
 if t=="LoadImage": print("  IMG=",w[0])
 if "Image to Video" in (n.get("title") or ""):
  print("  prompt=",repr(w[0])[:60])
  print("  WxH=",w[1],w[2],"dur=",w[3])
print("LINKS")
for L in d["links"]:
 print(" ",ns[L[1]]["type"],"->",ns[L[3]]["type"])
