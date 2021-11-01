def two_sum(nums, target):
    my_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in my_dict:
            return [ my_dict[ target - nums[i]], i]
        else:
            my_dict[nums[i]] = i
    return target.values()



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
