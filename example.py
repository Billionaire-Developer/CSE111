def process_data(data):
    total = sum(data)
    average = total / len(data)
    max_value = max(data)
    min_value = min(data)
    return {
        "total" : total,
        "average" : average,
        "max" : max_value,
        "min" : min_value
    }
    
data = [1,2,3,4,5]
result = process_data(data)
print(result)
    