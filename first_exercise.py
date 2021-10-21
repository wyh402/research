import json
import collections
import operator

total = 20000

def printExample():
    with open('random_profiles.jsonl','rt',encoding='utf-8') as records:
        for line in records:
            person = json.loads(line)
            print(json.dumps(person,indent=4))
            break

def exerciseOne():
    with open('random_profiles.jsonl','rt',encoding='utf-8') as records:
        withJob = 0
        for line in records:
            person = json.loads(line)
            experience = person.get('experience', None)

            #Do I have to say "if experience" or "if experience is not None"
            if experience:
                withJob += 1
        print("About ", withJob / total * 100, "% people have jobs")

def exerciseTwo():

    #nested helper function
    def hasValidTitle(experience):
        validTitles = None
        role = experience.get('role', None)
        if role:
            validTitles = role.get('valid_roles', None)
        return validTitles

    def hasDepartments(experience):
        role = experience.get('role', None)
        dp = None
        dpValid = None
        if role:
            dp = role.get('departments', None)
            validRole = role.get('valid_roles', None)
            if validRole:
                dpValid = role.get('departments', None)
        return dp, dpValid

    with open('random_profiles.jsonl','rt',encoding='utf-8') as records:
        tCount = 0 #counter for title
        dpCount = 0 #counter for department
        dpValidCount = 0 #counter for both valid title & department

        jobCount = 0

        for line in records:
            person = json.loads(line)
            lst = person.get('experience', None)
            for experience in lst:
                if experience:
                    #note that one person can hold multiple jobs
                    jobCount += 1
                    if hasValidTitle(experience):
                        tCount += 1
                    dp, dpValid =  hasDepartments(experience)
                    if dp:
                        dpCount += 1
                    if dpValid:
                        dpValidCount += 1
            
        print(tCount / jobCount * 100, "%", " of jobs have valid titles")
        print(dpCount / jobCount * 100, "%", " of jobs have departments")
        print(dpValidCount / jobCount * 100, "%", " of jobs have valid titles AND departments")

def exerciseThree():

    dic = collections.defaultdict(int)

    with open('random_profiles.jsonl','rt',encoding='utf-8') as records:
        for line in records:
            person = json.loads(line)
            lst = person.get('experience', None)

            for experience in lst:
                if experience:
                    role = experience.get('role', None)
                    if role:
                        validTitles = role.get('valid_roles', None)
                        department = role.get('departments', None)

                        if department and validTitles:
                            for title in validTitles:
                                if title not in dic:
                                    dic[title] = 1
                                else:
                                    dic[title] += 1

        orderedDic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
        print(orderedDic)

def exerciseFour():
    dic = collections.defaultdict(int)
    with open('random_profiles.jsonl','rt',encoding='utf-8') as records:
        for line in records:
            person = json.loads(line)
            lst = person.get('experience', None)

            for experience in lst:
                if experience:
                    role = experience.get('role', None)
                    if role:
                        validTitles = role.get('valid_roles', None)
                        department = role.get('departments', None)

                        if validTitles and not department:
                            for title in validTitles:
                                if title not in dic:
                                    dic[title] = 1
                                else:
                                    dic[title] += 1

        orderedDic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
        print(orderedDic)
