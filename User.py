class User:
    name = None
    pw = None

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_password(self, pw):
        self.pw = pw

    def get_password(self):
        return self.pw
