def calculate_technician_fee(hours_worked, is_emergency=False):
    if hours_worked < 0:
        raise ValueError("Hours worked cannot be negative")

    base_visit_fee = 500  
    hourly_rate = 800     

    total_fee = base_visit_fee + (hours_worked * hourly_rate)

    if is_emergency:
        total_fee -= 1000

    return total_fee