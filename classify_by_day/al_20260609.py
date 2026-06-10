from collections import deque


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        dq = deque(intervals)
        net_interval = []
        s, e = newInterval
        flag = False

        while dq:
            cur_interval = dq.popleft()
            cur_s, cur_e = cur_interval

            if e < cur_s:
                net_interval.append([s, e])
                net_interval.append([cur_s, cur_e])
                flag = True
                break
            elif cur_s <= e <= cur_e:
                s = min(s, cur_s)
                e = max(e, cur_e)
            elif e > cur_e:
                if s > cur_e:
                    net_interval.append([cur_s, cur_e])
                elif s <= cur_e:
                    s = min(s, cur_s)
        if not flag:
            net_interval.append([s, e])
        while dq:
            net_interval.append(dq.popleft())
        if not intervals:
            return [newInterval]
        return net_interval