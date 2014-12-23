class User:
    def __init__(self, id, name = None, password = None):
        self._user_data = \
            {
                "id": id,
                "name": name,
                "password": password,
            }

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def is_admin(self):
        return self._user_data.get("is_admin", False)

    def set_admin(self):
        self._user_data["is_admin"] = True

    def get_id(self):
        return self._user_data["id"]