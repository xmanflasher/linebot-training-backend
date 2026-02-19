from models.team import Team
from .base_repository import BaseRepository

class TeamRepository(BaseRepository):
    model = Team

    @classmethod
    def find_by_join_code(cls, join_code):
        return cls.model.query.filter_by(join_code=join_code).first()
