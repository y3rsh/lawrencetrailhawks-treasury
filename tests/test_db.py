import src.model.line_item
from src.model.line_item import LineItem, session
import src.sheets.spreadsheet
from src.sheets.spreadsheet import get_sheet

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def test_ledger_creation():
  line_item  = LineItem(ledgerId=None, eventCode='2017hawkExpense', receipt='', description='Park Donation', amount= '200.00', raceExpenseType='park donation', action='', payee='', actionCompleteDate='')
  session.add(line_item)
  our_user = session.query(LineItem).filter_by(description='Park Donation').first()
  assert  our_user == line_item

def test_persistance_of_record():
  our_user = session.query(LineItem).filter_by(description='Park Donation').first()
  print (f"ledgerid = {our_user.ledgerId}, description = {our_user.description}")
  assert our_user.description == 'Park Donation'

def test_getsheet():
  data = get_sheet("2017Hawk", "Sheet1")
  # data = get_sheet("2017Nighthawk", "Sheet1")
  # data = get_sheet("2017PiDay", "Sheet1")
  # data = get_sheet("2017Shuffle", "Sheet1")
  # data = get_sheet("2017Snake", "Sheet1")
  # data = get_sheet("2017Ultrasignup", "Sheet1")
  # data = get_sheet("2017Ledger", "Sheet1")
  # data = get_sheet("2017TestLedger", "Sheet1")
  description = [d for d in data if d["description"] == 'Park Donation ']
  assert description[0]["description"] == 'Park Donation '

def test_insertsheet():
  setup_test_sheet()
  our_user = session.query(LineItem).filter_by(description='Mile 90 Photography').first()
  print("look: ",our_user)

def test_write_back():
  setup_test_sheet()
  row = session.query(LineItem).filter_by(description='Mile 90 Photography').first()
  before_description = row.description
  print("before: ", row)
  row.description = row.description + " wut"
  altered_id = row.id
  session.commit()
  row = session.query(LineItem).filter_by(id=altered_id).first()
  after_description = row.description
  print("after: ", row)
  assert before_description != after_description

def setup_test_sheet():
  data = get_sheet("2017TestLedger", "Sheet1")
  for val in data:
    session.add(LineItem(**val))
  session.commit()