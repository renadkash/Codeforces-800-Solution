"""""
4A-watermelon
Difficulty:800
link:https://codeforces.com/problemset/problem/4/A
"""""
#Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos;
#and NO in the opposite case

w = int (input())
if(w>2 and w%2==0):
    print("YES")
else:
    print("NO")