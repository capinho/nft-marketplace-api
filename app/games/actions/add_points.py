from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.users.models import User


class POST_AddPointsAction(BaseAction):
    class InEntity(BaseEntity):
        user: User
        game_index: int
        score_to_add: int

    def __init__(self):
        self.user_manager = User.objects

    def run(self, data: InEntity) -> User:

        if data.game_index == 1:
            data.user.first_score += data.score_to_add
        elif data.game_index == 2:
            data.user.second_score += data.score_to_add
        elif data.game_index == 3:
            data.user.third_score += data.score_to_add

        data.user.save()
        return data.user
