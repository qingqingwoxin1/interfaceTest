"""
    迭代器
    让自定义对象参与for循环
    迭代自定义对象
    练习:exercise02,03
"""


class SkillIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index < len(self.data):
            return self.data[self.index]
        else:
            raise StopIteration()


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)


manager = SkillManager()
manager.add_skill("降龙十八掌")
manager.add_skill("六脉神剑")
manager.add_skill("乾坤大挪移")

# 迭代自定义对象
# for skill in manager:
#     print(skill)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  # 降龙十八掌
    except StopIteration:
        break
