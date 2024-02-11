def hanoi(n, source, target, auxiliary):
    """Print the sequence of moves needed to transfer n disks from source to target using auxiliary"""
    if n > 0:
        # Move n-1 disks from source to auxiliary, so they are out of the way
        hanoi(n-1, source, auxiliary, target)

        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks that we left on auxiliary to target
        hanoi(n-1, auxiliary, target, source)

# Start by moving 3 disks from needle 1 to needle 3 using needle 2
hanoi(3, '1', '3', '2')