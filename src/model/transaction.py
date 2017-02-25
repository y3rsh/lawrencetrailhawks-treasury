import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy import Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = None
session = None

class Transaction(Base):
    __tablename__ = 'transactions'
    __table_args__ = {'sqlite_autoincrement': True}
    ledgerId = Column(Integer, primary_key=True)
    eventCode = Column(String(50))
    receipt = Column(String(50))
    description = Column(String(200))
    amount = Column(Numeric)
    raceExpenseType = Column(String(50))
    action = Column(String(50))
    payee = Column(String(50))
    actionCompleteDate = Column(String(50))

    def __repr__(self):
        return "<Transaction(ledgerId='%s', description='%s', amount='%s')>" % (self.ledgerId, self.description, self.amount)


engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base.metadata.create_all(engine)