
# determine angle the minute hand turns if f is the degrees of the hour hand's turn since midnight
def hand_turned(f):
    print(f % 30 * 12)


hand_turned(190)
hand_turned(5)
hand_turned(29)