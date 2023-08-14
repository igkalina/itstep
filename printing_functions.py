def print_models(unprinted_designs, complete_models):
    while unprinted_designs:
        current_desing = unprinted_designs.pop()
        print(f'Printing model: {current_desing}')
        complete_models.append(current_desing)
    return complete_models