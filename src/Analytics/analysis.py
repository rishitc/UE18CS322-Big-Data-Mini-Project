import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def graph_plot(df, ax, title):
    """
    * This function takes in the *workers.csv* for each algorithm separately and groups by worker id.
    * For each worker, the number of tasks running at each secong in a time interval are calculated.
    * There are 3 plots displayed in a window, with a plot each for a scheduling algorithm. The X axis 
    * has the number of tasks and the Y axis has the time in seconds.
    * For a given scheduling algorithm, each worker is represented with a line of a different colour.
    """
    splits1 = list(df.groupby("WorkerID"))
    for i in range(len(splits1)):
        time = dict()
        a = pd.DataFrame(splits1[i][1], columns=['JobId', 'WorkerID', 'TaskId', 'start_time', 'end_time', 'duration'])
        end_time = a["end_time"].iloc[-1]
        for m in range(0, end_time):
            count = 0
            for n in range(len(a["TaskId"])):
                if m >= a["start_time"].iloc[n] and m <= a["end_time"].iloc[n]:
                    count = count + 1
                else:
                    pass
            time[m] = count
        label = "Worker" + ":"+str(splits1[i][0])
        x = list(time.keys())
        y = list(time.values())
        ax.set_xlabel('Time')
        ax.set_ylabel('Number of tasks')
        ax.plot(x, y, marker="o", label=label)
        ax.set_title(title)
        ax.legend()


def get_analytics():
    """
    * This function reads all the log files generated for each scheduling algorithm.
    * The objective of this function is to calculate the mean task completion time, mean job completion time,
    median task completion time, median job completion time for each of the scheduling algorithms separately.
    * Various bar plots are plotted comparing the mean and median times of the various scheduling algortihms.
    * This function also calls the graph_plot function for each of the scheduling algorithms that plots the number
    of tasks scheduled on each worker at each instance of time.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(15, 25))
    fig.tight_layout(pad=10.0)
    mean_salgo1_task = 0
    mean_salgo2_task = 0
    mean_salgo3_task = 0
    mean_salgo1_job = 0
    mean_salgo2_job = 0
    mean_salgo3_job = 0
    median_salgo1_task = 0 
    median_salgo2_task = 0
    median_salgo3_task = 0 
    median_salgo1_job = 0
    median_salgo2_job = 0
    median_salgo3_job = 0
    '''
    Checking if the log files for Round Robin Algorithm exist.
    If they exist perform the necessary statistical computation and plot the graphs to draw inferences.
    '''
    if os.path.exists('Round-Robin'):
        algo = 'Round-Robin'
        job1 = pd.read_csv(os.path.join(algo, 'jobs.csv'))
        task1 = pd.read_csv(os.path.join(algo, 'tasks.csv'))
        worker1 = pd.read_csv(os.path.join(algo, 'workers.csv'))

        df1_w1 = pd.DataFrame(worker1)
        df1_j1 = pd.DataFrame(job1)
        df1_t1 = pd.DataFrame(task1)

        mean_salgo1_task = df1_t1["duration"].mean()
        mean_salgo1_job = df1_j1["duration"].mean()
        median_salgo1_task = df1_t1["duration"].median()
        median_salgo1_job = df1_j1["duration"].median()

        graph_plot(df1_w1, ax1, 'Round Robin Scheduling')

    else:
        pass
    
    '''
    Checking if the log files for Least Loaded Algorithm exist.
    If they exist perform the necessary statistical computation and plot the graphs to draw inferences.
    '''
    if os.path.exists('Least-Loaded'):
        algo = 'Least-Loaded'
        job2 = pd.read_csv(os.path.join(algo, 'jobs.csv'))
        task2 = pd.read_csv(os.path.join(algo, 'tasks.csv'))
        worker2 = pd.read_csv(os.path.join(algo, 'workers.csv'))

        df1_w2 = pd.DataFrame(worker2)
        df1_j2 = pd.DataFrame(job2)
        df1_t2 = pd.DataFrame(task2)

        mean_salgo2_task = df1_t2["duration"].mean()
        mean_salgo2_job = df1_j2["duration"].mean()
        median_salgo2_task = df1_t2["duration"].median()
        median_salgo2_job = df1_j2["duration"].median()

        graph_plot(df1_w2, ax2, 'Least Loaded Scheduling')

    else:
        pass

    '''
    Checking if the log files for Random Algorithm exist.
    If they exist perform the necessary statistical computation and plot the graphs to draw inferences.
    '''
    if os.path.exists('Random'):
        algo = 'Random'
        job3 = pd.read_csv(os.path.join(algo, 'jobs.csv'))
        task3 = pd.read_csv(os.path.join(algo, 'tasks.csv'))
        worker3 = pd.read_csv(os.path.join(algo, 'workers.csv'))

        df1_w3 = pd.DataFrame(worker3)
        df1_j3 = pd.DataFrame(job3)
        df1_t3 = pd.DataFrame(task3)

        mean_salgo3_task = df1_t3["duration"].mean()
        mean_salgo3_job = df1_j3["duration"].mean()
        median_salgo3_task = df1_t3["duration"].median()
        median_salgo3_job = df1_j3["duration"].median()

        graph_plot(df1_w3, ax3, 'Random Scheduling')

    else:
        pass

    '''
    The 3 blocks of code given below display the computed mean and median
    values for each algorithm(if that algorithm was used) in a neat readable 
    format which can be used to easily read the data plotted in a graph format.
    '''
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
    fig = plt.figure(figsize=(10, 5))
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
    plt.bar(br1, y1, color='r', width=barWidth, edgecolor='grey', label='Tasks') 
    plt.bar(br2, y2, color='g', width=barWidth, edgecolor='grey', label='Jobs') 
    plt.xlabel('Scheduling algorithms')
    plt.ylabel('Average task and job completion time')
    plt.xticks([r + barWidth for r in range(len(x1))], x1)
    plt.legend()

    ''' Plotting bar graph to compare median times of scheduling algorithms'''
    barWidth = 0.25
    fig2 = plt.figure(figsize=(10, 5))
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
    plt.bar(br1, y1, color='r', width=barWidth, edgecolor='grey', label='Tasks') 
    plt.bar(br2, y2, color='g', width=barWidth, edgecolor='grey', label='Jobs') 
    plt.xlabel('Scheduling algorithms')
    plt.ylabel('Median task and job completion time')
    plt.xticks([r + barWidth for r in range(len(x1))], x1)
    plt.legend()


def main():
    get_analytics()


if __name__ == '__main__':
    main()
