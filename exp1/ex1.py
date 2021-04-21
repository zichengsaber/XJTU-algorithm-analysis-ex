from function import *

def sortedMethod(x,table):
    # 排序
    temp=quicksort(x)
    cumprob=0.0
    for item in temp:
        cumprob+=table[item]
        if cumprob>0.5:
            return (item,table[item])

class solution(object):
    def __init__(self):
        self.fun=LinearSelection()

    def partition(self,x,p):
        L=[item for item in x if item<p]
        R=[item for item in x if item>p]
        return L,R
    def weightedMedian(self,x,table):
        # 递归的base
        if len(x)==1:
            return x[0]
        if len(x)==2:
            if table[x[0]]==table[x[1]]:
                return (x[0]+x[1])/2
            elif table[x[0]]>table[x[1]]:
                return x[0]
            else:
                return x[1]
        p=self.fun.select(x,math.ceil(len(x)/2))
        # print("中位数{}".format(p))
        # print("长度{}".format(len(x)))
        L,R=self.partition(x,p)

        # print(L)
        # print(R)
        wl,wr=0.0,0.0 
    
        for i in range(len(L)):
            wl+=table[L[i]]
        for i in range(len(R)):
            wr+=table[R[i]]
        
        if wl<0.5 and wr<0.5:
            return p
        else:
            if wl>wr:
                table[p]+=wr
                x_hat=[item for item in x if item<=p]
                return self.weightedMedian(x_hat,table.copy())
            else:
                table[p]+=wl
                x_hat=[item for item in x if item>=p]
                return self.weightedMedian(x_hat,table.copy())
                



if __name__=='__main__':
    # 制造随机数据
    x1=[random.randint(0,1000) for i in range(10)]
    w1=np.squeeze(np.random.dirichlet(np.ones(len(x1)),size=1)).tolist()
    table1={}
    lst1=list(zip(x1,w1))
    sol=solution()
    for i in range(len(x1)):
        table1[x1[i]]=w1[i]
    print("随机生成数组")
    print(sorted(lst1,key=lambda x: x[0]))
    print("brute-force:{}".format(sortedMethod(x1,table1)))  
    value=sol.weightedMedian(x1,table1)
    print("O(n) select:{}".format((value,table1[value])))  
    
    
