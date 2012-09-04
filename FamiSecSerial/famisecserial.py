import os
import serial
import sqlite3

db_path = os.path.dirname(os.path.realpath(__file__)) + '/../FamiSecDjango/FamiSecDjango/db/famisec.db'
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row

c = conn.cursor()

c.execute("SELECT * FROM MEMBERS_MEMBER, MEMBERS_BADGE WHERE MEMBERS_BADGE.CARD_ID = ? AND MEMBERS_MEMBER.STATUS = ?", ('0xTESTBADGE','A'))

for row in c:
  print row["name"]
