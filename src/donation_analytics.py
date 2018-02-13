from __future__ import print_function

from typing import List

import sys
import re


# 假设文件可以一次加载完
# 修改方向：分割文件？分batch处理

class Donation:
	def __init__(self, CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID):
		self.CMTE_ID = CMTE_ID
		self.NAME = NAME
		self.ZIP_CODE = ZIP_CODE
		self.TRANSACTION_DT = TRANSACTION_DT
		self.TRANSACTION_AMT = TRANSACTION_AMT
		self.OTHER_ID = OTHER_ID

	def isValid(self):
		print("here")
		if self.CMTE_ID is None or re.match('^[a-zA-Z0-9\s]*$', self.CMTE_ID) is None:
			print(1)
		if self.NAME is None or re.match('^[a-zA-Z0-9\s.,]*$', self.NAME) is None:
			print(2)
		if self.ZIP_CODE is None or len(self.ZIP_CODE) < 5 or re.match('^[0-9]*$', self.ZIP_CODE) is None:
			print(3)
		if self.TRANSACTION_DT is None or re.match('^(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])(19|20)\d\d$', self.TRANSACTION_DT):
			print(4)
		if self.TRANSACTION_AMT is None:
			print(5)
		if self.OTHER_ID is not None:
			print(6)
	

		if (
			self.CMTE_ID is None or re.match('^[a-zA-Z0-9\s]*$', self.CMTE_ID) is None or
			self.NAME is None or re.match('^[a-zA-Z0-9\s.,]*$', self.NAME) is None or
			self.ZIP_CODE is None or len(self.ZIP_CODE) < 5 or re.match('^[0-9]*$', self.ZIP_CODE) is None or
			self.TRANSACTION_DT is None or re.match('^(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])(19|20)\d\d$', self.TRANSACTION_DT) or
			self.TRANSACTION_AMT is None or 
			self.OTHER_ID is not None
			):

			return False



INPUT_FILE = open(sys.argv[1], 'r')
INPUT_PERCENTILE = open(sys.argv[2],'r')
OUTPUT_FILR = open(sys.argv[3],'w')

itcont_lines = INPUT_FILE.readlines()

itcont_lines = list(map(lambda line : line.split('|'), itcont_lines))

# for donation in itcont_lines:
for record in [itcont_lines[1]]:
	print(itcont_lines[1])
	CMTE_ID = record[0]
	NAME = record[8]
	ZIP_CODE = record[11]
	TRANSACTION_DT = record[13]
	TRANSACTION_AMT = record[14]
	OTHER_ID = record[15]

	# if CMTE_ID is None or re.match('^[a-zA-Z0-9\s]*$', CMTE_ID) is None:
	# 	continue
	# if NAME is None or or re.match('^[a-zA-Z0-9\s.,]*$', NAME) is None:
	# 	continue
	# if ZIP_CODE is None or len(ZIP_CODE) < 5 or re.match('^[0-9]*$', ZIP_CODE) is None:
	# 	continue
	# if TRANSACTION_DT is None or re.match('^(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])(19|20)\d\d$', TRANSACTION_DT):
	# 	continue
	# if TRANSACTION_AMT is None:
	# 	continue
	# if OTHER_ID is not None:
	# 	continue
	
	donation = Donation(CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID)
	if donation.isValid() is False:
		print('TTTTTTTTT')