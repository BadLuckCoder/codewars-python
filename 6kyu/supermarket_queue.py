def queue_time(customers, n):
    
    machines = [0] * n
    
    for customer in customers:
        
        min_machine_index = machines.index(min(machines))
        
        machines[min_machine_index] += customer
        
    return max(machines)