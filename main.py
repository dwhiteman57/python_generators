guests = {}

def read_guestlist(file_name):
    text_file = open(file_name, "r")
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age

        n = yield name
        if n is not None:
            name = n.strip().split(",")[0]
            age = int(n.strip().split(",")[1])
            guests[name] = age


guestlist = read_guestlist("guest_list.txt")


counter = 0
for guest in guestlist:
    counter += 1
    if counter == 10:
        guestlist.send("Jane, 35")

# print(guests)

over_21 = (name for name, age in guests.items() if age >= 21)
# print(next(over_21))
for name in over_21:
    pass
    # print(name)


def table_one():
    for i in range(1, 6):
        yield "Chicken", "Table 1", "Seat {}".format(i)


def table_two():
    for i in range(1, 6):
        yield "Beef", "Table 2", "Seat {}".format(i)


def table_three():
    for i in range(1, 6):
        yield "Fish", "Table 3", "Seat {}".format(i)


def combined_tables():
    yield from table_one()
    yield from table_two()
    yield from table_three()


combined_tables = combined_tables()


def guest_assigner():
    for name in guests.keys():
        yield name, next(combined_tables)


guest_assigner = guest_assigner()
for guest in guest_assigner:
    print(guest)