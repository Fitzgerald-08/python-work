class User:
    """Define the information about a user"""

    def __init__(self, first_name, last_name, residence, birth_date):
        """Initialize attributes typical of a user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.residence = residence
        self.birth_date = birth_date
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1"""
        self.login_attempts += 1
        print(f"Login attempt number {self.login_attempts}")

    def reset_login_attempts(self):
        """Reset number of login attempts to 0"""
        self.login_attempts = 0
        print(f"Login attempts reset to {self.login_attempts}")


user = User("alex", "marquez", "japan", "mexico")
print()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print()
user.reset_login_attempts()
