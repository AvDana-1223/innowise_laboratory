from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///orm.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    title = Column(String(256), nullable=False)
    author = Column(String(256), nullable=False)
    year = Column(Integer, nullable=True)


Base.metadata.create_all(engine)
