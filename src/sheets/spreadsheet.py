import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet(worksheet_name):
  # use creds to create a client to interact with the Google Drive API
  scope = ['https://spreadsheets.google.com/feeds']
  creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GSERVICEJSON'], scope)
  client = gspread.authorize(creds)

  # Find a workbook by name and open the first sheet
  # Make sure you use the right name here.
  sheet = client.open(worksheet_name).sheet1

  # Extract and print all of the values
  list_of_hashes = sheet.get_all_records()
  print(list_of_hashes)
  return list_of_hashes