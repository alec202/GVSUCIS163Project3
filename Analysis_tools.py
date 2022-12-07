import math


class MyMath:
    @staticmethod
    def cleanup(data):
        float_list = []
        for string in data:
            if data != "":
                float_list.append(float(string))

        return float_list
      
    @staticmethod
    def mean(data):
        float_data = MyMath.cleanup(data)
        float_sum = sum(float_data)
        mean = float_sum / len(float_sum)
        return mean

    def median(data):
        float_nums = MyMath.cleanup(data)
        float_nums.sort()

        # append indices of middle most numbers
        if len(float_nums) % 2 == 1:
            return float_nums[len(float_nums) // 2]
        else:
            middle_value_sum = float_nums[len(float_nums) // 2]
            middle_value_sum += float_nums[((len(float_nums) // 2) - 1)]
            return middle_value_sum / 2

    @staticmethod
    def stdev(data):
        float_nums = MyMath.cleanup(data)
        mean = MyMath.mean(data)
        difference_sum = 0
        for num in float_nums:
            difference_sum += (num - mean) ** 2
        avg = difference_sum / len(float_nums)
        math.sqrt(avg)

    @staticmethod
    def minimum(data):
        float_list = MyMath.cleanup(data)
        return min(float_list)

    @staticmethod
    def maximum(data):
        float_list = MyMath.cleanup(data)
        return max(float_list)











