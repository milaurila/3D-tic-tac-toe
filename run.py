from treirad import *
import time

def main():
    """User interface for functions defined in treirad.py.

    Make sure this file is in the same directory as treirad.py.

    Prompts user for inputs which are sent to functions in
    treirad.py. Results of the simulation is output to the terminal
    and a pdf file with a plot of the results created in the script
    directory.
    Valid input is ensured by excepts and conditions.
    Entering 'exit' at any prompt exits the script.

    The time module is used to time the simulation.
    """

    print('Välkommen till Tre-i-Rad Simulator 2020')
    print("Skriv 'exit' när som för att avsluta.")
    print('---------------------------------------')

    while True:
        try:
            dim = input('I vilken dimension vill du simulera? (2/3) ')
            if dim == 'exit':
                return
            dim = int(dim)
        except:
            print('Ange en giltig dimension (2 eller 3).')
            continue
        if dim < 2:
            print('Ange en giltig dimension (2 eller 3).')
        elif dim > 3:
            print('Ange en giltig dimension (2 eller 3).')
        else:
            break

    if dim == 2:
        while True:
            try:
                size = input('Hur stort bräde? (3/5/7/9/...) ')
                if size == 'exit':
                    return
                size = int(size)
            except:
                print('Ange en giltig storlek (udda heltal > 1).')
                continue
            if size < 3 or size % 2 != 1:
                print('Ange en giltig storlek (udda heltal > 1).')
            else:
                break

    while True:
        try:
            scenario = input(f'Vilket scenario ska spelas?\n1: Alla drag'
                             f' slumpas.\n2: Första draget spelas i mitten.\n')
            if scenario == 'exit':
                return
            scenario = int(scenario)
        except:
            print('Ange ett giltigt scenario (1 eller 2).')
            continue
        if scenario < 1 or scenario > 2:
            print('Ange ett giltigt scenario (1 eller 2).')
        else:
            break

    while True:
        try:
            rounds = input('Hur många partier vill du simulera? ')
            if rounds == 'exit':
                return
            rounds = int(rounds)
        except:
            print('Ange ett giltigt antal partier (positivt heltal).')
            continue
        if rounds < 1:
            print('Ange ett giltigt antal partier (positivt heltal).')
        else:
            break
    print()

    if dim == 3:
        size = 3
    # Timing
    start_time = time.time()
    sims = simulation(dim, size, scenario, rounds)
    total_time = '{0:0.1f}'.format(time.time() - start_time)

    print(f'--- Utfall av {rounds} partier Tre-i-rad på ett {dim}-dimensionellt'
          f' bräde av storlek {size} ---\n')

    if scenario == 1:
        print('Spelare 1 slumpade sitt första drag.')
    elif scenario == 2:
        print('Spelare 1 spelade sitt första drag i mitten.')

    print(f'Vinster spelare 1: {sims[0]}\n'
          f'Vinster spelare 2: {sims[1]}\n'
          f'Remier: {sims[2]}\n')
    print(f'Simuleringen tog {total_time} sekunder.\n')

    plot_results(*sims, dim, size, scenario)
    print("En figur som visar utfallet är sparad i filen 'utfall.pdf'.")

main()
