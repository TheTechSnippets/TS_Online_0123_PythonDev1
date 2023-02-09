import CustomExceptions as ce


def priya_eats(fruit_name):
    if fruit_name in ['Apple', 'Orange']:
        print("priya is eating")
    else:
        print(f"Priya doesn't like {fruit_name},she is not eating")


def maha_eats(fruit_name):
    if fruit_name in ['Banana', 'Orange']:
        print("maha is eating")
    else:
        # print(f"Maha doesn't line {fruit_name}, she is not eating")
        raise ce.MahaDoesNotLikeException(f"Maha doesn't line {fruit_name}, she is not eating")


def sowmiya_eats(fruit_name):
    if fruit_name in ['Papaya', 'Jackfruit']:
        print("Sowmiya is eating")
    else:
        raise ce.SowmiyaDoesNotLikeException(f"Maha doesn't line {fruit_name}, she is not eating")


def trainer_eats(fruit_name):
    if fruit_name in ['Papaya']:
        # other statements
        print("Trainer is eating")
    else:
        raise ce.TrainerDoesNotLikeException(f"Trainer doesn't line {fruit_name}, he is not eating")


try:
    priya_eats('Apple')
    maha_eats('Banana')
    sowmiya_eats('Papaya')
except ce.MahaDoesNotLikeException as rte:
    print(repr(rte))
except ce.SowmiyaDoesNotLikeException as rte:
    print(repr(rte))
finally:
    try:
        trainer_eats('Apple')
    except RuntimeError as rte:
        print(repr(rte))
