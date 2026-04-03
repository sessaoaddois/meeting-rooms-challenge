import unittest
from app import checaConflito

class TestChecaConflito (unittest.TestCase):
	def test_checaconflito_case_um(self):
		self.assertEqual(checaConflito([[0, 30], [5, 10], [15, 20]]),2)
	def test_checaconflito_case_dois(self):
		self.assertEqual(checaConflito([]),0)
	def test_checaconflito_case_tres(self):
		self.assertEqual(checaConflito([[15,20]]),1)
	def test_checaconflito_case_tres(self):
		self.assertEqual(checaConflito([[0,5],[0,5],[0,5]]),3)
	def test_checaconflito_case_tres(self):
		self.assertEqual(checaConflito([[0,10],[10,20]]),1)
if __name__ == '__main__':
    unittest.main()