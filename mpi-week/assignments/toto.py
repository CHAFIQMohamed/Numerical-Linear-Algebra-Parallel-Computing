from mpi4py import MPI 
import numpy as np

COMM  = MPI.COMM_WORLD
RANK = COMM.Get_rank()
SIZE = COMM.Get_size()

"""
buffer = int(input("give a value to distribute : "))
while buffer>0:
    print("process",RANK, "got" ,buffer)
"""

while True:
    if RANK == 0:
        data = int(input("enter a value "))
        print('Process {} broadcast data:'.format(RANK), data)
    else:
        data = None

    data = COMM.bcast(data, root=0)
    if data<0:
        break


        
    
    print('Process {} received data:'.format(RANK), data)
