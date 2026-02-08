from .create_db import db, User, Stats


class Insert:
    # Insert a new user into the database
    @staticmethod
    def insert_user(username, email, password_hash, bio, code):
        new_user = User(
            username=username, email=email, password_hash=password_hash, bio=bio, verified=False, code=code
        )
        new_user.stats = Stats()
        db.session.add(new_user)
        db.session.commit()

        return new_user.user_id
