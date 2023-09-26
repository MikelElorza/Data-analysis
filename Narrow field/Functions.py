import numpy as np

def readZoraidasCSV(filename):
    counts=np.array([])
    time=np.array([])
    file=open(filename)
    line=file.readline()
    while line!='\n':
        line=file.readline()
    for line in file.readlines():
        t,c=line.split(',')[0:2]
        time=np.append(time,float(t))
        counts=np.append(counts,float(c))
    return time,counts
def cumulative(counts):
    cumul=np.array([])
    for i,c in enumerate(counts):
        s=np.sum(counts[i:])
        cumul=np.append(cumul,s)
    return cumul  
def binned(times,t_res, t0, tf):
        edges=np.arange(t0,tf,t_res)
        return np.histogram(times,edges)
def edges2bins(edges):
    return edges[:-1]+np.diff(edges)/2
def cumulative2D(counts):
    size=np.size(counts)
    cumul2D=np.zeros((size,size))
    cumul2D[0]=cumulative(counts)
    for i in range(1,size):
        cumul2D[i]=np.append(cumulative(counts[:-i]),np.zeros(i))
    cumul2D[cumul2D==0]=np.nan
    return cumul2D