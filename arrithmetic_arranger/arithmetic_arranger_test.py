#Arithmetic arranger function

def arithmetic_arranger(problems, yn=False):

    all_probs = []
    buff = []
    x = 0
    calc = 2
    error = 0
    accepted_operands= "+-"

    #If the second agrument is True we have to print the answer 
    if yn == True :
        calc = 3

    for problem in problems :
        sproblem = problem.split()
        # If the operands are + or - continue, if not return error
        if any(c in accepted_operands for c in sproblem[1]):
            all_probs.append((sproblem[0], sproblem[1], sproblem[2]))
        else :
            error = 2

    # If we have more than 5 problems to solve return error        
    if len(all_probs) > 5 :
        error = 1

    for prob in all_probs :
        largest = max(len(prob[0]), len(prob[2]))
        
        #If one of the numbers is more than 4 digits
        if largest > 4 :
            error = 4
        prob0=prob[0]
        prob2=prob[2]
        
        if not (prob0.isdigit() and prob2.isdigit()):
          return "Error: Numbers must only contain digits."
        elif (prob0.isdigit() and prob2.isdigit()):
          if prob[1] == "+" :
              ans = int(prob0) + int(prob2)
          elif prob[1] == "-" :
              ans = int(prob0) - int(prob2)
            
          buff_size = largest + 2
          buff1 = prob[0].rjust(buff_size)
          buff2 = prob[1] + " " + prob[2].rjust(largest)
          buff3 = "-"*buff_size
          buff4 = str(ans).rjust(buff_size)

          buff.append((buff1, buff2, buff3, buff4))

    #If there are more than 5 problems, return error 
    if len(all_probs) > 5 :
        error = 1

    amount = len(all_probs) - 1
    arranged_problems = ""
    n = '\n'
    while x <= calc :
        
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

    if error == 1:
        arranged_problems = "Error: Too many problems."
    elif error == 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
    elif error == 3:
        arranged_problems = "Error: Numbers must only contain digits."
    elif error == 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."

    return arranged_problems


print(arithmetic_arranger(['32 + 698', '1 - 3071', '45 + 43', '123 + 49', '988 + 460'], True))
