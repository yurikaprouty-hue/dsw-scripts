import json, urllib.request
d=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
for k,n in d.items():
 req=n["input"].get("required",{})
 hits=[]
 for f,v in req.items():
  if isinstance(v[0],list):
   for opt in v[0]:
    if "minimax_h3_fl2va" in str(opt):
     hits.append((f,str(opt)))
 if hits:
  print("KEY",k,"DISPLAY",n.get("display_name"))
  print(" REQ_FIELDS",list(req.keys()))
  for f,o in hits: print("  ENUM",f,o)
  print(" OUT",n.get("output_name"))
