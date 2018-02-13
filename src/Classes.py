import re

class Donation:
	def __init__(self, CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID):
		self.CMTE_ID = CMTE_ID
		self.NAME = NAME
		self.ZIP_CODE = ZIP_CODE
		self.TRANSACTION_DT = TRANSACTION_DT
		self.TRANSACTION_AMT = TRANSACTION_AMT
		self.OTHER_ID = OTHER_ID

	def isValid(self):
		if (
			self.CMTE_ID is None or len(self.CMTE_ID) == 0 or re.match('^[a-zA-Z0-9\s]*$', self.CMTE_ID) is None or
			self.NAME is None or len(self.NAME) == 0 or re.match('^[a-zA-Z0-9\s.,]*$', self.NAME) is None or
			len(self.ZIP_CODE) < 5 or re.match('^[0-9]*$', self.ZIP_CODE) is None or
			self.TRANSACTION_DT is None or len(self.TRANSACTION_DT) == 0 or 
			re.match('^((0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])[12]\d{3})$', self.TRANSACTION_DT) is None or
			self.TRANSACTION_AMT is None or len(self.TRANSACTION_AMT) == 0 or 
			len(self.OTHER_ID) > 0
			):
			return False
		else:
			return True

	def getID(self):
		return str(self.NAME) + str(self.ZIP_CODE)

	def getYear(self):
		return self.TRANSACTION_DT[4:]

	def getRecipient(self):
		return self.CMTE_ID

	def getZip(self):
		return self.ZIP_CODE

	def getAmt(self): 
		return float(self.TRANSACTION_AMT)
		# return int(self.TRANSACTION_AMT)


class Dictionary:
	def __init__(self):
		self.dictionary = {}

	def add(self, key, year):
		if key in self.dictionary:
			self.dictionary[key][0] += 1
		else:
			self.dictionary[key] = [1, year]

	def add_long(self, recipient, zipcode, year, amt):
		key = (recipient, zipcode, year)
		if key in self.dictionary:
			self.dictionary[key][0].append(amt)
			self.dictionary[key][1] += 1
		else:
			self.dictionary[key] = [[amt], 1] 

	def drop(self, key):
		self.dictionary.pop(key)

	def check(self, key):
		return True if key in self.dictionary else False

	def get(self, key):
		return self.dictionary[key]

class Output:
	def __init__(self, recipient, zipcode, year, percentile, amt, donors):
		self.recipient = recipient
		self.zipcode = zipcode
		self.year = year
		self.percentile = percentile
		self.amt = amt
		self.donors = donors
