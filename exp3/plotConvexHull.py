import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import time
sns.set_style("white")


def plot_result(points,ans):
    plt.plot(points[:,0],points[:,1],'o')
    start=ans[0]
    plt.pause(0.3)
    for i in range(len(ans)):
        if i==len(ans)-1:
            plt.plot([ans[i,0],start[0]],[ans[i,1],start[1]],color='red',alpha=0.8,lineWidth=2)
        else:
            plt.plot([ans[i,0],ans[i+1,0]],[ans[i,1],ans[i+1,1]],color='red',alpha=0.8,lineWidth=2)
    plt.show()

def plot_process(points,ans):
    plt.plot(points[:,0],points[:,1],'o')
    start=ans[0]
    for i in range(len(ans)):
        if i==len(ans)-1:
            break
        else:
            plt.plot([ans[i,0],ans[i+1,0]],[ans[i,1],ans[i+1,1]],color='red',alpha=0.8,lineWidth=2)
    plt.pause(0.3)
    plt.cla()
   
   

