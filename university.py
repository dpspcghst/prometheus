from json_historian import JSON_Historian

class HISTORY_Department():

    historian_types = ["JSON"]

    def __init__(self):
        """
        """

        print("University object created.")

    def build_historian(self, historian_type):
        """
        """

        if historian_type.upper() in self.historian_types:
            if historian_type.upper() == "JSON":
                return JSON_Historian()

        return None
