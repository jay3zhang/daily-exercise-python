
from pythonds.basic.queue import Queue

def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:   #玩游戏的人全部入队列
        simqueue.enqueue(name)
        
    while simqueue.size()>1:
        for i in range(0,num-1):    
            # num大于队列的长度。这不是一个问题，
            # 因为队列像一个圈，计数会重新回到开始，直到达到计数值。
            simqueue.enqueue(simqueue.dequeue())
        # 数到num的人出局
        print(simqueue.dequeue())  #每次出局的人
        
    return simqueue.dequeue()   # 返回最后剩下的人
    
print(hotPotato(["1Bill","2David","3Susan","4Jane","5Kent","6Brad"],7))