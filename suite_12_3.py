import unittest

class RunnerTest(unittest.TestCase):
    def test_challenge(self):

        self.assertEqual(2 + 2, 4)

    def test_run(self):

        self.assertEqual("hello".upper(), "HELLO")

    def test_walk(self):

        self.assertEqual(len("test"), 4)

class TournamentTest(unittest.TestCase):
    @unittest.skip("Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        
        self.assertEqual(1, 1)

    @unittest.skip("Тесты в этом кейсе заморожены")
    def test_second_tournament(self):

        self.assertEqual(2, 2)

    @unittest.skip("Тесты в этом кейсе заморожены")
    def test_third_tournament(self):

        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()