"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "age": "33 Years old",
            "gender": "Male",
            "Lucky_numbers": ["7", "13", "22"]
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": "Doe",
            "age": "35 Years old",
            "gender": "Female",
            "Lucky_numbers": ["10", "14", "3"]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        for i in self._members:
            if id==i["id"]:
                Informacion = {
                    id: self._generateId(),
                    first_name:member["first_name"],
                    last_name:member["Doe"],
                    age:member["age"],
                    gender:member["gender"],
                    lucky_numbers:member["lucky_numbers"]
                }
                self._members.append(Informacion)
        return None

    def delete_member(self, id):
        for i in self._members:
            if id==i["id"]:
                self._members.remove(i)
                return ('Done')
        return None

    def update_member(self, id, member, request):
        for i in self._members:
            if id==i["id"]:
                Informacion = {
                    first_name:request.data["first_name"],
                    age:request.data["age"],
                    gender:request.data["gender"],
                    lucky_numbers:request.data["lucky_numbers"]
                }
                self._members.append(Informacion)
        return None

    def get_member(self, id):
        for i in self._members:
            if id==i["id"]:
                return i
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members