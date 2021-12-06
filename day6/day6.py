ages_counter = {}
with open("input.txt") as f:
    l_ages = map(int, f.readline().split(","))

    for age in l_ages:
        ages_counter[age] = ages_counter.get(age, 0) + 1

def nb_lanterns(n_jours):
    copy_counter = ages_counter.copy()
    
    for i in range(n_jours):
        daily_age = {}
        for age in range(9):
            if age in copy_counter:
                if age - 1 >= 0:
                    daily_age[age - 1] = daily_age.get(age - 1, 0) + copy_counter[age]

                if age == 0:
                    daily_age[0] = 0
                    daily_age[6] = copy_counter[0]
                    daily_age[8] = copy_counter[0]

        copy_counter = daily_age
    
    return copy_counter
    
print(sum(nb_lanterns(80).values()))
print(sum(nb_lanterns(256).values()))
