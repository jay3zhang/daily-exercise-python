# coding=utf-8
from pythonds.basic.queue import Queue
import random

# 平均每天大约10名学生在任何给定时间在实验室工作。这些学生通常在此期间打印两次，
# 这些任务的长度范围从1到20页。实验室中的打印机较旧，每分钟以草稿质量可以处理10页。
# 打印机可以切换以提供更好的质量，但是它将每分钟只能处理五页。较慢的打印速度可能会使学生等待太久。

# 打印机的类
class Printer:
    def __init__(self,printrate):
        self.printrate = printrate  #打印机的速率，一秒钟打印几页
        self.nowTask = None     #打印机当前任务
        self.timeDelay = 0  #打印机时延(学生等待时间)
        
    def tick(self):     #打印中
        if self.nowTask != None:
            self.timeDelay = self.timeDelay -1  #任务用时-1
            if self.timeDelay <= 0:
                self.nowTask = None
                
    def isBusy(self):
        return self.nowTask != None
        
    def start_nextTask(self,newtask):     #从队列中取得下一个任务
        self.nowTask = newtask
        self.timeDelay = newtask.pagenum*60/self.printrate   #计算该任务的用时
            
# 任务的类  
class Task:
    def __init__(self,timeclock):
        self.pagenum = random.randrange(1,21)
        self.timetamp = timeclock
        
    def waitTime(self,currenttime):     # 用取出任务的时间-创建任务的时间
        return currenttime - self.timetamp
     
# printQueue类-> printQueue=Queue()

# 整个过程的模拟
def simulation(numSeconds, printBetter=True,argslist=[10,2]):
    # numSeconds为模拟的时长(秒计数)，printBetter指定打印的质量
    # 以一个列表传入学生数和每个学生打印的次数

    pagesPerMinute = 5 if printBetter == True else 10
    # pagesPerMinute为打印机每分钟打印多少页
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []   #存放每个任务的等待时间

    for currentSecond in range(numSeconds):     # 每秒发生的事件
      
      #事件1：Task()类，是否有新任务
      if newPrintTask(argslist):    #每秒尝试创建一次任务
         task = Task(currentSecond)     #以当前时间创建任务
         printQueue.enqueue(task)   # 加入任务队列

      # 事件2：PrintQueue()类，是否进行下一个任务
      if (not labprinter.isBusy()) and (not printQueue.isEmpty()):    #打印机空闲且队列中有任务
        nexttask = printQueue.dequeue()     #取新任务
        waitingtimes.append(nexttask.waitTime(currentSecond))   #计算该任务的等待时间
        labprinter.start_nextTask(nexttask)     #开始新任务
       
      # Print()类，打印任务，该任务用时-1
      labprinter.tick()     #每秒打印一下

    averageWait=sum(waitingtimes)/len(waitingtimes)     #计算平均等待时间
    # 输出平均等待时间，剩余任务数量
    print("Average Wait %6.2f secs，%3d tasks remaining，%d tasks print."%(averageWait,printQueue.size(),len(waitingtimes)))

def newPrintTask(argslist):
    # 如果实验室中有 10 个学生，每人打印两次，则平均每小时有 20 个打印任务。 
    # 在任何给定的秒，打印任务将被创建的机会是什么？ 
    # 回答这个问题的方法是考虑任务与时间的比率。
    # 每小时 20 个任务意味着平均每 180 秒将有一个任务：
    # 当随机数=180时，创建任务成功，平均180秒成功一次
    
    studentnum,perTasknum = argslist    #以一个列表传入学生数和每个学生打印的次数
    new_task_time = 3600/(studentnum*perTasknum)
    num = random.randrange(1,new_task_time+1)
    return num == new_task_time
    
for i in range(10):  
    simulation(3600,printBetter=False)