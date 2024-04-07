import math
import time


class FPSManager:
    def __init__(self, target: float, n: int):
        self._n = n
        self.times: list[float] = [0.0 for _ in range(n)]
        self.intervals: list[float] = [0.0 for _ in range(n)]

        self._count: int = -n
        self.skip_rate: float = 1.0 / (n + 1)
        self._skip_tank: float = 0
        self._skip_co: list[float] = [1.0 / (n + 1), target, 1, 0.0018]

    def record(self):
        self.times.append(
            time.time()
        )
        self.times.pop(0)

        self.intervals.append(
            self.times[-1] - self.times[-2]
        )
        self.intervals.pop(0)

        if self._count > self._n:
            self._count = 0
        self._count += 1

    def _skip_rate_func_fitting(self, ave_interval: float, learning_rate: float = 0.001):
        a = self._skip_co[0]
        b = self._skip_co[1]
        c = self._skip_co[2]
        d = self._skip_co[3]
        k = 2 * self.skip_rate / (a - c) - (a + c) / (a - c)

        a1 = (2 * self.skip_rate - (a + c)) / ((a - c) ** 2)
        a2 = c / (a - c)
        da = (b - d) * 0.5 / (math.cosh(k) ** 2) * (a1 - a2)

        db = 0.5 * math.tanh(k) + 0.5

        c1 = (2 * self.skip_rate + a + c) / ((a - c) ** 2)
        c2 = a / (a - c)
        dc = (b - d) * 0.5 / (math.cosh(k) ** 2) * (c1 - c2)

        dd = -0.5 * math.tanh(k) + 0.5

        t = (d - b) / (c - a) * self.skip_rate + b - (d - b) / (c - a) * a
        h = t - ave_interval
        self._skip_co[0] -= h * da * learning_rate
        self._skip_co[1] -= h * db * learning_rate
        self._skip_co[2] -= h * dc * learning_rate
        self._skip_co[3] -= h * dd * learning_rate

        if self._skip_co[0] < 0:
            self._skip_co[0] = 0
        if self._skip_co[2] > 1:
            self._skip_co[2] = 1
        if self._skip_co[0] >= self._skip_co[2]:
            self._skip_co[0] = (self._skip_co[0] + self._skip_co[2]) * 0.5
            self._skip_co[2] = self._skip_co[0] + 0.00001

    def _calc_skip_rate(self, target: float):
        if target >= self._skip_co[1]:
            return self._skip_co[0]
        elif target <= self._skip_co[3]:
            return self._skip_co[2]
        return (
                (target - self._skip_co[1])
                * (self._skip_co[2] - self._skip_co[0])
                / (self._skip_co[3] - self._skip_co[1])
                + self._skip_co[0]
        )

    def render_or_not(self, target: float, ave_interval: float | None = None):
        # if ave_interval is None:
        #     ave_interval = self.ave_interval()

        if self._count == self._n:
            # self._skip_rate_func_fitting(ave_interval, 0.01)
            self.skip_rate = self._calc_skip_rate(target)

        if self._skip_tank > 0:
            self._skip_tank -= 1
        else:
            self._skip_tank += 1.0 / self.skip_rate
            return False

        return True

    def ave_interval(self):
        return sum(self.intervals) / len(self.intervals)
