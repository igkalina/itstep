sandwich_orders = ['pastrami','pastrami','pastrami','ketchup','mustard']
sandwich_finiched = []
print('pastrami is not')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
sandwich_finiched = sandwich_orders[:]
print(sandwich_finiched)