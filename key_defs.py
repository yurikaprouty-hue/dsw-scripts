import json, urllib.request
d=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
for k in ["MinimaxH3ImageToVideo","ComfyMathExpression","PrimitiveFloat","PrimitiveInt","PrimitiveBoolean","ComfySwitchNode","LoraLoaderModelOnly","CreateVAEVideoTile","SaveVideo"]:
 n=d.get(k)
 if not n: print("MISSING",k); continue
 print("KEY",k)
 req=n["input"].get("required",{})
 opt=n["input"].get("optional",{})
 for f,v in req.items(): print(" R",f,("ENUM"+str(len(v[0]))) if isinstance(v[0],list) else v[0])
 for f,v in opt.items(): print(" O",f,("ENUM"+str(len(v[0]))) if isinstance(v[0],list) else v[0])
 print(" OUT",n.get("output"),n.get("output_name"))
