"""
Logging module
"""
import datetime

class Logger:
    def __init__(self, name):
        self.name = name
        self.logs = []
    
    def log(self, level, message):
        """Log a message with timestamp"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] [{self.name}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def info(self, message):
        """Log info level message"""
        self.log("INFO", message)
    
    def error(self, message):
        """Log error level message"""
        self.log("ERROR", message)
    
    def warning(self, message):
        """Log warning level message"""
        self.log("WARNING", message)