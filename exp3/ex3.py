import random
from plotConvexHull import *


def read_file(path,mode):
    with open(path,mode=mode,encoding='utf-8') as file:
        lines=file.readlines()
        table=dict()
        key=0
        for item in lines:
            temp=list(map(int,item.strip('\n').split(' ')))
            if len(temp)==1:
                key=temp[0]
                table[key]=[]
            else:
                table[key].append(temp)
        
        for key,val in table.items():
            table[key]=np.array(val)
            # 检查是否读入错误
            assert len(val)==key
        
    return table

def output_file(path,mode):
    with open(path,mode=mode,encoding='utf-8') as file:
        lines=file.readlines()
        for item in lines:
            temp=item.strip('\n')
            print(temp)





class Sol(object):
    @staticmethod
    def ConvexHull(points):
        # 比较方法
        def method(p):
            vec1=np.array([1,0])
            vec2=np.array([p[0]-start[0],p[1]-start[1]])
            return vec1.dot(vec2)/(np.linalg.norm(vec2))
        # 通过外积来判断是否是逆时针方向
        def ccw(x,y,z): 
            vec1,vec2=y-x,z-y
            return np.cross(vec1,vec2)

        # 寻找起始点 O(n)
        index=np.argmin(points[:,1])
        start=points[index,:]
        points=np.delete(points,index,axis=0) # 删除起始节点
        # 对点集按照角度排序
        points=np.array(sorted(points,key=method,reverse=True))
        points=np.concatenate((start.reshape(1,2),points))

        # 创建栈 初始化
        stack=[]
        # 做cross product 来判断 方向
        for i in range(len(points)):
            while len(stack)>1 and ccw(stack[-2],stack[-1],points[i,:]) <0:
                stack.pop()
            stack.append(points[i,:])
        
        return np.array(stack)

    @staticmethod
    def ConvexHull_dynamic(points):
        # 排序的比较方法
        def method(p):
            vec1=np.array([1,0])
            vec2=np.array([p[0]-start[0],p[1]-start[1]])
            # 返回的是cos值
            return vec1.dot(vec2)/(np.linalg.norm(vec2))
        # 通过外积来判断是否是逆时针方向
        def ccw(x,y,z): 
            vec1,vec2=y-x,z-y
            return np.cross(vec1,vec2)

        # 寻找起始点 O(n)
        index=np.argmin(points[:,1])
        start=points[index,:]
        points=np.delete(points,index,axis=0) # 删除起始节点
        # 对点集按照角度排序
        points=np.array(sorted(points,key=method,reverse=True)) # cos 值单调递减
        points=np.concatenate((start.reshape(1,2),points))
        # 交互图像
        plt.ion()
        # 创建栈 初始化
        stack=[]
        # 做cross product 来判断 方向
        for i in range(len(points)):
            while len(stack)>1 and ccw(stack[-2],stack[-1],points[i,:]) <=0:
                stack.pop()
                plot_process(points,np.array(stack))
            stack.append(points[i,:])
            plot_process(points,np.array(stack))
                    
        plot_result(points,np.array(stack))
        plt.pause(10)



if __name__=='__main__':
    # 随机生成点集
    # num=50
    # points=np.random.uniform(low=0.0,high=10.0,size=(num,2))
    # ans=np.array(Sol.ConvexHull(points))
    # print(ans)
    # # 绘制原始图像
    # plot_result(points,ans)
    table=read_file('./exp3(2)_in.txt','r')
    for key,val in table.items():
        Sol.ConvexHull(val)
    output_file('./exp3(2)_out.txt','r')
    Sol.ConvexHull_dynamic(table[50])

