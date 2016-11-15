import json
import datetime
from time import strftime
from time import localtime

def findMatches(json_str, db):
	data = json.loads(json_str)
	results = applyAllFilters(data['user_email'], data['location'], data['start_time'], data['end_time'], db)
	return json.dumps(results)

def applyAllFilters(user_email, city, start_time, end_time, db):
	db.row_factory = dict_factory
	cur = db.execute('select distinct events.id, firstname, lastname, charge, rating, description, location from guides inner join events on guides.id = events.guide_id where events.interest_id in (select user_interests.interest_id from user_interests inner join guide_interests on user_interests.interest_id = guide_interests.interest_id) and events.location = "%s" and events.start_time >= "%s" and events.end_time <= "%s" order by rating' % (city, start_time, end_time))
	return cur.fetchall()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def addBooking(json_str, db):
	data = json.loads(json_str)
	db.row_factory = dict_factory
	cur = db.execute('select id as id from users where email = "%s"' % (data['user_email']))
	user = cur.fetchone()
	currentTime = strftime("%Y-%d-%m %H:%M", localtime())
	try:
		cur = db.execute('insert into booking (booking_time, event_id, user_id) values (?, ?, ?)', [currentTime, data['event_id'], user["id"]])
		db.commit()
		return json.dumps(True)
	except Exception as e:
		return json.dumps(False)