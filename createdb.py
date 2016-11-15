import csv

def addData(db):
	addUsers(db)
	addGuides(db)
	addInterests(db)
	userInterests(db)
	guideInterests(db)
	addEvents(db)

def addUsers(db):
	with open('models/user.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			db.execute('insert into users (id, firstname, lastname, email, password) values (?, ?, ?, ?, ?)', [row[0], row[1], row[2], row[3], row[4]])
		db.commit()

def addGuides(db):
	with open('models/guide.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			db.execute('insert into guides (id, firstname, lastname, email, contact, password, address, charge, rating) values (?, ?, ?, ?, ?, ?, ?, ?, ?)', [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
		db.commit()

def addInterests(db):
	with open('models/interests.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			db.execute('insert into interests (id, name) values (?, ?)', [row[0], row[1]])
		db.commit()

def userInterests(db):
	with open('models/user_interests.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			db.execute('insert into user_interests (user_id, interest_id) values (?, ?)', [row[0], row[1]])
		db.commit()

def guideInterests(db):
	with open('models/guide_interests.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			db.execute('insert into guide_interests (guide_id, interest_id) values (?, ?)', [row[0], row[1]])
		db.commit()

def addEvents(db):
	with open('models/event.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			address = row[3]
			location = address.split(':')[1]
			db.execute('insert into events (id, description, interest_id, location, guide_id, start_time, end_time) values (?, ?, ?, ?, ?, ?, ?)', [row[0], row[1], row[2], location, row[4], row[5], row[6]])
		db.commit()