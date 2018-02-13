import unittest
from Classes import Donation, Dictionary, Output

class TestClasses(unittest.TestCase):
	def test_isValid(self):
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), True)

		donation = Donation(None, 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('$00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		
		donation = Donation('C00384516', None, '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('C00384516', '', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('C00384516', 'ABBOTT,*JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028#95146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.isValid(), False)

		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], None, '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '', '333', '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '&1-2?18', '333', '')
		self.assertEqual(donation.isValid(), False)

		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', None, '')
		self.assertEqual(donation.isValid(), False)
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '', '')
		self.assertEqual(donation.isValid(), False)

		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', 'abc')
		self.assertEqual(donation.isValid(), False)

if __name__ == '__main__':
	unittest.main()