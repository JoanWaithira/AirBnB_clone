import unittest
import models
import os
from models.review import Review

class TestReview(unittest.TestCase):

    def test_create_review_instance(self):
        """Checks if an instance is created"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_properties(self):
        """Checks if initial values are strings"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes(self):
        """Checks if attributes are set and retrieved correctly"""
        review = Review()
        review.place_id = "12345"
        review.user_id = "user123"
        review.text = "A great place to stay!"
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.text, "A great place to stay!")

    def test_base_model_inheritance(self):
        """Checks the inheritance from basemodel"""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_to_dict_method(self):
        """Checks if a dictionary is returned"""
        review = Review()
        data_dict = review.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'Review')
        self.assertIn('place_id', data_dict)
        self.assertIn('user_id', data_dict)
        self.assertIn('text', data_dict)

    def test_str_representation(self):
        """Checks if a string is returned"""
        review = Review()
        expected_str = f"[{review.__class__.__name__}] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected_str)

if __name__ == '__main__':
    unittest.main()

