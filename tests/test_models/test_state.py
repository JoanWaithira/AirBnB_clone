#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def test_create_state_instance(self):
        """Tests if an instance in the city class is created"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_properties(self):
        """Tests if te initial values are strings"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attributes(self):
        """Checks if the state and name attributes are set correctly"""
        state = State()
        state.name = "Kenya"
        self.assertEqual(state.name, "Kenya")

    def test_base_model_inheritance(self):
        """Tests if city inherits attributes from base model"""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    def test_to_dictionary_method(self):
        """Tests whether to_dict method returns dictionary representation"""
        state = State()
        data_dict = state.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'State')

    def test_str_representation(self):
        """Tests whether the str method returns a string"""
        state = State()
        expected_str = f"[{state.__class__.__name__}] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_str)

if __name__ == '__main__':
    unittest.main()

