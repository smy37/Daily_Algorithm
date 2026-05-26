from typing import List
from collections import deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        target_idx_list = []
        visit = {id: True}
        dq = deque()
        dq.append([id, 0])

        while dq:
            cur, cur_level = dq.popleft()

            if cur_level < level:
                for next_f in friends[cur]:
                    if next_f not in visit:
                        visit[next_f] = True
                        dq.append([next_f, cur_level + 1])

                        if cur_level + 1 == level:
                            target_idx_list.append(next_f)

        video_dict = {}

        for idx in target_idx_list:
            for video in watchedVideos[idx]:
                if video not in video_dict:
                    video_dict[video] = 0
                video_dict[video] += 1

        answer = sorted(video_dict.items(), key=lambda x: [x[1], x[0]])

        return [item[0] for item in answer]