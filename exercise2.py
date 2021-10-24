import json
import collections
import operator

map = collections.defaultdict(int)
errors = []

class Error:
    def __init__(self, keyword):
        self.keyword = keyword
        self.dict = collections.defaultdict(int)

#initialize map dicitonary with keyword-department pair
def fillDict():
    with open('departments.jsonl','rt',encoding='utf-8') as records:
        for line in records:
            item = json.loads(line)
            k = item.get('keyword', None)
            dep = item.get('department', None)
        
            if k and dep:
                k = k.lower()
                map[k] = dep.lower()


def processProfiles():

    with open('random_profiles.jsonl','rt',encoding='utf-8') as records:
        for line in records:
            person = json.loads(line)
            lst = person.get('experience', None)

            for exp in lst:
                if exp:
                    role = exp.get('role', None)
                    isEdu = exp.get('is_edu', None)
                    if role and not isEdu:
                        title = role.get('original', None)
                        deps = role.get('departments', None)
                        if deps and title:
                            for dep in deps:
                                isCorrect, key = checkMap(title, dep)
                                if not isCorrect:
                                    updateList(key, dep)
                            

def updateList(key, dep):

    for e in errors:
        if e.keyword == key:
            if dep in e.dict:
                e.dict[dep] += 1
            else:
                e.dict[dep] = 1
            return
    
    err = Error(key)
    errors.append(err)
                       

def checkMap(title, dep):
    title = title.lower()
    dep = dep.lower()

    for key in map:
        if title in key:
            return map[key] == dep, key