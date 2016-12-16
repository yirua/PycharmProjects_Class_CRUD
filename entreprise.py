

person_list =[]

def add_person(person):
    person_list.append(person)

def delete_person(name, prename):
    for element in person_list:
        if (element.name == name and element.prename == prename):
            person_list.remove(element)

def get_person_list():
    return person_list

def getByName(person):
    return person.name

def getByPreName(person):
    return person.prename

