A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 질문!!!!!!!
# 이게 어떻게 같아요?? 분배법칙 했는데 %C 가 왜 그대로 있어요??