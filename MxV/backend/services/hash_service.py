import hashlib

class Hash():
    # Hash the given password
    @staticmethod
    def hash_password(password):
        if password == "":
            return "empty_password"

        elif " " in password:
            return "has_space"

        full_hashed_password = int(
            hashlib.sha256(password.encode("utf-8")).hexdigest(), 16
        )
        password_hash = full_hashed_password % (10**8)

        return password_hash
