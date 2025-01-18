import unittest
from race_simulation.race_simulation import format_time, simulate_race


class TestRaceSimulation(unittest.TestCase):

    def test_format_time(self):
        """
        Test the format_time function for various inputs.
        """
        self.assertEqual(format_time(0), "0m 0.00s")
        self.assertEqual(format_time(59), "0m 59.00s")
        self.assertEqual(format_time(60), "1m 0.00s")
        self.assertEqual(format_time(125.5), "2m 5.50s")
        self.assertEqual(format_time(3661), "61m 1.00s")

    def test_simulate_race(self):
        """
        Test the simulate_race function to ensure it
        returns a winner and times.
        """

        winner, times = simulate_race()

        # Check that the winner is one of the vehicle names
        self.assertIn(
            winner, ["Royal Enfield", "Hindustan Ambassador", "Tata 1210"]
        )

        # Check that times is a dictionary with correct vehicle names
        self.assertIsInstance(times, dict)
        self.assertIn("Royal Enfield", times)
        self.assertIn("Hindustan Ambassador", times)
        self.assertIn("Tata 1210", times)


if __name__ == '__main__':
    unittest.main()
