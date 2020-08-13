def isHappy(self, n, answer_set=None):
        if answer_set == None:
            answer_set = set()
        if n == 1:
            return True
        elif n in self.answer_set:
            return False

        new_num = sum([int(digit)**2 for digit in str(n)])
        self.answer_set.add(n)
        return self.isHappy(new_num, answer_set)