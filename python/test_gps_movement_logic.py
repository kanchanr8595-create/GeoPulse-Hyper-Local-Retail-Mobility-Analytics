
import unittest

from gps_movement_logic import (
    validate_coordinates,
    calculate_distance,
    calculate_next_position
)


class TestGPSMovement(unittest.TestCase):

    def test_valid_coordinates(self):
        self.assertTrue(validate_coordinates(28.6139, 77.2090))

    def test_invalid_latitude(self):
        with self.assertRaises(ValueError):
            validate_coordinates(100, 77.2090)

    def test_invalid_longitude(self):
        with self.assertRaises(ValueError):
            validate_coordinates(28.6139, 200)

    def test_distance_between_same_points(self):
        distance = calculate_distance(
            28.6139, 77.2090,
            28.6139, 77.2090
        )
        self.assertAlmostEqual(distance, 0, places=5)

    def test_next_position(self):
        new_lat, new_lon = calculate_next_position(
            28.6139, 77.2090,
            30, 90, 60
        )

        self.assertGreater(new_lon, 77.2090)

    def test_negative_speed(self):
        with self.assertRaises(ValueError):
            calculate_next_position(
                28.6139, 77.2090,
                -10, 90, 60
            )


if __name__ == "__main__":
    unittest.main()
