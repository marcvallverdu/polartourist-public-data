import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from scale import listed_kp_to_g
from validate import validate
class ScaleTests(unittest.TestCase):
    def test_data(self): self.assertEqual(len(validate()),5)
    def test_source_labels(self):
        for token,want in [('5','G1'),('6','G2'),('7','G3'),('8','G4'),('9-','G4'),('9−','G4'),('9','G5')]:
            with self.subTest(token=token): self.assertEqual(listed_kp_to_g(token),want)
    def test_no_unsupported_inference(self):
        for token in [None,9,8.67,'8.67','9+','4','5-','',' 9','9 ','5.0']:
            with self.subTest(token=token):
                with self.assertRaises(ValueError): listed_kp_to_g(token)
if __name__=='__main__': unittest.main()
