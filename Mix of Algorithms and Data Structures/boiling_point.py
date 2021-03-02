boiling_map = { 'Butane': -0.5,
                'Copper': 1187,
                'Gold': 2660,
                'Mercury': 357,
                'Methane': -161.7,
                'Nonane': 150.8,
                'Selver': 2197,
                'Watter': 100}

def boiling_material(boiling_map, boiling_point):
    l_negative_value = list()
    l_negative_material = list()
    l_postive_value = list()
    l_postive_material = list()
    first_bound = boiling_point - boiling_point * 0.02
    second_bound = boiling_point + boiling_point * 0.02
    for material, value in boiling_map.items():
        if value > 0:
            l_postive_value.append(value)
            l_postive_material.append(material)
        else:
            l_negative_material.append(material)
            l_negative_value.append(value)

    if boiling_point > 0:
        for value in l_postive_value:
            if first_bound <= value <= second_bound:
                index = l_postive_value.index(value)
                return l_postive_material[index]
    else:
        for value in l_negative_value:
            if first_bound <= value <= second_bound:
                index = l_negative_value.index(value)
                return l_negative_material[index]

    return 'Unknown'

# def boiling_material(boiling_map, boiling_point):
#     for matirial, value in boiling_map.items():
#         first_bound = boiling_point - boiling_point * 0.05
#         second_bound = boiling_point + boiling_point * 0.05
#         compare = first_bound <= value <= second_bound
#         if first_bound <= value <= second_bound:
#             return matirial
#     return 'Unknown'
print(boiling_material(boiling_map, -0.475))