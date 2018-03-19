class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid=pid
        self.arrival_time=arrival_time
        self.burst_time=burst_time

gant_chart= []

def SJF(process_list, n, preemptive):
    global gant_chart
    queue=[]
    time=0
    arrived_process=0
    ready_to_exe_process= 0
    done= 0 

    if not preemptive:
        while(done<n):
            for i in range(arrived_process,n):
                if time >=process_list[i].arrival_time:
                    queue.append(process_list[i])
                    arrived_process+=1
                    ready_to_exe_process+=1
            if ready_to_exe_process<1:
                time+=1
                gant_chart.append(0)
                continue

            queue.sort(key=lambda x: (x.burst_time, x.arrival_time))

            if queue[0].burst_time>0:
                for i in range(queue[0].burst_time):
                    gant_chart.append(queue[0].pid)
                time+=queue[0].burst_time
                queue[0].burst_time=99999999
                don+=1
                ready_to_exe_process-=1

    else:
        while(done<n):
            for i in range(arrived_process,n):
                if time >=process_list[i].arrival_time:
                    queue.append(process_list[i])
                    arrived_process+=1
                    ready_to_exe_process+=1
            if ready_to_exe_process<1:
                time+=1
                gant_chart.append(0)
                continue

            queue.sort(key=lambda x: (x.burst_time, x.arrival_time))

            if queue[0].burst_time>0:
                gant_chart.append(queue[0].pid)
                time+=1
                queue[0].burst_time-=1
                if queue[0].burst_time<1:
                   queue[0].burst_time=9999999
                   done+=1
                   ready_to_exe_process-=1

process_list=[]
process_list.append(Process(1,0,7))
process_list.append(Process(2,2,4))
process_list.append(Process(3,4,1))
process_list.append(Process(4,5,4))

SJF(process_list, len(process_list), 1)
print (gant_chart)



                
