import operator

class DecoratorCalculator:
    def add(self, arg):
        if not isinstance(arg, _Equation):
            raise ValueError('state error')
        arg.add_op(operator.add)
        return arg

    def sub(self, arg):
        if not isinstance(arg, _Equation):
            raise ValueError('state error')
        arg.add_op(operator.sub)
        return arg

    def mul(self, arg):
        if not isinstance(arg, _Equation):
            raise ValueError('state error')
        arg.add_op(operator.mul)
        return arg

    def div(self, arg):
        if not isinstance(arg, _Equation):
            raise ValueError('state error')
        arg.add_op(operator.truediv)
        return arg

    def __call__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('not a number')
        def deco(arg):
            if isinstance(arg, _Equation):
                arg.add_value(value)
                return arg
            else:
                # arg is the reporter
                eqstate = _Equation(arg)
                eqstate.add_value(value)
                return eqstate
        return deco


class _Equation:
    def __init__(self, reporter):
        self.reporter = reporter
        self.ops_and_rights = []
        self.value = None

    def add_op(self, op):
        if self.value is None:
            raise ValueError('state error, value None')
        self.ops_and_rights.append((op, self.value))
        self.value = None

    def add_value(self, value):
        if self.value is not None:
            raise ValueError('state error, value {0}'.format(self.value))
        self.value = value

    def evaluate(self):
        if self.value is None:
            raise ValueError('cannot call, eqstate has no value')
        result = self.value
        for op, right in reversed(self.ops_and_rights):
            result = op(result, right)
        return self.reporter(result)

    def __call__(self):
        return self.evaluate()


c = DecoratorCalculator()

@c(100)
@c.add
@c(4)
@c.mul
@c(5)
@c.div
@c(10)
@c.sub
@c(10)
def report(answer):
    print('the answer is', answer)

report()
