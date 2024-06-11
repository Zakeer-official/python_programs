def TowerOfHanoi(n, source_name, auxiliary_name, destination_name, towers):
    if n == 1:
        disk = towers[source_name].pop()
        towers[destination_name].append(disk)
        print(f"Move disk {disk} from {source_name} to {destination_name}")
        print_towers(towers)
        return
    
    TowerOfHanoi(n - 1, source_name, destination_name, auxiliary_name, towers)
    disk = towers[source_name].pop()
    towers[destination_name].append(disk)
    print(f"Move disk {disk} from {source_name} to {destination_name}")
    print_towers(towers)
    TowerOfHanoi(n - 1, auxiliary_name, source_name, destination_name, towers)

def print_towers(towers):
    print(f"Rod A: {sorted(towers[0], reverse=True)}")
    print(f"Rod B: {sorted(towers[1], reverse=True)}")
    print(f"Rod C: {sorted(towers[2], reverse=True)}")
    print()

# Initializing the towers with descriptive names
towers = [[3, 2, 1],[],[]]  

print("Initial State:")
print_towers(towers)

TowerOfHanoi(len(towers[0]), 0, 1, 2, towers)
