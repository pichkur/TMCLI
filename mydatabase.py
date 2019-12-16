from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


engine = create_engine('sqlite:///tasks.db', echo=True)


metadata = MetaData()

tasks_table = Table('tasks', metadata,
            Column('id', Integer, primary_key=True),
            Column('text', String),
            Column('end_date', String)
        )

metadata.create_all(engine)



