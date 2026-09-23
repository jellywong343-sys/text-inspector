import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from text_inspector.cli import analyze_text
class Tests(unittest.TestCase):
 def test_counts(self):
  report=analyze_text("Hello hello\n你好",3); self.assertEqual(report["lines"],2); self.assertEqual(report["terms"],4); self.assertEqual(report["top_terms"][0],("hello",2))
if __name__ == "__main__": unittest.main()
