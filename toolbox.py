def increment_char_map():
    characters = '123456789abcdefghijklmnopqrstuvwxyz'
    result = []
    carry = 0

    for i in range(16):
        if carry:
            next_char = characters[(carry - 1) % len(characters)]
            carry = (carry - 1) // len(characters)
        else:
            next_char = characters[i % len(characters)]
            carry = i // len(characters)
        result.append(next_char)

    return ''.join(result)

def create_shapes(x_coords, y_coords):
    shapes = []
    for x, y in zip(x_coords, y_coords):
        z = round((y / 3), 2)
        shape = f'{x},{y},{z}'
        if shape not in shapes:
            shapes.append(shape)
    return shapes

def object_array(shape_list):
    object_map = {}
    for shape in shape_list:
        if shape in object_map:
            object_map[shape] += 1
        else:
            object_map[shape] = 1

    sorted_objects = sorted(object_map.items(), key=lambda item: item[1], reverse=True)
    return sorted_objects

# Example usage:
x_coords = [1, 2, 3, 4, 1, 2, 3, 4]
y_coords = [1, 2, 3, 4, 1, 2, 3, 4]

char_map = increment_char_map()
shapes = create_shapes(x_coords, y_coords)
obj_array = object_array(shapes)

print("Character Map: ", char_map)
print("Shapes: ", shapes)
print("Object Array: ", obj_array)
