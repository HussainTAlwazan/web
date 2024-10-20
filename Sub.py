#Tester: Hussain Alwazan
#University ID: 230049123
#Function: This function tests the subtract function implementation.


class Math:
    def sub(self, a, b):
        return a - b

def sub_test():
    sub1 = Math()
    result = sub1.sub(4, 2)
    if result == 2:
        print("Correct Implementation")
    else:
        print("Error in Implementation")

