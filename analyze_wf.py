import glob,json
d=json.load(open(glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03*")[0]))
print("UI", "nodes" in d, len(d.get("nodes",[])))
for n in d["nodes"]:
 s=json.dumps(n.get("widgets_values"),ensure_ascii=False)
 print(n.get("id"),n.get("type"),s[:120])
