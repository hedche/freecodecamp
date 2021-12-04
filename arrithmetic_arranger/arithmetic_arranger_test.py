def arithmetic_arranger(problems, yn=False):

    all_probs = []
    all_ans = []
    buff = []
    x = 0
    calc = 2
    error = 0

    if yn == True :
        calc = 3
        for probl in problems :
            sprobl = probl.split()
            print(sprobl)
            if sprobl[1] == "+" or "-" :
                all_probs.append((sprobl[0], sprobl[1], sprobl[2]))
                print(all_probs)
            else :
                error = 2

    for problem in problems :
        if calc == 3 :
            break

        sproblem = problem.split()
        if sproblem[1] == "+" or "-" :
            all_probs.append((sproblem[0], sproblem[1], sproblem[2]))

        else :
            error = 2

    for prob in all_probs :
        if error == 1 or 2 or 3 or 4 :
            continue
        if prob[1] == "+" :
            ans = int(prob[0]) + int(prob[2])
            print(ans)
        elif prob[1] == "-" :
            ans = int(prob[0]) - int(prob[2])

        if len(prob) > 4 :
            error = 4
            break

        largest = max(len(prob[0]), len(prob[2]))

        buff_size = largest + 2

        buff1 = prob[0].rjust(buff_size)
        buff2 = prob[1] + " " + prob[2].rjust(largest)
        buff3 = "-"*buff_size
        buff4 = str(ans).rjust(buff_size)

        buff.append((buff1, buff2, buff3, buff4))

    if len(all_probs) > 5 :
        error = 1

    amount = len(all_probs) - 1
    arranged_problems = ""
    n = '\n'
    while x <= calc :
        if error == 1 or 2 or 3 or 4 :
            break
        y = 0
        while y <= amount :
            if y < amount :
                arranged_problems += buff[y][x] + "    "
            elif x == calc:
                arranged_problems += buff[y][x]
            elif y == amount:
                arranged_problems += buff[y][x] + n
            y = y + 1

        x = x + 1

    print(error)
    if error == 1:
        arranged_problems = "Error: Too many problems."
    elif error == 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
    elif error == 3:
        arranged_problems = "Error: Numbers must only contain digits."
    elif error == 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."

    return arranged_problems

print(arithmetic_arranger(['32 + 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
