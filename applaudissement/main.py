def resolve(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

    N = int(lines[0])
    results = []

    for case_num in range(1, N + 1):
        Tmax_str, people_str = lines[case_num].split()
        Tmax = int(Tmax_str)

        nb_debouts = 0
        nb_amis = 0

        for i in range(Tmax + 1):
            nb_personnes = int(people_str[i])

            if nb_debouts < i:
                amis_needed = i - nb_debouts
                nb_amis += amis_needed
                nb_debouts += amis_needed

            nb_debouts += nb_personnes

        results.append(f"Case #{case_num}: {nb_amis}")

    with open(output_file, 'w') as f:
        f.write("\n".join(results))

# Exemple d'utilisation :

resolve('input_file.txt', 'output_file.txt')
