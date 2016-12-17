#!/usr/bin/python

import entreprise

from Person_class import Person_Manager

p_manager = Person_Manager()
person1=p_manager.create_person('python', 'gama', '514-1234567', 'python_alpha@gmail.com', '1900-01-01')
person2=p_manager.create_person('qython', 'beta', '514-1234567', 'qython_beta@gmail.com', '1901-01-01')
person3=p_manager.create_person('rython', 'alpha', '514-1234567', 'rython_gama@gmail.com', '1902-01-01')

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

