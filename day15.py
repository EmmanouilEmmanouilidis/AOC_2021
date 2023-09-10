input = [1,12,0,20,8,16]

def memory(nums, turns):
    num_dict = {num: counter+1 for counter, num in enumerate(nums[:-1])}
    last = nums[-1]
    for i in range(len(nums),turns):
        if last in num_dict:
            new = i - num_dict[last]
        else:
            new = 0
        num_dict[last] = i
        last = new
    return last


print(memory(input, 2020))
print(memory(input, 30000000))
