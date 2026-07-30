# test_modelcore.py
"""
Tests for ModelCore module.
"""

import unittest
from modelcore import ModelCore

class TestModelCore(unittest.TestCase):
    """Test cases for ModelCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelCore()
        self.assertIsInstance(instance, ModelCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
