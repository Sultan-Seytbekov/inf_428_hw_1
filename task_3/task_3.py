import math
import unittest

def transform_time_to_cyclic_feature(hour):
    if hour < 0 or hour >= 24:
        raise ValueError("Hour must be between 0 and 23")
    
    radians = (hour / 24) * 2 * math.pi
    sin_feature = math.sin(radians)
    cos_feature = math.cos(radians)
    
    return sin_feature, cos_feature

def calculate_time_difference_in_hours(start_hour, end_hour):
    if start_hour < 0 or start_hour >= 24 or end_hour < 0 or end_hour >= 24:
        raise ValueError("Hours must be between 0 and 23")

    diff = (end_hour - start_hour) % 24
    if diff > 12:
        diff = 24 - diff
    
    return diff

class TestTimeTransformation(unittest.TestCase):

    def test_transform_time_to_cyclic_feature(self):
        test_hours = [0, 6, 12, 18, 23]
        for hour in test_hours:
            sin_feature, cos_feature = transform_time_to_cyclic_feature(hour)
            self.assertTrue(-1 <= sin_feature <= 1)
            self.assertTrue(-1 <= cos_feature <= 1)
    
    def test_invalid_hour(self):
        with self.assertRaises(ValueError):
            transform_time_to_cyclic_feature(24)
        
        with self.assertRaises(ValueError):
            transform_time_to_cyclic_feature(-1)
    
    def test_calculate_time_difference_in_hours(self):
        self.assertEqual(calculate_time_difference_in_hours(23, 1), 2)
        self.assertEqual(calculate_time_difference_in_hours(1, 23), 2)
        self.assertEqual(calculate_time_difference_in_hours(12, 18), 6)
        
    def test_invalid_time_difference(self):
        with self.assertRaises(ValueError):
            calculate_time_difference_in_hours(24, 1)
        
        with self.assertRaises(ValueError):
            calculate_time_difference_in_hours(1, -1)

if __name__ == "__main__":
    unittest.main()
