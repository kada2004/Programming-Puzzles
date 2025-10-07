#num_disks=2 try to solve for 2 first

num_disks = 2
A_list = ["Disc 1", "Disc 2"]  # Source (top , bottom)
B_list = []                    # Auxiliary
C_list = []                    # Target

def tower(A_list, B_list, C_list, n=num_disks):

    #base case
    if n == 0:
        return A_list, B_list, C_list

    # Move n-1 disks from A to B using C
    tower(A_list, C_list, B_list, n - 1)
    print(f" Dan State: A = {A_list}, B = {B_list}, C = {C_list}")

    # Move the top disk (last in list) from A to C
    if len(A_list) >= 1:
        disk = A_list[-1]          # Get top disk (end of list)
        A_list.pop()               # Remove top disk
        print("A_list Happy Peope",disk)
        C_list.append(disk)        # Place it on target
        print(f"Moved {disk} from A to C")
        print(f"State: A = {A_list}, B = {B_list}, C = {C_list}")

    # Move n-1 disks from B to C using A
    tower(B_list, A_list, C_list, n - 1)

    return A_list, B_list, C_list

result = tower(A_list, B_list, C_list)
print("\nFinal result:", result)

