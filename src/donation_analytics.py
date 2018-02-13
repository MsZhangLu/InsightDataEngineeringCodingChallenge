from __future__ import print_function

from typing import List

from Classes import Donation, Dictionary, Output

import sys
import re


# 假设文件可以一次加载完
# 修改方向：分割文件？分batch处理


INPUT_FILE = open(sys.argv[1], 'r')
INPUT_PERCENTILE = open(sys.argv[2],'r')
OUTPUT_FILR = open(sys.argv[3],'w')

itcont_lines = INPUT_FILE.readlines()

itcont_lines = list(map(lambda line : line.split('|'), itcont_lines))

viewed = Dictionary()
repeated = Dictionary()

# for donation in itcont_lines:
for record in [itcont_lines[1]]:

	CMTE_ID, NAME, ZIP_CODE = record[0], record[8], record[10][0:5]
	TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID = record[13], record[14], record[15]

	donation = Donation(CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID)

	if donation.isValid():
		don_id = donation.getID
		
		# 如果相同的人有过捐款记录，就是一个重复捐款的人
		# 记录最新出现的一次捐款
		if viewed.check(don_id):
			viewed.pop(don_id)
			repeated.add(donation.getRecipient(), donation.getZip(), donation.getYear(), donation.getAmt())
			# more calculation
			output = 
			


		if repeated.check(don_id):
			repeated.add(don_id,donation.getRecipient(), donation.getZip(), donation.getYear())
			# more calculation here
			
		
		else:
			viewed.add(don_id, donation.getYear())


		print(viewed.get(don_id))
		print(repeated.check(don_id))










