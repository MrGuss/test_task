import unittest
import areas

class testareas(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_circle(self):
        self.assertAlmostEqual(areas.calc_circle(3), 28.2743, places=4)
        with self.assertRaises(TypeError):
            areas.calc_circle("asdasd")
        with self.assertRaises(AssertionError):
            areas.calc_circle(-12)
        with self.assertRaises(TypeError):
            areas.calc_circle(1,2)
    
    def test_triang(self):
        self.assertEqual(areas.calc_triang(3,4,5),6)
        with self.assertRaises(TypeError):
            areas.calc_triang("as","as","aa")
        with self.assertRaises(AssertionError):
            areas.calc_triang(-12,1,4)
        with self.assertRaises(AssertionError):
            areas.calc_triang(1,1,4)
        with self.assertRaises(TypeError):
            areas.calc_triang(2,1)
            
    def test_fig(self):
        self.assertEqual(areas.calc_fig("t", 3,4,5),6)
        self.assertAlmostEqual(areas.calc_fig("c", 3), 28.2743, places=4)
        with self.assertRaises(ValueError):
            areas.calc_fig("g",1,233)
        with self.assertRaises(ValueError):
            areas.calc_fig(1,1,233)
            
    def test_check(self):
        self.assertEqual(areas.check_triang(3,4,5),True)
        self.assertEqual(areas.check_triang(3,3,5),False)
        with self.assertRaises(TypeError):
            areas.check_triang("as","as","aa")
        with self.assertRaises(AssertionError):
            areas.check_triang(-12,1,4)
        with self.assertRaises(AssertionError):
            areas.check_triang(1,1,4)
        with self.assertRaises(TypeError):
            areas.check_triang(2,1)
            
if __name__ == "__main__":
  unittest.main()
