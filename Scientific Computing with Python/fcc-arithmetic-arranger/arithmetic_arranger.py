def arithmetic_arranger(problems, flag=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    for i in range(len(problems)):
        if problems[i].split()[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        elif (len(problems[i].split()[0]) > 4) or (len(problems[i].split()[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        elif not problems[i].split()[0].isnumeric() or not problems[i].split()[2].isnumeric():
            return "Error: Numbers must only contain digits."

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for i in range(len(problems)):
        sep = problems[i].split()
        width = max(len(sep[0]), len(sep[2]))
        line1 += "{:{align}{width}}".format(sep[0], align='>', width=width+2)
        line2 += "{:<} {:{align}{width}}".format(sep[1], sep[2], align='>', width=width)
        line3 += '-'*(width+2)

        if flag:
            if sep[1] == '+':
                res = int(sep[0]) + int(sep[2])
            else:
                res = int(sep[0]) - int(sep[2])
            line4 += "{:{align}{width}}".format(res, align='>', width=width+2)

        if i != len(problems)-1:
            line1 += ' '*4
            line2 += ' '*4
            line3 += ' '*4
            if flag:
                line4 += ' '*4

    if not flag:
        return line1 + '\n' + line2 + '\n' + line3
    else:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
