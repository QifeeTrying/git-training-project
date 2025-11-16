"""
User authentication module
"""

class UserAuth:
    def __init__(self):
        self.users = {
            "admin": "admin123",
            "user": "user123"
        }
    
    def authenticate(self, username, password):
        """Authenticate user with username and password"""
        if username in self.users:
            if self.users[username] == password:
                return True
        return False
    
    def validate_username(self, username):
        """Validate username format"""
        if len(username) < 3:
            return False
        return True