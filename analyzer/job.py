class JobDescription:
    def __init__(self, description):
        self.description = description.lower() if description else ""