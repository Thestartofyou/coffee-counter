data = {
    "8:00am": 10,
    "9:00am": 20,
    "10:00am": 25,
    "11:00am": 30,
    "12:00pm": 35,
    "1:00pm": 30,
    "2:00pm": 25,
    "3:00pm": 20,
    "4:00pm": 15,
    "5:00pm": 10
}

averages = {}
for interval, count in data.items():
    hour = int(interval.split(":")[0])
    if hour not in averages:
        averages[hour] = [count, 1]
    else:
        averages[hour][0] += count
        averages[hour][1] += 1

max_average = 0
busiest_intervals = []
for hour, (total_count, num_intervals) in averages.items():
    average_count = total_count / num_intervals
    if average_count > max_average:
        max_average = average_count
        busiest_intervals = [hour]
    elif average_count == max_average:
        busiest_intervals.append(hour)

print("The coffee shop is busiest during the following intervals:")
for hour in busiest_intervals:
    print(f"{hour}:00am to {hour+1}:00am")
