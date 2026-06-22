# test_ledgermint.py
"""
Tests for LedgerMint module.
"""

import unittest
from ledgermint import LedgerMint

class TestLedgerMint(unittest.TestCase):
    """Test cases for LedgerMint class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerMint()
        self.assertIsInstance(instance, LedgerMint)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerMint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
