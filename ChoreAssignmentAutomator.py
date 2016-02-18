#Imports
from prettytable import PrettyTable
import csv
import random
import sys
import time
import smtplib

#Fetch the date
date = time.strftime("%d-%m-%Y")

#Open the member and chore files and read in info
members = []
with open("chores.csv") as chore_file:
	chores = chore_file.read().splitlines()

with open("members.csv") as mem_file:
	for line in mem_file:
		members.append(line.strip().split(','))

fin = open("File path" % date, 'w') 

#Shuffle the chores
random.shuffle(chores)

#Setup email 
sender = "username@provider.com"
password = "password"
server = smtplib.SMTP('SMTP server address')
server.ehlo()
server.starttls()
server.login(sender,password)
index = 0

#Setup table
table = PrettyTable(['First Name', 'Last Name', 'Chore','Completed'])
table.padding_width = 1
table.align['Chore'] = 'l'

#Loop
for name in members:
	table.add_row([name[0], name[1], chores[index], u"\u2610"])
	print name[2]
	message = "Your chore for this week is to %s Chores are due Sunday at 10PM. \n" %chores[index]
	print message
	server.sendmail(sender, name[2], message)
	print "Successfully sent email"
	index = index + 1

#Write table to file
fin.write(str(table))

#Close the files
mem_file.close()
chore_file.close()

	







