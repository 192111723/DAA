def container_loader(items, container_capacity):
    containers = []
    current_container = []
    for item in items:
        if sum(current_container) + item <= container_capacity:
            current_container.append(item)
        else:
            containers.append(current_container)
            current_container = [item]
    containers.append(current_container)
    return containers
items = [2, 3, 5, 7, 8, 9]
container_capacity = 10
loaded_containers = container_loader(items, container_capacity)
print("Loaded containers:", loaded_containers)