import glob,json
p=glob.glob("/mnt/workspace/ComfyUI/user/default/workflows/03*")[0]
d=json.load(open(p))
lines=[]
lines.append("FORMAT UI nodes=%d links=%d" % (len(d["nodes"]), len(d.get("links",[]))))
for n in d["nodes"]:
 w=n.get("widgets_values")
 wj=json.dumps(w,ensure_ascii=False)
 lines.append("ID=%s TYPE=%s TITLE=%s" % (n.get("id"), n.get("type"), n.get("title")))
 lines.append("  W=%s" % wj)
open("/tmp/wf_report.txt","w").write("\n".join(lines))
print("WROTE", len("\n".join(lines)))
