from __future__ import annotations
import argparse,json,re
from collections import Counter
from pathlib import Path
TERM_PATTERN=re.compile(r"[A-Za-z0-9_'-]+|[\u4e00-\u9fff]")
def analyze_text(text,top=10):
 terms=[term.lower() for term in TERM_PATTERN.findall(text)]
 return {"lines":len(text.splitlines()),"characters":len(text),"characters_without_whitespace":sum(not c.isspace() for c in text),"terms":len(terms),"unique_terms":len(set(terms)),"top_terms":Counter(terms).most_common(top)}
def analyze_file(path,top=10,encoding="utf-8"):
 return {"file":str(path.resolve()),**analyze_text(path.read_text(encoding=encoding),top)}
def main():
 parser=argparse.ArgumentParser(description="Analyze text files and frequent terms."); parser.add_argument("files",nargs="+"); parser.add_argument("--top",type=int,default=10)
 parser.add_argument("--encoding",default="utf-8"); parser.add_argument("--json",dest="json_path"); args=parser.parse_args()
 reports=[analyze_file(Path(name),args.top,args.encoding) for name in args.files]
 for report in reports:
  print(f"\n{report['file']}\n  Lines: {report['lines']}\n  Characters: {report['characters']}\n  Terms: {report['terms']}")
  print("  Top terms: "+", ".join(f"{term} ({count})" for term,count in report["top_terms"]))
 if args.json_path: Path(args.json_path).write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding="utf-8")
if __name__ == "__main__": main()
