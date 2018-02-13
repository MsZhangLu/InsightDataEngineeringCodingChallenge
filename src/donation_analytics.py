from __future__ import print_function

from typing import List

from Classes import Donation, Dictionary, Output

import sys
import re
import math


# 假设文件可以一次加载完
# 修改方向：分割文件？分batch处理


INPUT_FILE = open(sys.argv[1], 'r')
PERCENTILE_FILE = open(sys.argv[2],'r')
OUTPUT_FILE = open(sys.argv[3],'w')

PERCENTILE = float(PERCENTILE_FILE.readlines()[0].split('\n')[0])

itcont_lines = INPUT_FILE.readlines()

itcont_lines = list(map(lambda line : line.split('|'), itcont_lines))

viewed = Dictionary()
repeated = Dictionary()

for record in itcont_lines:
# for record in [itcont_lines[1]]:

	CMTE_ID, NAME, ZIP_CODE = record[0], record[7], record[10][0:5]
	TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID = record[13], record[14], record[15]

	donation = Donation(CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID)

	if donation.isValid():
		don_id = donation.getID()
		
		if viewed.check(don_id):
			viewed.drop(don_id)
			repeated.add_long(donation.getRecipient(), donation.getZip(), donation.getYear(), donation.getAmt())

			key = donation.getRecipient(), donation.getZip(), donation.getYear()
			total_donations = repeated.get(key)

			# calculate percentile of contributions			
			dollar_donations = total_donations[0]
			dollar_donations.sort()
			rank = len(dollar_donations)
			percentile_index = math.ceil(PERCENTILE * rank / 100) - 1
			percentile_amt = dollar_donations[percentile_index]
			
			OUTPUT_FILE.write(key[0] + '|' + key[1] + '|' + key[2] + '|' + str(int(round(percentile_amt))) + '|' + str(int(round(sum(total_donations[0])))) + '|' + str(total_donations[1]) + '\n')
	
		else:
			viewed.add(don_id, donation.getYear())











