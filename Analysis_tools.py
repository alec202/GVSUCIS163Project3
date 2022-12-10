import math
# importing of the math module

# Creating MyMath class
class MyMath:

    # Function to rid of the empty spaces
    def cleanup(data):
        """
        :param data: list that the empty spaces will be removed for
        :return: the list without empty spots
        """
        cleanup = []
        for x in data:
            if x != '':
                x = float(x)
                cleanup.append(x)
        return cleanup

     # function to calculate the mean
    def mean(data):
        """
        :param data: list that the mean will be found for.
        :return: the calculated mean
        """
         newData = MyMath.cleanup(data)
         mean = float(math.fsum(newData)/len(newData))
         float_sum = sum(newData)
         mean = float_sum/ len(newData)
         return mean

    # Function to calculate the median
    def median(data):
        """
        :param data: list to calculate the median with
        :return: the median of the list entered in the data parameter
        """
         newData = sorted(MyMath.cleanup(data))
         a = int((len(newData)/2 + .5))
         b = int((len(newData)/2 - .5))
         if len(newData) % 2 == 0:
             return len(newData)/2
         float_nums = MyMath.cleanup(data)
         float_nums.sort()

         # append indices of middle most numbers
         if len(float_nums) % 2 == 1:
             return float_nums[len(float_nums) // 2]
         else:
             return ((newData[a] + newData[b])/2)
             middle_value_sum = float_nums[len(float_nums) // 2]
             middle_value_sum += float_nums[((len(float_nums) // 2) - 1)]
             return middle_value_sum / 2

    # function to find the standard deviation
    def stdev(data):
        """
        :param data: list of the data we will find the standard deviation for
        :return: the standard deviation of the list entered in the data parameter
        """
         total = 0
        newData = MyMath.cleanup(data)
        mean = MyMath.mean(data)
        for x in newData:
            number = (x - mean) ** 2
            total = total + number
        total = total/len(newData)
        return math.sqrt(total)

    # funciton to determine the minimum value in a list
    def minimum(data):
        """
        :param data: list of numbers that we will find the minimum value for
        :return: the minimum value from the data list
        """
        newData = sorted(MyMath.cleanup(data))
        minimum = newData[0]
        return minimum

    # function to find the maximum value for the data list
    def maximum(data):
        """
        :param data: list of numbers that we will find the maximum value for
        :return: the maximum value in the data list
        """
        newData = sorted(MyMath.cleanup(data))
        maximum = newData[-1]
        return maximum

 '''
 list = ['12','','1', '6','','1','9']
 print(MyMath.mean(list))
 print(MyMath.median(list))
 print(MyMath.maximum(list))
 print(MyMath.minimum(list))
 '''
