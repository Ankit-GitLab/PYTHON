nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

search = int(input("Enter a number those you want to find : "))
idx = 0

while idx < len(nums):

    if nums[idx] == search:
        print("index is ",idx)
   
    idx += 1