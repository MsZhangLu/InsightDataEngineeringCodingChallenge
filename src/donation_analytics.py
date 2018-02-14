from __future__ import print_function

from typing import List

from Classes import Donation, Dictionary

import sys
import re
import math


INPUT_FILE = open(sys.argv[1], 'r')
PERCENTILE_FILE = open(sys.argv[2],'r')
OUTPUT_FILE = open(sys.argv[3],'w')

PERCENTILE = float(PERCENTILE_FILE.readlines()[0].split('\n')[0])

viewed = Dictionary()
repeated = Dictionary()


with open(sys.argv[1]) as file:
	for record in file:
		record = record.split('|')

		CMTE_ID, NAME, ZIP_CODE = record[0], record[7], record[10]
		TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID = record[13], record[14], record[15]

		if ZIP_CODE is None:
			continue
		else:
			donation = Donation(CMTE_ID, NAME, ZIP_CODE[0:5], TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID)

			if donation.isValid():
				don_id = donation.getID()
				
				if viewed.check(don_id):
					repeated.add_long(donation.getRecipient(), donation.getZip(), donation.getYear(), donation.getAmt())

					key = donation.getRecipient(), donation.getZip(), donation.getYear()
					total_donations = repeated.get(key)

					# calculate percentile of contributions			
					dollar_donations = total_donations
					dollar_donations.sort()
					rank = len(dollar_donations)
					percentile_index = math.ceil(PERCENTILE * rank / 100) - 1
					percentile_amt = dollar_donations[percentile_index]

					OUTPUT_FILE.write(key[0] + '|' + key[1] + '|' + key[2] + '|' + str(int(round(percentile_amt))) + '|' + str(int(round(sum(total_donations)))) + '|' + str(len(total_donations)) + '\n')
			
				else:
					viewed.add(don_id, donation.getYear())











