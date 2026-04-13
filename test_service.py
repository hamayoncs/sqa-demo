def calculate_technician_fee(hours_worked, is_emergency=False):
    # SQA Rule 1: Catch invalid system inputs
    if hours_worked < 0:
        raise ValueError("Hours worked cannot be negative")

    base_visit_fee = 500  # Rs
    hourly_rate = 800     # Rs per hour

    # SQA Rule 2: Apply standard billing math
    total_fee = base_visit_fee + (hours_worked * hourly_rate)

    # SQA Rule 3: Apply business conditions (Emergency surcharge)
    if is_emergency:
        total_fee += 1000

    return total_fee
#the test file