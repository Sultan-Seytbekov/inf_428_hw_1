import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    """Generate random threat scores for a department."""
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_aggregated_score(department_scores, importance_tags):
    """
    Calculate aggregated threat score for the company.
    - department_scores: List of lists, where each sublist contains threat scores of a department.
    - importance_tags: List of integers representing departmental importance (1-5).
    """
    total_weighted_score = 0
    total_users = 0

    for i, scores in enumerate(department_scores):
        importance = importance_tags[i]
        total_weighted_score += sum(scores) * importance
        total_users += len(scores) * importance

    aggregated_score = total_weighted_score / total_users
    return round(min(max(aggregated_score, 0), 90))  # Ensure score is in range 0-90

class TestAggregatedThreatScore(unittest.TestCase):
    def test_generate_random_data(self):
        data = generate_random_data(45, 10, 50)
        self.assertTrue(all(0 <= x <= 90 for x in data))
        self.assertEqual(len(data), 50)

    def test_calculate_aggregated_score_balanced(self):
        scores = [
            generate_random_data(40, 5, 100),
            generate_random_data(42, 5, 100),
            generate_random_data(38, 5, 100)
        ]
        importance = [3, 3, 3]
        result = calculate_aggregated_score(scores, importance)
        self.assertTrue(0 <= result <= 90)

    def test_calculate_aggregated_score_unbalanced_importance(self):
        scores = [
            generate_random_data(40, 5, 100),
            generate_random_data(70, 5, 100)
        ]
        importance = [1, 5]
        result = calculate_aggregated_score(scores, importance)
        self.assertTrue(0 <= result <= 90)
    
    def test_calculate_aggregated_score_large_variance(self):
        scores = [
            generate_random_data(40, 10, 200),
            generate_random_data(50, 10, 10)
        ]
        importance = [2, 3]
        result = calculate_aggregated_score(scores, importance)
        self.assertTrue(0 <= result <= 90)
    
    def test_edge_cases(self):
        # Empty departments
        scores = [[]]
        importance = [1]
        with self.assertRaises(ZeroDivisionError):
            calculate_aggregated_score(scores, importance)

        # All zero scores
        scores = [[0, 0, 0], [0, 0]]
        importance = [2, 3]
        result = calculate_aggregated_score(scores, importance)
        self.assertEqual(result, 0)

        # Single department
        scores = [generate_random_data(50, 5, 100)]
        importance = [3]
        result = calculate_aggregated_score(scores, importance)
        self.assertTrue(0 <= result <= 90)

if __name__ == "__main__":
    unittest.main()
