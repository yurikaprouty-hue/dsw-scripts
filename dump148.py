import json
p="/mnt/workspace/ComfyUI/user/default/workflows/03_H3图生视频(满血bf16).json"
d=json.load(open(p))
for n in d["nodes"]:
 if n.get("id")==148:
  print("KEYS",list(n.keys()))
  for k,v in n.items():
   if k=="widgets_values": continue
   print(k,"=",repr(v)[:400])
  print("PROPERTIES",json.dumps(n.get("properties",{}),ensure_ascii=False)[:600])
