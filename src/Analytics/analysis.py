import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def graph_plot(df,ax,title):
    splits1 = list(df.groupby("WorkerID"))
    for i in range(len(splits1)):
        time={}
        a=pd.DataFrame(splits1[i][1],columns=['JobId','WorkerID','TaskId','start_time','end_time','duration'])
        end_time= a["end_time"].iloc[-1]
        for m in range(0,end_time):
            count=0
            for n in range(len(a["TaskId"])):
                if m >= a["start_time"].iloc[n] and m <= a["end_time"].iloc[n]:
                    count=count+1    
                else:
                    pass
            time[m] = count
        l = "Worker" + ":"+str(splits1[i][0])
        x = list(time.keys())
        y = list(time.values())
        ax.set_xlabel('Time')
        ax.set_ylabel('Number of tasks')
        ax.plot(x,y,marker="o",label=l)
        ax.set_title(title)
        ax.legend()


def get_analytics():
    fig, (ax1, ax2 , ax3) = plt.subplots(3,figsize=(15,25))
    fig.tight_layout(pad=10.0)
    mean_salgo1_task = 0
    mean_salgo2_task = 0
    mean_salgo3_task = 0
    mean_salgo1_job = 0
    mean_salgo2_job = 0
    mean_salgo3_job = 0
    
    if os.path.exists('Round-Robin'):
        algo='Round-Robin'
        job1 = pd.read_csv(os.path.join(algo,'jobs.csv'))
        task1 = pd.read_csv(os.path.join(algo,'tasks.csv'))
        worker1 = pd.read_csv(os.path.join(algo,'workers.csv'))
        
        df1_w1 = pd.DataFrame(worker1)
        df1_j1 = pd.DataFrame(job1)
        df1_t1 = pd.DataFrame(task1)
        
        mean_salgo1_task = df1_t1["duration"].mean()
        mean_salgo1_job = df1_j1["duration"].mean()
        median_salgo1_task = df1_t1["duration"].median()
        median_salgo1_job = df1_j1["duration"].median()

        graph_plot(df1_w1 , ax1 ,'Round Robin Scheduling')
    
    else:
        pass

    if os.path.exists('Least-Loaded'):
        algo='Least-Loaded'
        job2 = pd.read_csv(os.path.join(algo,'jobs.csv'))
        task2 = pd.read_csv(os.path.join(algo,'tasks.csv'))
        worker2 = pd.read_csv(os.path.join(algo,'workers.csv'))
        
        df1_w2 = pd.DataFrame(worker2)
        df1_j2 = pd.DataFrame(job2)
        df1_t2 = pd.DataFrame(task2)
        
        mean_salgo2_task = df1_t2["duration"].mean()
        mean_salgo2_job = df1_j2["duration"].mean()
        median_salgo2_task = df1_t2["duration"].median()
        median_salgo2_job = df1_j2["duration"].median()
        
        graph_plot(df1_w2 , ax2 ,'Least Loaded Scheduling')
    
    else:
        pass
        
        
    if os.path.exists('Random'):
        algo='Random'
        job3 = pd.read_csv(os.path.join(algo,'jobs.csv'))
        task3 = pd.read_csv(os.path.join(algo,'tasks.csv'))
        worker3 = pd.read_csv(os.path.join(algo,'workers.csv'))
        
        df1_w3 = pd.DataFrame(worker3)
        df1_j3 = pd.DataFrame(job3)
        df1_t3 = pd.DataFrame(task3)
        
        mean_salgo3_task = df1_t3["duration"].mean()
        mean_salgo3_job = df1_j3["duration"].mean()
        median_salgo3_task = df1_t3["duration"].median()
        median_salgo3_job = df1_j3["duration"].median()
        
        graph_plot(df1_w3 , ax3 ,'Random Scheduling')
    
    else :
        pass
 
    
    if os.path.exists('Round-Robin'):
        print("\nRound-Robin Scheduling Algorithm")
        print(f"Mean of task completion time : {mean_salgo1_task}")
        print(f"Mean of job completion time : {mean_salgo1_job}")
        print(f"Median of task completion time : {median_salgo1_task}")
        print(f"Median of job completion time : {median_salgo1_job}\n")  
    else:
        pass
        
    if os.path.exists('Least-Loaded'):
        print("\nLeast-Loaded Scheduling Algorithm")
        print(f"Mean of task completion time : {mean_salgo2_task}")
        print(f"Mean of job completion time : {mean_salgo2_job}")
        print(f"Median of task completion time : {median_salgo2_task}")
        print(f"Median of job completion time : {median_salgo2_job}\n")
    else:
        pass
        
    if os.path.exists('Random'):
        print("\nRandom Scheduling Algorithm")
        print(f"Mean of task completion time : {mean_salgo3_task}")
        print(f"Mean of job completion time : {mean_salgo3_job}")
        print(f"Median of task completion time : {median_salgo3_task}")
        print(f"Median of job completion time : {median_salgo3_job}\n")    
    else:
        pass
    
    ''' Plotting bar graph to compare mean times of scheduling algorithms'''
    barWidth = 0.25
    fig = plt.figure(figsize = (10, 5))
    x1 = []
    y1 = []
    y2 = []
    y1.append(mean_salgo1_task)
    y1.append(mean_salgo2_task)
    y1.append(mean_salgo3_task)
    
    y2.append(mean_salgo1_job)
    y2.append(mean_salgo2_job)
    y2.append(mean_salgo3_job)
    
    x1.append('Round Robin Scheduling')
    x1.append('Least Loaded Scheduling')
    x1.append('Random Scheduling')
    
    br1 = np.arange(len(x1)) 
    br2 = [x + barWidth for x in br1] 
    plt.bar(br1,y1, color ='r', width = barWidth,edgecolor ='grey', label ='Tasks') 
    plt.bar(br2, y2, color ='g', width = barWidth,edgecolor ='grey', label ='Jobs') 
    plt.xlabel('Scheduling algorithms')
    plt.ylabel('Average task and job completion time')
    plt.xticks([r + barWidth for r in range(len(x1))],x1)
    plt.legend()
    
    ''' Plotting bar graph to compare median times of scheduling algorithms'''
    barWidth = 0.25
    fig2 = plt.figure(figsize = (10, 5))
    x1 = []
    y1 = []
    y2 = []
    y1.append(median_salgo1_task)
    y1.append(median_salgo2_task)
    y1.append(median_salgo3_task)
    
    y2.append(median_salgo1_job)
    y2.append(median_salgo2_job)
    y2.append(median_salgo3_job)
    
    x1.append('Round Robin Scheduling')
    x1.append('Least Loaded Scheduling')
    x1.append('Random Scheduling')
    
    br1 = np.arange(len(x1)) 
    br2 = [x + barWidth for x in br1] 
    plt.bar(br1,y1, color ='r', width = barWidth,edgecolor ='grey', label ='Tasks') 
    plt.bar(br2, y2, color ='g', width = barWidth,edgecolor ='grey', label ='Jobs') 
    plt.xlabel('Scheduling algorithms')
    plt.ylabel('Median task and job completion time')
    plt.xticks([r + barWidth for r in range(len(x1))],x1)
    plt.legend()

def main():
    get_analytics()
if __name__ == '__main__':
    main()
        
    
    
