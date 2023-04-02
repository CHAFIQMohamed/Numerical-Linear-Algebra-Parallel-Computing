from mpi4py import MPI

COMM =MPI.COMM_WORLD
SIZE =COMM.Get_size()
RANK =COMM.Get_rank()
"""
if RANK==0:
    sendbuf=int(input("write an integer "))
    COMM.send(sendbuf, dest=1)
else:
    sendbuf=None
    for i in range(1,SIZE):
        if RANK==i:
            recvbuf = COMM.recv(source=i-1)
            if i!=SIZE-1:
                sendbuf=recvbuf + i
                COMM.send(sendbuf, dest=i+1)
            print("I, process",i, "I received ",recvbuf," from the process",i-1)
        

"""
while(1):
    if RANK == 0:
        x = int(input())
        comm_world.send(x,1)
    else:
        x = co
 