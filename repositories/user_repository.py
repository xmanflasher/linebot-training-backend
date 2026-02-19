from models.user import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    model = User

    @classmethod
    def find_by_line_id(cls, line_id):
        return cls.model.query.filter_by(line_id=line_id).first()
