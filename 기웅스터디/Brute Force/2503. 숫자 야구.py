N = int(input())
game = []
for _ in range(N):
    k = map(int, input().split())
    game.append([k])

print(game)