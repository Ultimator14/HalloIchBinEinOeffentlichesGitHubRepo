class User:
    name = "default"
    hashed_pw = "default"

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_hashed_password(self, pw):
        self.hashed_pw = pw

    def get_hashed_password(self):
        return self.hashed_pw
