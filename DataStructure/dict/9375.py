t = int(input())

for _ in range(t):
    n = int(input())
    cloth_dict = {}
    result = 1

    for i in range(n): # 각 종류별 가짓수 세기
        name, ty = map(str, input().split())

        if(ty in cloth_dict): # 해당 type의 옷이 등장한 경우는 갯수 + 1
            cloth_dict[ty] += 1
        else: # 해당 type의 옷이 처음 등장한 경우는 가짓수를 세기 위한 키 생성
            cloth_dict[ty] = 1

    for i in cloth_dict: # 각 type별 개수 + 1 (선택하지 않는 경우의 수)를 결과에 곱해주기
        result *= cloth_dict[i] + 1

    print(result - 1) # 알몸인 경우 제외하고 결과 출력
