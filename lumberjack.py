import logging
import os

class Logger():

    log_path = ""

    def set_log_path(self):
        """
        """

        self.log_path = os.path.join(os.getcwd(), "logs/prometheus.log")

    def build_log_dir(self):
        """
        """

        if not os.path.isdir("logs"):
            print("Logging directory not found.")
            print("Creating logging directory...")
            log_dir_path = os.path.join(os.getcwd(), "logs")
            os.mkdir(log_dir_path)
            f = open(self.log_path, "x")
            f.close()

        elif not os.path.exists(self.log_path):
            f = open(self.log_path, "x")
            f.close()

    def build_logger(self):
        """
        """

        print("Setting up logging...")
        self.build_log_dir()
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename=self.log_path)

    def get_logger(self):
        """
        """

        self.set_log_path()
        self.build_logger()
        return logging.getLogger()
