from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, user_id):
        self.id = user_id

    def get_role(self):
        return UserRoles().get_user_roles(self.id)


class Roles():
    READER = 'Reader'
    WRITER = 'Writer'


class UserRoles():  
    def __init__(self) -> None:
        pass  

    USER_ROLES = [
        {'id': '73077410', 'role': Roles.WRITER},
        {'id': '73077500', 'role': Roles.READER}
    ]

    def get_user_roles(self, user_id):
        # Default to READER. Role with the least permision
        role = Roles.READER
        for mapping in self.USER_ROLES:
            if mapping['id'] == user_id:
                return mapping['role']

        return role