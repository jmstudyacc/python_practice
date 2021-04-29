def generate_sentences(subjects, predicates, objects):
    # requirement for returned value to be sorted
    subjects.sort()
    predicates.sort()
    objects.sort()
    # new string to hold output
    res = ""
    # loop with subject 1 over predicates and objects
    # loop with subject 2 over predicates and objects
    for i in range(len(subjects)):
        for j in range(len(predicates)):
            for k in range(len(objects)):
                if (i == len(subjects) - 1) and (j == len(predicates) - 1) and (k == len(objects) - 1):
                    res += subjects[i] + " " + predicates[j] + " " + objects[k]
                    res += "."
                else:
                    res += subjects[i] + " " + predicates[j] + " " + objects[k]
                    res += ". "
    return res


assert generate_sentences(["John", "Mary"], ["hates", "loves"],
                          ["apples", "bananas"]) == "John hates apples. John hates " \
                                                    "bananas. John loves apples. John " \
                                                    "loves bananas. Mary hates apples. " \
                                                    "Mary hates bananas. Mary loves " \
                                                    "apples. Mary loves bananas."
assert generate_sentences(["Vlad", "Hubie"], ["drives"], ["car", "motorcycle", "bus"]) == "Hubie drives bus. Hubie " \
                                                                                          "drives car. Hubie drives " \
                                                                                          "motorcycle. Vlad drives " \
                                                                                          "bus. Vlad drives car. " \
                                                                                          "Vlad drives motorcycle."
