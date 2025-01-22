"""Introduce docstring here"""

from user import User


class Admin(User):
    """Model a user (no more)"""

    def __init__(self, first_name, last_name, residence, birth_date):
        """Define the privileges for an admin"""
        self.birth_date = birth_date
        super().__init__(self, first_name, last_name, residence)
        self.admin_privileges = Privileges()


class Privileges:
    """Define what are the privileges of an admin"""

    def __init__(self):
        """Privileges for an admin"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print privileges"""
        print("List of privileges an admin enjoys of:\n")
        for privilege in self.privileges:
            print(f"- {privilege}")
