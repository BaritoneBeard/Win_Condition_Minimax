with open('graphs.txt', 'r') as document:
    answer = {}
    for line in document:
        line = line.split()
        if not line:
            continue
        answer[line[0]] = line[1:]

print(answer)