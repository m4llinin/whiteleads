from src.core.database.base import SqlAlchemyRepository
from src.models.user import User


class UserRepository(SqlAlchemyRepository, model=User):
    pass
