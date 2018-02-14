import unittest
from Classes import Donation, Dictionary

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

	def test_getID(self):
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.getID(), 'ABBOTT, JOSEPH02895')

	def test_getYear(self):
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.getYear(), '2018')

	def test_getRecipient(self):
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.getRecipient(), 'C00384516')

	def test_getZip(self):
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.getZip(), '02895')

	def test_getAmt(self):
		donation = Donation('C00384516', 'ABBOTT, JOSEPH', '028956146'[0:5], '01122018', '333', '')
		self.assertEqual(donation.getAmt(), float(333))

	def test_add(self):
		d = Dictionary()
		self.assertEqual(d.add('ABBOTT, JOSEPH02895', 2018).dictionary, {'ABBOTT, JOSEPH02895': [1, 2018]})

	def test_add_long(self):
		d = Dictionary()
		self.assertEqual(d.add_long('C00384516', '028956146'[0:5], '2018', 333).dictionary, {('C00384516', '02895', '2018'): [333]} )
		self.assertEqual(d.add_long('C00384516', '028956146'[0:5], '2018', 384).dictionary, {('C00384516', '02895', '2018'): [333, 384]} )

	def test_check(self):
		d = Dictionary()
		self.assertEqual(d.add('ABBOTT, JOSEPH02895', 2018).dictionary, {'ABBOTT, JOSEPH02895': [1, 2018]})
		self.assertEqual(d.check('ABBOTT, JOSEPH02895'), True)

	def test_get(self):
		d = Dictionary()
		self.assertEqual(d.add_long('C00384516', '028956146'[0:5], '2018', 333).dictionary, {('C00384516', '02895', '2018'): [333]} )	
		self.assertEqual(d.get(('C00384516', '028956146'[0:5], '2018')), [333])

if __name__ == '__main__':
	unittest.main()