from os import add_dll_directory
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


# 面对对象编程
# class Animal(object):
#     def run(self):
#         return('Animal is running...')
# dog= Animal()
# print(dog.run())
# 或者
class Animal(object):
    def run(self):
        print('Animal is running...')
dog= Animal()
dog.run()


# 继承:继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
class Animal(object):
    def run(self):
        print('Animal is running...')
dog.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog = Dog()
dog.eat()
cat=Animal()

cat.run()
print(isinstance(dog, Animal))
# 判断类型
def run_twice(Animal):
    Animal.run()
    Animal.run()
class cat(Animal):
    pass
run_twice(cat())
type(123)
# 类型
print(isinstance(125,int))
print(isinstance([1, 2, 3], (list, tuple)))
print(dir(dog))
print('ABC'.lower())
class MyObject(object):
     def __init__(self):
        #__slots__(self):则不能添加绑定属性 其中 myobject 的子类会把slots当作init 
         self.x = 9
     def power(self):
      return self.x * self.x
obj=MyObject()
hasattr(obj, 'x') # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(getattr(obj, 'y',404) )# 获取属性'y'
print(getattr(obj, 'z',404) )# 获取属性'z',如果没有则报错404
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        print(nums)
        return len(nums)
      
print(Solution.removeDuplicates('adc',[1,1,3,7,8,8,9]))
print(type('adc')) 
class Solution(object):
    def removeDuplicates(self, nums):
        N = len(nums)
        left = 0
        for right in range(1, N):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left + 1
# 记得定义实例
s=Solution()
print(s.removeDuplicates([1,1,3,7,8,8,9]))