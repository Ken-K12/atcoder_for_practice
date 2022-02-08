N = int(input())
num_list = [int(input()) for _ in range(N)]
print(num_list)

num_list = list(set(num_list))

print(len(num_list))