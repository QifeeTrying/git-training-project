"""
Main application module
"""
from logger import Logger

def main():
    # Initialize logger
    logger = Logger("GitTrainingApp")
    
    logger.info("Git Training Project started")
    logger.info("Version: 1.0.0")
    
    logger.info("Application running")

if __name__ == "__main__":
    main()