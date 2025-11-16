"""
Main application module
"""
from auth import UserAuth

def main():
    print("Git Training Project")
    print("Version: 1.0.0")
    
    # Initialize authentication
    auth = UserAuth()
    print("Authentication system initialized")

if __name__ == "__main__":
    main()