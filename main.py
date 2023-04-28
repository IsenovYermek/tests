class FindDuplicates:
    def __init__(self, nums):
        self.nums = nums

    def find_duplicates(self):
        n = len(self.nums) - 2
        count = [0] * (n + 1)
        duplicates = []
        for num in self.nums:
            count[num - 1] += 1
            if count[num - 1] == 2:
                duplicates.append(num)
        return duplicates


nums = [1, 2, 5, 2, 6, 7, 5, 4, 5, 9, 8]
fd = FindDuplicates(nums)
print("Исходный массив:", nums)
print("Повторяющиеся числа:", fd.find_duplicates())
