def minMergeCost(stones, left, right):
    n = len(stones)

    # 돌 더미가 하나라면 비용은 0
    if n == 1:
        return 0

    # 누적합을 구하여 구간 합을 빠르게 계산
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stones[i]

    # dp[i][j]는 i번째 돌부터 j번째 돌까지 합쳤을 때 최소 비용
    dp = [[float('inf')] * n for _ in range(n)]

    # 길이가 1인 구간은 비용이 0
    for i in range(n):
        dp[i][i] = 0

    # 구간 길이가 2 이상일 때 합병 비용 계산
    for length in range(2, n + 1):  # 구간의 길이
        for i in range(n - length + 1):
            j = i + length - 1
            # [i, j] 구간을 합칠 때, 중간 점을 기준으로 분할
            for k in range(i, j):
                # [i, j] 구간의 합은
                total_cost = prefix_sum[j + 1] - prefix_sum[i]
                # 합병 비용이 left와 right 사이일 때만 유효
                if left <= total_cost <= right:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + total_cost)

    # 전체 구간을 합쳤을 때의 최소 비용
    return dp[0][n - 1] if dp[0][n - 1] != float('inf') else 0


# 예시 실행
stones = [1,2,3]  # 돌 더미 크기
left = 2        # 합병 비용 최소 범위
right = 3             # 합병 비용 최대 범위

result = minMergeCost(stones, left, right)
print(result)  # 예상 결과 값 10
