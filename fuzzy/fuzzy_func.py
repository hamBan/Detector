import numpy as np

def fuzzy(arr):
    n,m=arr.shape
    N=n*m
    etnmax=0
    ent=0
    c=0
    i2=(np.reshape(arr,(1,-1)))
    L=np.max(i2)
    unique_elements, counts_elements = np.unique(i2, return_counts=True)
    n1=unique_elements.shape[0]
    entr=[]
    for t in range(n1):
        psa=counts_elements[:t]
        tempa=unique_elements[:t]
        ea=np.dot(psa,tempa)
        psb=counts_elements[t+1:]
        tempb=unique_elements[t+1:]
        eb=np.dot(psb,tempb)
        u0=(ea/sum(psa))
        u1=(eb/sum(psb))
        v1=(np.dot(psa,abs(tempa-u0)/L))
        v2=(np.dot(psb,abs(tempb-u1)/L))
        ent=N-v1-v2
    if ent>etnmax:
        etnmax=ent
        c=t
    final_array=i2>=c
    array=np.extract(final_array,i2)
    size=array.shape[0]
    return size/N