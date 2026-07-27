class Solution():
    def mirrorReflection(self, p: int, q: int):
        cur_x, cur_y = 0, 0

        direction = "up"

        while True:

            if direction == "up":
                rest = (p-cur_y)%q
                if ((p-cur_y)//q)%2 != 0:
                    cur_x = p if cur_x == 0 else 0
                cur_y = p - rest
            else:
                rest = cur_y%q
                if (cur_y//q)%2 != 0:
                    cur_x = p if cur_x == 0 else 0
                cur_y = rest

            if (cur_x, cur_y) == (p, 0):
                return 0
            elif (cur_x, cur_y) == (p, p):
                return 1
            elif (cur_x, cur_y) == (0, p):
                return 2

            cur_x = p if cur_x == 0 else 0
            if direction == "up":
                cur_y = p-(q-rest)
                direction = "down"
            else:
                cur_y = (q-rest)
                direction = "up"
