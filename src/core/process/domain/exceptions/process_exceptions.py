class Error(Exception):
    def __init__(self):
        self.msg = ""
        self.status_code = 500

    def __str__(self):
        return self.msg


class InvalidCandidatoError(Error):
    def __init__(self):
        self.msg = "Invalid candidato"
        self.status_code = 400


class InvalidCargoError(Error):
    def __init__(self):
        self.msg = "Invalid cargo"
        self.status_code = 400


class InvalidStatusError(Error):
    def __init__(self):
        self.msg = "Invalid status"
        self.status_code = 400
