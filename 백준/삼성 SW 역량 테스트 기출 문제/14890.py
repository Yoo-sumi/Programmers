n,l=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))

result=0

for i in range(n):
    index=0
    block=[]
    while True:
        if index>=n-1:
            result+=1
            break

        if graph[i][index]==graph[i][index+1]:
            index+=1
            continue

        if abs(graph[i][index]-graph[i][index+1])!=1:
            break
        #up
        if graph[i][index]==graph[i][index+1]-1:
            count=0
            for h in range(index,-1,-1):
                if count==l:
                    break
                if graph[i][h]!=graph[i][index+1]-1:
                    break
                if h in block:
                    break
                count+=1
            if count!=l:
                break
            for h in range(l):
                block.append(index-h)
            index+=1

        #down
        elif graph[i][index]==graph[i][index+1]+1:
            count=0
            for h in range(index+1,n):
                if count==l:
                    break
                if graph[i][h]!=graph[i][index]-1:
                    break
                count+=1
            if count!=l:
                break
            for h in range(l):
                block.append(index+h+1)
            index+=l

    index=0
    block=[]
    while True:
        if index>=n-1:
            result+=1
            break

        if graph[index][i]==graph[index+1][i]:
            index+=1
            continue

        if abs(graph[index][i]-graph[index+1][i])!=1:
            break
        #up
        if graph[index][i]==graph[index+1][i]-1:
            count=0
            for h in range(index,-1,-1):
                if count==l:
                    break
                if graph[h][i]!=graph[index+1][i]-1:
                    break
                if h in block:
                    break
                count+=1
            if count!=l:
                break

            for h in range(l):
                block.append(index-h)
            index+=1
        #down
        elif graph[index][i]==graph[index+1][i]+1:
            count=0
            for h in range(index+1,n):
                if count==l:
                    break
                if graph[h][i]!=graph[index][i]-1:
                    break
                count+=1
            if count!=l:
                break

            for h in range(l):
                block.append(index+h+1)
            index+=l
print(result)