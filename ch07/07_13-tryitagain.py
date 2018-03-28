sandwich_orders = ['ham', 'turkey', 'reuben']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    finished_sandwiches.append(order)

for sandwich in finished_sandwiches:
    print("Order up! " + sandwich + " is ready!")