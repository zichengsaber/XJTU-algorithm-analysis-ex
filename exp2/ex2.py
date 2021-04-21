import numpy as np
# 读取文件
def readfile(path,mode):
    table={
        'write':'w',
        'read':'r'
    }
    with open(path,table[mode],encoding='utf-8') as file:
        lines=file.readlines()
        test_data=[]
        for i in range(0,len(lines),2):
            L,n=list(map(int,lines[i].strip('\n').split(' ')))
            segment=sorted(list(map(int,lines[i+1].strip('\n').split(' '))))
            test_data.append(Data(L,n,segment))
        return test_data

class Data(object):
    def __init__(self,L,n,segment):
        self.L=L
        self.n=n
        self.segment=segment

# 测试结果的正确性
# 
def check_correctness(ans):
    corret_ans=[]
    with open('./exp2_out.txt','r',encoding='utf-8') as file:
        for item in file.readlines():
            corret_ans.append(int(item.strip('\n')))
    print('Reference answer:',corret_ans)
    print('my answer:',ans)
    ans,corret_ans=np.array(ans),np.array(corret_ans)
    print((ans-corret_ans).any()==0)
    




class solution(object):
    """ 
    dp[i][j]代表从第i个断点到第j个断点的最优代价
    p[i] 表是第i个断点的位置
    递推关系
    dp[i][j]=0 if i==j
    dp[i][j]=min{dp[i][k]+dp[k][j]+p[j]-p[i]}
    最优解:dp[0][n+1]
    边界条件
    dp
     """
    def __init__(self,n,L,p):
        self.s=[[0]*(n+2) for i in range(n+2)]
        self.n=n
        self.L=L
        self.p=p
    def segmentation(self):
        n=self.n
        L=self.L
        p=self.p
        # 补全p数组
        p.append(L)
        p.insert(0,0)
        size=n+2
        # 初始化
        # dp[i][i]=0
        dp=[[0]*size for i in range(size)]
        for gap in range(2,size):
            for i in range(0,size-gap):
                j=i+gap
                temp=float("inf")
                for k in range(i+1,j):
                    if temp>dp[i][k]+dp[k][j]+p[j]-p[i]:
                        temp=dp[i][k]+dp[k][j]+p[j]-p[i]
                        self.s[i][j]=k 
                dp[i][j]=temp
        return dp[0][n+1]
        
    def traceback(self,i,j):
        if (j-i==1):
            return
        print("{}~{}在{}分割".format(i,j,self.s[i][j]))
        self.traceback(i,self.s[i][j])
        self.traceback(self.s[i][j],j)
        



if __name__=='__main__':
    '''
    n,L=4,7
    p=[1,3,4,5]
    sol=solution(n,L,p)
    print("The number of segment:{}".format(n))
    print("Total Length:{}".format(L))
    print("Breaking point:{}".format(p))

    ans=sol.segmentation()
    print("Total Cost:{}".format(ans))
    sol.traceback(0,n+1)
    '''
    Dataset=readfile('./exp2_in.txt','read')
    ans=[]
    for item in Dataset:
        n,L,segment=item.n,item.L,item.segment
        sol=solution(n,L,segment)
        ans.append(sol.segmentation())
    
    check_correctness(ans)
    
