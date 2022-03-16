class TestCase:
    def __init__(self, num_of_steps):
        self._num_of_steps = num_of_steps

    @property
    def steps(self):
        return self._num_of_steps

    @steps.setter
    def steps(self, new_num):
        if new_num > self._num_of_steps:
            self._num_of_steps = new_num
        else:
            print(f'Same number of steps: {self._num_of_steps}')


tc = TestCase(5)
print(tc.steps)
tc.steps = 5
print(tc.steps)
