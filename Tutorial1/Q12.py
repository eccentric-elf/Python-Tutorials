def sum_and_average(numbers):
    pos_nums = [num for num in numbers if num > 0]
    neg_nums = [num for num in numbers if num < 0] 

    pos_sum = sum(pos_nums)
    pos_avg = pos_sum / len(pos_nums) if pos_nums else 0

    neg_sum = sum(neg_nums)
    neg_avg = neg_sum / len(neg_nums) if neg_nums else 0

    return pos_sum, pos_avg, neg_sum, neg_avg

nums = [int(input(f"Enter number {i+1}: ")) for i in range(4)]

pos_sum = sum_and_average(nums)
pos_avg = sum_and_average(nums)
neg_sum = sum_and_average(nums)
neg_avg = sum_and_average(nums)

print(f"Sum of positive numbers: {pos_sum}")
print(f"Average of positive numbers: {pos_avg:.2f}")
print(f"Sum of negative numbers: {neg_sum}")
print(f"Average of negative numbers: {neg_avg:.2f}")
