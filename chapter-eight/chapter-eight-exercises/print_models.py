def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that are printed"""
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)