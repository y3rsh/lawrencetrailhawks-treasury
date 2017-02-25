import src.model.transaction
from src.model.transaction import Transaction, session
import src.sheets.spreadsheet
from src.sheets.spreadsheet import get_sheet

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def test_ledger_creation():
  transaction  = Transaction(ledgerId=None, eventCode='2017hawkExpense', receipt='', description='Park Donation', amount= '200.00', raceExpenseType='park donation', action='', payee='', actionCompleteDate='')
  session.add(transaction)
  our_user = session.query(Transaction).filter_by(description='Park Donation').first()
  assert  our_user == transaction

def test_persistance_of_record():
  our_user = session.query(Transaction).filter_by(description='Park Donation').first()
  print (f"ledger id = {our_user.ledgerId}, description = {our_user.description}")
  assert our_user.description == 'Park Donation'

def test_getsheet():
  data = get_sheet("2017Hawk")
  description = [d for d in data if d["description"] == 'Park Donation ']
  assert description[0]["description"] == 'Park Donation '