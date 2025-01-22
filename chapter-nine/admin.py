class User:
    """Define the information about a user"""

    def __init__(self, first_name, last_name, residence, birth_date):
        """Initialize attributes typical of a user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.residence = residence
        self.birth_date = birth_date

    def describe_user(self):
        """Summarize user information"""
        information_summary = (f"First name: {self.first_name.title()}\n"
                               f"Last name: {self.last_name.title()}\n"
                               f"Country of Residence: {self.residence.title()}\n"
                               f"Birth date: {self.birth_date.title()}")

        return information_summary

    def greet_user(self):
        """Greet user (no less, no more)"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, how's it going?")


class Admin(User):
    """Model a user (no more)"""

    def __init__(self, first_name, last_name, residence, birth_date):
        """Define the privileges for an admin"""
        self.birth_date = birth_date
        super().__init__(self, first_name, last_name, residence)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print the privileges listed above"""
        print("List of privileges an admin enjoys of:\n")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("fitz", "unknown", "private", "not reachable")
admin.show_privileges()
