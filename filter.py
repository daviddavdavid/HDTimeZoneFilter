import copy
senior_list = {
    "1": 1,
    "2": 3,
    "4": 5
}

intern_list = {
    "1": 5,
    "2": 6,
    "4": 5,
    "3": 2,
    "7": -1,
    "6": 2
}



def sort_people(seniors_time, interns_time, people_per_senior):
    if len(seniors_time) * people_per_senior < len(interns_time):
        print("Error: there will be interns not assigned to seniors due to the amount of interns")
        return


    couples = {}
    couples.clear() #just to be sure
    for senior in seniors_time.items():
        pairing = []
        for intern in interns_time.items():
            if len(pairing) < people_per_senior:
                pairing.append(intern)
            else:
                for old_intern in pairing:
                    dif_new_intern = abs(senior[1] - intern[1])
                    dif_old_intern = abs(senior[1] - old_intern[1])

                    if dif_new_intern < dif_old_intern:
                        old_intern = dif_new_intern #I think this should work, if it doesn't ill do it w pairing itself

        d_pairing = copy.deepcopy(pairing)
        assigned_senior = {senior[1]: d_pairing}
        couples[senior[1]] = d_pairing
        assigned_senior.clear()

        for paired_interns in d_pairing:
            interns_time.pop(paired_interns[0])
        pairing.clear()
        
    return copy.deepcopy(couples)


print(sort_people(senior_list, intern_list, 2))

