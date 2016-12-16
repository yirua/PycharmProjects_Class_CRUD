#!/usr/bin/python

import  entreprise
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

person1=Person('python', 'gama', '514-1234567', 'python_alpha@gmail.com', '1900-01-01')
person2=Person('qython', 'beta', '514-1234567', 'qython_beta@gmail.com', '1901-01-01')
person3=Person('rython', 'alpha', '514-1234567', 'rython_gama@gmail.com', '1902-01-01')

entreprise.add_person(person3)
entreprise.add_person(person2)
entreprise.add_person(person1)



print "\n after sorted by name: \n"
print(sorted(entreprise.person_list, key=entreprise.getByName))


print "\n after sorted by prename: \n"
print(sorted(entreprise.get_person_list(), key=entreprise.getByPreName))

entreprise.delete_person('python', 'gama')
print "\n after deleted by name and prename: \n"
print(sorted(entreprise.get_person_list(), key=entreprise.getByPreName))
entreprise.add_person(person1)

