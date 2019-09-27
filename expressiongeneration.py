from typing import List
import random


class Generationsystem:
    def generation(self, length: int) -> List:
        result = []
        for i in range(length - 1):
            result.append(random.randint(1, 99))
            k = random.randint(1, 4)
            # print(k)
            if k == 1:
                result.append("+")
            elif k == 2:
                result.append("-")
            elif k == 3:
                result.append("x")
            else:  # k=4
                result.append("÷")
        result.append(random.randint(1, 99))
        return result

    def generation2(self, length: int) -> List:  # 生成整除式子,且不会同时出现2个连在一起的/
        flag = 0
        x = 0
        result = []
        for i in range(length):
            if flag == 1:
                flag = 0  # flag复位否则就会出现bug
                result.append(x)
                if i == length - 1:
                    result_str = str(result)
                    if eval(result_str.replace("x", "*").replace("÷", "/")) < 0:
                        print(result_str)
                        return self.generation2(length)
                    else:
                        return result
                k = random.randint(1, 3)
                print(k)
                if k == 1:
                    result.append("+")
                elif k == 2:
                    result.append("-")
                else:
                    result.append("x")
            else:
                if i == length - 1:
                    result.append(random.randint(1, 99))
                    return result
                k = random.randint(1, 4)
                print(k)
                if k == 1:
                    result.append(random.randint(1, 99))
                    result.append("+")
                elif k == 2:
                    result.append(random.randint(1, 99))
                    result.append("-")
                elif k == 3:
                    result.append(random.randint(1, 99))
                    result.append("x")
                else:
                    flag = 1
                    x = random.randint(1, 99)
                    n = random.randint(2, 9)
                    result.append(n * x)
                    result.append("÷")

    def generation_no_negative_numbers(self, length: int) -> List:  # 一个表达式中最多一个除法符号，并且最多一组括号对
        flag1 = 0  # 检查是否有除法符号
        x = 0
        result = []
        count = 2
        k = random.randint(1, 4)  # +,-,*,/
        if k == 4:
            x = random.randint(1, 99)
            n = random.randint(2, 9)
            result.append(n * x)
            result.append("÷")
            result.append(x)
            flag1 = 1
        else:
            result.append(random.randint(1, 99))
            if k == 3:
                result.append("x")
                result.append(random.randint(1, 9))
            elif k == 2:
                result.append("-")
                result.append(random.randint(1, 99))
            else:
                result.append("+")
                result.append(random.randint(1, 99))
        while (count < length):  # 当进入这个循环的时候，保证表达式是一个可以计算的算式
            result_str1 = [str(i) for i in result]
            result_str = ''.join(result_str1)
            if eval(result_str.replace("x", "*").replace("÷", "/")) < 0:
                result = self.generation_no_negative_numbers(count)
            count += 1
            if flag1 == 1:  # 出现过除法
                k = random.randint(1, 3)
                if k == 1:
                    result.append("+")
                    result.append(random.randint(1, 99))
                elif k == 2:
                    result.append("-")
                    result.append(random.randint(1, 99))
                else:
                    result.append("x")
                    result.append(random.randint(1, 9))
            else:
                k = random.randint(1, 3)
                if k == 1:
                    result.append("+")
                    result.append(random.randint(1, 99))
                elif k == 2:
                    result.append("-")
                    result.append(random.randint(1, 99))
                elif k == 3:
                    result.append("x")
                    result.append(random.randint(1, 99))
                else:
                    flag1 = 1
                    result.pop()
                    n = random.randint(1, 9)
                    x = random.randint(1, 99)
                    result.append(n * x)
                    result.append("÷")
                    result.append(x)
        result_str0 = [str(i) for i in result]
        result_str2 = ''.join(result_str0)
        if eval(result_str2.replace("x", "*").replace("÷", "/")) < 0:
            result = self.generation_no_negative_numbers(count)
        return result

    def generation3(self, length: int) -> List:  # 生成一个有括号的表达式但是不能保证其非负
        result = []
        result = self.generation_no_negative_numbers(length)
        i = random.randint(0, len(result) - 3)
        while i % 2 == 1:
            i = random.randint(0, len(result) - 3)
        result.insert(i, "(")
        j = random.randint(i + 4, len(result))
        while j % 2 == 1:
            j = random.randint(i + 4, len(result))
        result.insert(j, ")")
        result_str0 = [str(i) for i in result]
        result_str2 = ''.join(result_str0)
        if eval(result_str2.replace("x", "*").replace("÷", "/")) < 0:
            result = self.generation3(length)
        return result

if __name__ == '__main__':
    k = input("input an integer:(done to end)")
    while not k == "done":
        k = int(k)
        solution = Generationsystem()
        print(solution.generation3(k))
        k = input("input an integer:(done to end)")

