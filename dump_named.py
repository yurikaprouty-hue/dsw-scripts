import json, glob
ps=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03_H3*")
d=json.load(open(ps[0]))
for n in d["nodes"]:
 if n.get("id")==148:
  wvn=n.get("widgets_values_named")
  print("NAMED_TYPE",type(wvn).__name__)
  print(json.dumps(wvn,ensure_ascii=False,indent=1)[:3000])
  print("INPUTS",json.dumps(n.get("inputs"),ensure_ascii=False)[:800])
  print("OUTPUTS",json.dumps(n.get("outputs"),ensure_ascii=False)[:800])
