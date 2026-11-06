import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TemplateTests(unittest.TestCase):
    def test_each_template_standalone(self):
        folder=ROOT/'templates'
        files=sorted(folder.glob('*.md'))
        self.assertEqual(len(files),3)
        for f in files:
            text=f.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('# '))
            self.assertNotIn('Back to [README]',text)
            self.assertNotIn('../examples/',text)
    def test_rights(self):
        self.assertIn('MIT License',(ROOT/'LICENSE').read_text(encoding='utf-8'))
