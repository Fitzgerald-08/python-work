def build_person(first_name, last_name, occupation, city, age=None, country=""):
    """Return a dictionary of information about a person"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    if country:
        person["country"] = country
    if occupation:
        person["occupation"] = occupation
    if city:
        person["city"] = city
    return person


musician = build_person("jimi", "hendrix", "software developer", "seattle", age=27)
print(musician)
