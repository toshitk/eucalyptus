from sqlalchemy import create_engine

from api.infrastructrure.database.model.base import Base
from api.infrastructrure.database.model.user import Base as user

DB_URL = "mysql+pymysql://root@db:3306/eucalyptus_local?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    user.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
