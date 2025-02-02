def unique_elements():
    nums = input("Enter numbers separated by spaces: ").split()
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    print(unique_list)

unique_elements()
