import copy
#There is one limitation to the program, if the timezones are -12 and 12 for example the program would regard them as the farthest away while the are close then you think
#Here you fill in all the seniors in order, where the top one is most guaranteed to get an intern and the bottom one the least
#The index (first value of the two) is the id of the senior (tag can work as well) and the second the timezone where the number x is gmt + x 
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

#fill the senior_list and intern list (instruction above) and the how much people you want as a senior in as the last value
print(sort_people(senior_list, intern_list, 2))

