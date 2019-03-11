from multiprocessing import Pool
from random import randint
from ast import literal_eval
import cycle as cycle

def nonblank_lines(f):   # Joon
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def set_broadcast(population, sortedEvaluatedPopulation, islandNumber, percentageOfBestIndividualsForMigrationPerIsland, broadcast):
    allBests = []
    for i in range(int((len(population)) * percentageOfBestIndividualsForMigrationPerIsland)):
        allBests.append([population[sortedEvaluatedPopulation[i][5]], [sortedEvaluatedPopulation[i][0]]])
    broadcast[islandNumber] = allBests

def isMigrationNeed(broadcast):
    migraNeed = broadcast[len(broadcast)-1]
    return migraNeed

def find_island(random_best_thread, island_number, broad_size, percentageOfBestIndividualsForMigrationPerIsland, migrant_index):
    random_best_thread = randint(0, broad_size - 1)
    while random_best_thread == island_number or migrant_index[island_number] == percentageOfBestIndividualsForMigrationPerIsland:
        random_best_thread = randint(0, broad_size - 1)


def do_migration2(island_content, island_number, num_islands, island_fitness, mig_policy_size, broadcast):
    if isMigrationNeed(broadcast) == 0:
        return
    else:
        #migrant_index = []
        #for i in range(num_islands):
        #    broadcast[i] = sorted(broadcast[i], reverse=False, key=cycle.takeSecond)
        #    migrant_index.append(0)

        archipelago = []
        for i in range(num_islands):
            island = broadcast[i]
            for j in range(len(island)):
                archipelago.append(island[j])
        archipelago = sorted(archipelago, reverse=False, key=cycle.takeSecond)

        worst_gen_list = []
        count = 0
        for individuo in range(len(island_fitness)):
            worst_gen_list.append([island_fitness[individuo], count])
            count += 1

        print('Migrating', island_number)

        sorted_worst_gen_list = sorted(worst_gen_list, reverse=False, key=cycle.takeFirst)
        iter = 0
        while iter < mig_policy_size*(len(island_content)):
            #random_best_thread = -1
            #broad_size = len(broadcast)
            #find_island(random_best_thread, island_number, broad_size, mig_policy_size, migrant_index)
            worst_fit = sorted_worst_gen_list[iter][0]
            #best_thread = broadcast[random_best_thread]
            #best_fit_value = best_thread[migrant_index[island_number]]
            #migrant_index[island_number] += 1
            #best_fit_list = best_fit_value[1]
            #best_fit = best_fit_list[0]

            best_fit_selected = archipelago[iter]
            best_fit = best_fit_selected[1][0]

            #print('Comparing:', worst_fit, 'with', best_fit_selected[0], 'that has', best_fit)

            if worst_fit < best_fit:
                island_content[sorted_worst_gen_list[iter][1]] = best_fit_selected[0]
            iter = iter + 1

        print('Migration', island_number, 'concluded')
        return