from database import Select

class Leaderboard:
    # Return the top 10 users ranked by momentum
    @staticmethod
    def get_top_users():
        return Select.get_top_users()