import logging
import sys

class Logger:
    def __init__(self, name, filename="app.log", level=logging.INFO):
        """
        Initializes the custom Logger.
        
        Args:
            name (str): The name of the logger, typically __name__.
            filename (str): The name of the file to log messages to.
            level (int): The minimum logging level to track (default: INFO).
        """
        self.logger = logging.getLogger(name)
        # Set the logger's threshold level
        self.logger.setLevel(level)
        self.logger.propagate = False # Prevents messages from going to the root logger's handlers

        # Create a file handler and set its level
        file_handler = logging.FileHandler(filename, mode='a', encoding='utf-8')
        file_handler.setLevel(level)

        # Define the log message format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        if not self.logger.handlers: # Avoids adding duplicate handlers if the class is instantiated multiple times
            self.logger.addHandler(file_handler)
            
        # Optional: Add a stream handler for console output of WARNING/ERROR messages
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING) # Only show WARNING and ERROR in console
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        """Logs an INFO message."""
        self.logger.info(message)

    def warn(self, message):
        """Logs a WARNING message."""
        # Note: The standard method is 'warning', 'warn' is an alias
        self.logger.warning(message)

    def error(self, message, exc_info=False):
        """Logs an ERROR message. Set exc_info=True to include exception info."""
        self.logger.error(message, exc_info=exc_info)

