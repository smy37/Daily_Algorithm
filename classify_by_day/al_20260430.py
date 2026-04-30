import sys

while 1:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    cord_list = []

    c_x, c_y, c_z = 0, 0, 0
    for _ in range(N):
        x, y, z = map(float, sys.stdin.readline().split())
        cord_list.append([x, y, z])
        c_x += x
        c_y += y
        c_z += z

    c_x /= N
    c_y /= N
    c_z /= N

    w = 0.1
    max_dist = 0
    for _ in range(1000000):
        max_dist = 0
        max_idx = 0
        for i in range(len(cord_list)):
            x, y, z = cord_list[i]
            cur_dist = (c_x-x)**2 + (c_y-y)**2 + (c_z-z)**2

            if max_dist < cur_dist:
                max_dist = cur_dist
                max_idx = i

        m_x, m_y, m_z = cord_list[max_idx]
        c_x += (m_x-c_x)*w
        c_y += (m_y-c_y)*w
        c_z += (m_z-c_z)*w
        w *= 0.9999
    radius = max_dist**0.5
    print(f"{radius:0.5f}")
