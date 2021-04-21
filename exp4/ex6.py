import numpy as np 
import time 

# 读入元素
def read_data(PATH,mode):
    with open(PATH,mode=mode,encoding='utf-8') as file:
        lines=file.readlines()
        mat=[]
        cnt=0
        for item in lines:
            if cnt==0:
                cnt+=1
                continue
            row=list(map(int,item.strip('\n').split(' ')))
            mat.append(row)
    return np.array(mat)

def check():
    with open("./exp6_out.txt",'r') as file:
        lines=file.readlines()
        for item in lines:
            item=list(map(int,item.strip('\n').split(' ')))
            print(item)
        
class Sol(object):
    @staticmethod
    def solver(mat):
        # A,B 矩阵
        A,B=np.zeros((1000,20)),np.zeros((1000,20))
        recordA,recordB=[],[]
        lenA,lenB=0,0
        bestlen=0
        bestA,bestB=[],[] # 最优索引
        sub=20
        sumA=1000
        Length=0

        def check(X,Y,col,lenX,lenY): 
            x=X.copy()
            x[:,lenX]=col # lenx=lenX+1 # 将col加入X
            sumX=np.sum(x[:,:lenX+1],axis=1)
            sumY=np.sum(Y[:,:lenY],axis=1)
            # 检查加入后的X和Y是否互斥
            for i in range(1000):
                if sumX[i]>0 and sumY[i]>0 :
                    return False
            return True


        def backtrace(level):
            nonlocal A,B,lenA,lenB,recordA,recordB,bestlen,bestA,bestB,sub,Length,sumA
            if (level>19): # 
                if lenA>0 and lenB>0: # A 和 B集合不为空
                    if (lenA+lenB>bestlen): # 超出历史最优
                        bestlen=lenA+lenB
                        bestA=recordA.copy()
                        bestB=recordB.copy()
                        return
                    if (lenA+lenB==bestlen): # 并列历史最优
                        if (abs(lenA-lenB)<sub  and lenA>=lenB): # A和B的个数差的绝对值最小
                            sub=abs(lenA-lenB)
                            sumA=np.sum(recordA)
                            Length=lenA
                            bestlen=lenA+lenB
                            bestA=recordA.copy()
                            bestB=recordB.copy()
                            return
                    
                        if (abs(lenA-lenB)==sub and lenA>Length):# A的长度最大
                            Length=lenA
                            sumA=np.sum(recordA)
                            bestlen=lenA+lenB
                            bestA=recordA.copy()
                            bestB=recordB.copy()
                            return
                        if (np.sum(recordA)<sumA and abs(lenA-lenB)==sub and lenA==Length): #A的和最小
                            sumA=np.sum(recordA)
                            bestlen=lenB+lenA
                            bestA=recordA.copy()
                            bestB=recordB.copy()
                            return
                return
            else:
                col=mat[:,level]
                if (check(A,B,col,lenA,lenB)): # 尝试将A加入
                    A[:,lenA]=col
                    lenA+=1
                    recordA.append(level)
                    backtrace(level+1)
                    recordA.pop()
                    lenA-=1
                if (check(B,A,col,lenB,lenA)): # 尝试将B加入
                    B[:,lenB]=col
                    lenB+=1
                    recordB.append(level)
                    backtrace(level+1)
                    recordB.pop()
                    lenB-=1
                # 该列不进入A也不进入B
                if (lenA+lenB+19-level>bestlen):
                    backtrace(level+1)
            
        backtrace(0)
        print(bestlen)
        print(bestA)
        print(bestB)
        return 
       
                
                






if __name__=='__main__':
    mat=read_data('./exp6_in.txt','r')
    for i in range(0,9):
        Sol.solver(mat[i*1000:(i+1)*1000,:])
    print(0)
    print([])
    print([])
    

   
    

    
