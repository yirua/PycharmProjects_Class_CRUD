


class Person_Manager(object):
    def create_person(self, name, prename, tel, email, dob):
        person = Person(name=name, prename = prename, tel = tel, email = email, dob = dob)
        return  person

class Person(object):

    def __init__(self, name, prename, tel, email, dob):
        self.name = name
        self.prename = prename
        self.tel = tel
        self.email = email
        self.dob = dob

    def set_name(self, name):
        self.name = name

    def set_prename(self, prename):
        self.prename = prename

    def set_tel(self, tel):
        self.tel = tel

    def set_email(self, email):
        self.email = email

    def set_dob(self, dob):
        self.dob = dob

    def __repr__(self):

       return '\n<name: {}, prename: {}, tel: {}, email: {}, dob: {}>'.format(self.name, self.prename, self.tel, self.email, self.dob)

    objects = Person_Manager()