def task5(s: str) -> str:

    def __get_string(element):
        return element[1] + element[0]

    persons = s.upper().split(';')
    persons_1 = []
    for it in persons:
        persons_1.append(list(it.split(':')))
    persons_1.sort(key=__get_string)
    for i in persons_1:
        i[0], i[1] = i[1], i[0]

    for i in range(len(persons_1)):
        persons_1[i] = tuple(persons_1[i])
    string = ''.join(map(str, persons_1))
    string = string.replace("'", '')
    return string

print(task5('Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill'))