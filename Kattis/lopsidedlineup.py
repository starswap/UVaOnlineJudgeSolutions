print((lambda n : (lambda l: int(sum(l[: n // 2])/2 - sum(l[n // 2 :])/2))(sorted((sum(map(int, input().split())) for i in range(n)),reverse=True)))(n = int(input())))