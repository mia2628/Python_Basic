from collections import deque

n, m = map(int, input().split())#n,m을 공백으로 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input()))) #2차원 배열 생성

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1] #상하좌우

#bfs 구현
def bfs(x, y):
  queue = deque()
  queue.append((x,y)) # 왜 괄호 2개임?
  #큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    #현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      #벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  #가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

#bfs를 수행한 결과 출력
print(bfs(1,0))