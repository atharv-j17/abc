def berkeley_algorithm(time_offsets):
    avg_offset = sum(time_offsets) / len(time_offsets)
    return [time - avg_offset for time in time_offsets]

time_offsets = [1.2, 0.5, -0.3, 2.1, -1.0]
adjusted_clocks = berkeley_algorithm(time_offsets)
print(adjusted_clocks)
