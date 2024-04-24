class Sample:
    def __init__(
        self,
        title=None,
        location=None,
        website=None,
        email=None,
        phone=None,
    ):
        self.title = title
        self.location = location
        self.website = website
        self.email = email
        self.phone = phone

    @property
    def __keys__(self):
        key_list = list(self.__dict__.keys())
        return key_list
