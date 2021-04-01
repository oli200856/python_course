import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTest(unittest.TestCase):

    def test_eat_healthy(self):
        """eat should return positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )

    def test_eat_healthy_boolean(self):
        """is_healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="hahah")

    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )

    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Ugh, I overslept. I didn't mean to nap for 3 hours!"
        )

    def test_is_funny_tim(self):
        # self.assertFalse(is_funny("tim"), "tim should not be funny")
        self.assertEqual(is_funny("tim"), False)

    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("blue"))
        self.assertTrue(is_funny("noah"))
        self.assertTrue(is_funny("hazel"))
        self.assertTrue(is_funny("jason"))
        self.assertTrue(is_funny("jake"))

    def test_laugh(self):
        self.assertIn(laugh(), ("hahaha", "lol", "muahahaha", "tehehe"))        

if __name__ == "__main__":
    unittest.main()