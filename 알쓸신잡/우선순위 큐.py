import heapq
# 우선순위 큐 -> 이진힙 -> heapq 라이브러리 사용
pq = []
heapq.heappush(pq, (0, 0))  # 우선순위에 따라 뽑아올 수 있음
                        # 원소의 첫번째 요소를 보고 뽑아오는 것
