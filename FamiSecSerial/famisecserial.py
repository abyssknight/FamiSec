import os
import serial
import sqlite3
import datetime

db_path = os.path.dirname(os.path.realpath(__file__)) + '/../FamiSecDjango/FamiSecDjango/db/famisec.db'
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row

c = conn.cursor()

mycard = u'0xTESTBADGE'
ts = datetime.datetime.now()

c.execute("SELECT MEMBERS_MEMBER.ID as member_id, MEMBERS_BADGE.card_id as card_id, MEMBERS_MEMBER.STATUS as status FROM MEMBERS_MEMBER, MEMBERS_BADGE WHERE MEMBERS_BADGE.CARD_ID = ?", (mycard,))

for row in c:
  if row["status"] == 'A':
    # Log active members card, and let them in
    c.execute("INSERT INTO MEMBERS_BADGELOG (card_id, owner_id, login_date) VALUES (?, ? ,?)", (mycard, row["member_id"], ts)) 
  elif row["status"] == 'I':
    # Log inactive members card, maybe tell them why
    c.execute("INSERT INTO MEMBERS_BADGELOG (card_id, owner_id, login_date) VALUES (?, ? ,?)", (mycard, row["member_id"], ts))

conn.commit()
conn.close()
