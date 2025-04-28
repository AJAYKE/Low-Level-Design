# [Operating Systems Interview Preparation Guide](https://whimsical.com/operating-system-cheatsheet-5Xv9MsZqsrtQwG4wwyEohq)

## Table of Contents
1. [Overview of Operating Systems](#overview-of-operating-systems)
2. [Process Concepts](#process-concepts)
3. [Process Scheduling](#process-scheduling)
4. [Thread Concepts](#thread-concepts)
5. [Synchronization](#synchronization)
6. [Deadlocks](#deadlocks)
7. [Memory Management Strategies](#memory-management-strategies)
8. [Virtual Memory Management](#virtual-memory-management)
9. [Storage Management](#storage-management)

## Overview of Operating Systems

### What is an Operating System?

An operating system (OS) is a software that acts as an intermediary between computer hardware and user applications. It manages computer hardware, software resources, and provides common services for computer programs.

### Services Provided by an Operating System

1. **Process Management**: Creates, schedules, and terminates processes
2. **Memory Management**: Allocates and deallocates memory space
3. **File System Management**: Creates, deletes, and provides access to files
4. **Device Management**: Manages devices through drivers
5. **I/O System Management**: Handles input/output operations
6. **Security and Protection**: Protects system resources from unauthorized access
7. **Networking**: Facilitates communication over networks
8. **Command Interpreter**: Provides an interface to interact with the OS

### Types of Operating Systems

#### Batch Operating Systems
- Processes jobs in batches without user interaction
- Examples: IBM's OS/360, early mainframe systems
- **Characteristics**:
  - Groups similar jobs
  - No direct interaction with users
  - Efficient for CPU-bound tasks

```c
// Batch processing pseudocode
while (batch_queue_not_empty) {
    job = get_next_job_from_queue();
    setup_job_environment(job);
    execute_job(job);
    cleanup_job_environment(job);
    record_job_statistics(job);
}
```

#### Time-Sharing Operating Systems
- Multiple users share computing resources simultaneously
- Examples: UNIX, early versions of Linux
- **Characteristics**:
  - Uses CPU scheduling and multiprogramming
  - Provides quick response time
  - Each user gets a small portion of CPU time

#### Distributed Operating Systems
- Manages a group of independent computers to appear as a single system
- Examples: Amoeba, Mach
- **Characteristics**:
  - Resource sharing across network
  - Load balancing
  - Increased reliability through redundancy

#### Network Operating Systems
- Manages server network resources and provides services to client computers
- Examples: Novell NetWare, Windows Server
- **Characteristics**:
  - Centralized servers
  - Shared applications and data
  - User management and security

#### Real-Time Operating Systems
- Designed for immediate response time guarantees
- Examples: VxWorks, QNX
- **Characteristics**:
  - Deterministic scheduling
  - Minimal latency
  - Used in embedded systems, industrial controls

```c
// Real-time task scheduling pseudocode
void schedule_tasks() {
    // Sort tasks by priority or deadline
    sort_tasks_by_priority();
    
    while (true) {
        task = get_highest_priority_task();
        if (task->deadline > current_time()) {
            execute_task(task);
        } else {
            handle_deadline_miss(task);
        }
        yield_cpu();
    }
}
```

### Hardware Fundamentals

#### RAM vs ROM

| Feature | RAM (Random Access Memory) | ROM (Read-Only Memory) |
|---------|----------------------------|------------------------|
| Volatility | Volatile (loses data when powered off) | Non-volatile (retains data when powered off) |
| Modifiability | Data can be modified | Data cannot be modified (or limited modification) |
| Speed | Faster | Slower |
| Usage | Temporary storage of programs and data | Permanent storage of firmware and bootstrap code |
| Types | SRAM, DRAM | PROM, EPROM, EEPROM |

#### SRAM vs DRAM

**SRAM (Static RAM)**:
- Retains data as long as power is supplied
- Faster but more expensive
- Uses flip-flops (6 transistors per bit)
- Used in cache memory

**DRAM (Dynamic RAM)**:
- Must be periodically refreshed
- Slower but less expensive
- Uses capacitors and transistors (1 transistor + 1 capacitor per bit)
- Used as main memory

#### PROM, EPROM & EEPROM

**PROM (Programmable ROM)**:
- Can be programmed once
- Uses fuses or anti-fuses

**EPROM (Erasable Programmable ROM)**:
- Can be erased using UV light
- Must be removed from circuit to erase

**EEPROM (Electrically Erasable Programmable ROM)**:
- Can be programmed and erased electrically
- Can be erased without removal
- Modern flash memory is a type of EEPROM

### Virtualization vs Containerization

#### Virtualization
- Creates multiple virtual machines on a single physical machine
- Each VM has its own OS kernel
- Higher isolation but more resource overhead
- Examples: VMware, VirtualBox, Hyper-V

```python
# Python code using libvirt to create a VM
import libvirt

conn = libvirt.open('qemu:///system')
xml_config = '''
<domain type='kvm'>
  <name>vm1</name>
  <memory unit='KiB'>2097152</memory>
  <vcpu placement='static'>2</vcpu>
  <os>
    <type arch='x86_64'>hvm</type>
    <boot dev='hd'/>
  </os>
  <!-- Additional configuration... -->
</domain>
'''
dom = conn.defineXML(xml_config)
dom.create()
```

#### Containerization
- Shares the host OS kernel but isolates application environments
- Lightweight and faster to start
- Less isolation but more efficient
- Examples: Docker, Kubernetes, LXC

```bash
# Docker example to create a container
docker run -d --name web-server -p 80:80 nginx
```

### System Boot Process: BIOS vs UEFI

#### BIOS (Basic Input/Output System)
- Legacy boot process
- 16-bit mode
- Limited to 2.2TB hard drives
- Uses MBR (Master Boot Record)

#### UEFI (Unified Extensible Firmware Interface)
- Modern replacement for BIOS
- 32-bit or 64-bit mode
- Supports drives larger than 2.2TB
- Uses GPT (GUID Partition Table)
- More secure with Secure Boot feature

### MBR vs GPT

#### MBR (Master Boot Record)
- Traditional partition scheme
- Limited to 4 primary partitions
- Maximum partition size of 2.2TB
- No redundancy for partition data

#### GPT (GUID Partition Table)
- Modern partition scheme
- Virtually unlimited number of partitions (typically 128)
- Maximum partition size of 18 exabytes
- Includes backup partition table for redundancy
- Uses CRC protection for partition data

### Important Terms in Operating Systems

#### Compiler
Software that translates high-level programming code to machine code for execution.

```bash
# Compiling a C program
gcc -o program program.c
```

#### Loader
Part of the OS that loads programs from executable files into memory for execution.

```c
// Simplified pseudo-code for a loader
void load_program(char *executable) {
    binary_file = open(executable);
    program_header = read_header(binary_file);
    
    // Allocate memory
    program_memory = allocate_memory(program_header.size);
    
    // Load segments
    for each segment in program_header.segments {
        load_segment(binary_file, segment, program_memory);
    }
    
    // Set up entry point
    jump_to(program_memory + program_header.entry_point);
}
```

#### Assembler
Converts assembly language into machine code.

```bash
# Assembling an assembly program
nasm -f elf64 program.asm -o program.o
```

#### Interpreter
Executes high-level language programs directly without prior compilation.

```python
# Python as an interpreter
# This line interprets and executes python_script.py
python python_script.py
```

#### System Calls
Interface for user programs to request services from the OS kernel.

```c
// Example of system calls in C
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd = open("file.txt", O_RDWR | O_CREAT, 0644); // open() system call
    if (fd != -1) {
        write(fd, "Hello, World!", 13); // write() system call
        close(fd); // close() system call
    }
    return 0;
}
```

#### API (Application Programming Interface)
Set of functions and procedures that allow the creation of applications.

#### Kernel
The core component of an OS that manages system resources.

#### Shell
User interface to access OS services.

```bash
# Bash shell examples
ls -la  # List files with details
ps aux  # List running processes
grep "error" logfile.txt  # Search for "error" in logfile.txt
```

#### JVM (Java Virtual Machine)
Enables a computer to run Java programs by executing Java bytecode.

```java
// Java code that runs on JVM
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

#### Booting
Process of starting a computer by loading the operating system.

### Computing Paradigms

#### Multiprogramming
- Multiple programs loaded in memory
- CPU switches between programs
- Improves CPU utilization

#### Multiprocessing
- Multiple processors (CPUs) working together
- Parallel execution of processes
- Types: Symmetric (SMP) and Asymmetric (ASMP)

```c
// Example of multiprocessing with fork() in C
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();  // Create a new process
    
    if (pid < 0) {
        // Error occurred
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (pid == 0) {
        // Child process
        printf("Child process with PID: %d\n", getpid());
    } else {
        // Parent process
        printf("Parent process with PID: %d created child with PID: %d\n", 
               getpid(), pid);
    }
    
    return 0;
}
```

#### Multitasking
- Multiple tasks (processes) executed concurrently
- CPU time is shared among tasks
- Managed by the OS scheduler

#### Multithreading
- Multiple threads within a process
- Threads share process resources
- Lightweight compared to processes

```c
// Example of multithreading with POSIX threads in C
#include <stdio.h>
#include <pthread.h>

void *thread_function(void *arg) {
    int thread_id = *(int*)arg;
    printf("Thread %d is running\n", thread_id);
    return NULL;
}

int main() {
    pthread_t threads[3];
    int thread_args[3] = {1, 2, 3};
    
    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, thread_function, &thread_args[i]);
    }
    
    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }
    
    printf("All threads have completed\n");
    return 0;
}
```

### Kernel Architectures

#### Monolithic Kernel
- All OS services run in kernel space
- Direct communication between components
- Examples: Linux, FreeBSD
- **Advantages**: Performance, direct access to hardware
- **Disadvantages**: Large codebase, crash affects entire system

#### Microkernel
- Minimal functionality in kernel space
- Most services run in user space
- Examples: QNX, MINIX
- **Advantages**: Reliability, security, modularity
- **Disadvantages**: Performance overhead due to message passing

Windows uses a hybrid approach that is primarily monolithic but incorporates some microkernel features. While its NT kernel was originally designed with microkernel principles, it evolved to include more components in kernel space for performance reasons, making it more monolithic in practice.

### Computer Startup Process

When a computer is turned on:

1. **Power-On Self-Test (POST)**: Hardware initialization and testing
2. **BIOS/UEFI Initialization**: Firmware identifies bootable devices
3. **Bootloader Loading**: MBR/GPT loads the bootloader (e.g., GRUB)
4. **Kernel Loading**: Bootloader loads the OS kernel into memory
5. **Kernel Initialization**: Kernel sets up memory management, device drivers
6. **User Space Initialization**: System services and daemons start
7. **Login Screen**: System ready for user interaction

## Process Concepts

### Process vs Program

| Program | Process |
|---------|---------|
| Passive entity | Active entity |
| Binary executable file on disk | Program in execution |
| Static | Dynamic |
| No resources allocated | Has allocated resources |
| Contains instructions | Contains program counter, stack, data section |

### Process States

A process can exist in one of the following states:

1. **New**: Process is being created
2. **Ready**: Process is waiting to be assigned to a processor
3. **Running**: Process is executing on a processor
4. **Waiting/Blocked**: Process is waiting for some event (I/O completion, signal)
5. **Terminated**: Process has finished execution

```c
// State transition pseudocode
void process_state_demo() {
    // New
    process_t *proc = create_process("example");
    
    // Ready
    add_to_ready_queue(proc);
    
    // Running
    current_process = scheduler_select();
    execute(current_process);
    
    // Waiting
    if (needs_io(current_process)) {
        block_process(current_process, IO_EVENT);
        schedule_next_process();
    }
    
    // When I/O completes
    process_t *completed_io = get_io_completion();
    unblock_process(completed_io);
    add_to_ready_queue(completed_io);
    
    // Terminated
    if (is_complete(current_process)) {
        terminate_process(current_process);
        release_resources(current_process);
    }
}
```

### Types of Processes

1. **Foreground Processes**: Interactive processes that users initiate and interact with
2. **Background Processes**: Non-interactive processes that run with no user interface
3. **System Processes**: Background processes started by the OS during boot
4. **Child Processes**: Created by a parent process using fork() or spawn()
5. **Daemon Processes**: Background processes that run continuously

### Process Control Block (PCB)

PCB is a data structure that contains all the information about a process. It's created and maintained by the OS for each process.

**PCB Structure**:

```c
struct process_control_block {
    // Process identification
    pid_t process_id;
    pid_t parent_process_id;
    
    // Process state
    enum process_state state;
    
    // CPU registers
    struct cpu_context {
        uint64_t program_counter;
        uint64_t stack_pointer;
        uint64_t general_registers[16];
        uint64_t status_register;
    } context;
    
    // CPU scheduling information
    int priority;
    uint64_t time_quantum;
    uint64_t cpu_time_used;
    
    // Memory management
    void *memory_base;
    size_t memory_size;
    struct page_table *page_table;
    
    // I/O status
    struct open_file_table *open_files;
    
    // Accounting information
    time_t creation_time;
    uint64_t total_cpu_time;
    
    // Pointer to next PCB in list/queue
    struct process_control_block *next;
};
```

### Process Memory Layout

A process in memory typically has the following segments:

1. **Text/Code Segment**: Contains executable code (read-only)
2. **Data Segment**: Contains initialized global and static variables
3. **BSS Segment**: Contains uninitialized global and static variables (initialized to zero)
4. **Heap**: Dynamic memory allocation (grows upward)
5. **Stack**: Function calls, local variables, return addresses (grows downward)

```
High Address  +------------------+
              |      Stack       | ← Stack pointer (grows downward)
              |        ↓         |
              |                  |
              |        ↑         |
              |       Heap       | ← Heap pointer (grows upward)
              +------------------+
              |       BSS        | (uninitialized data)
              +------------------+
              |       Data       | (initialized data)
              +------------------+
Low Address   |       Text       | (code)
              +------------------+
```

### Process vs Threads

| Process | Thread |
|---------|--------|
| Independent execution unit | Subset of a process |
| Has own memory space | Shares memory with other threads |
| Communication is expensive (IPC) | Communication is easy (shared memory) |
| Context switching is expensive | Context switching is cheaper |
| Created using fork() | Created using pthread_create() |
| Isolated | Not isolated from other threads |

### Process Scheduling

#### Scheduling Queues

1. **Job Queue**: Set of all processes in the system
2. **Ready Queue**: Set of processes in memory, ready to execute
3. **Device Queue**: Set of processes waiting for a specific I/O device

#### Schedulers

1. **Long-term Scheduler (Job Scheduler)**:
   - Controls degree of multiprogramming
   - Selects which processes to load into memory
   - Executes less frequently

2. **Short-term Scheduler (CPU Scheduler)**:
   - Selects which process to execute next
   - Allocates CPU to the selected process
   - Executes very frequently

3. **Medium-term Scheduler (Swapper)**:
   - Handles swapping processes in and out of memory
   - Reduces degree of multiprogramming when needed
   - Executes at medium frequency

### CPU-Bound vs I/O-Bound Processes

**CPU-Bound Processes**:
- Spend more time doing computations
- Use CPU heavily with few I/O requests
- Examples: Scientific calculations, rendering

**I/O-Bound Processes**:
- Spend more time waiting for I/O operations
- Make frequent I/O requests
- Examples: Database operations, user interfaces

A well-balanced system should have a mix of CPU-bound and I/O-bound processes for optimal resource utilization.

### Context Switch

A context switch occurs when the CPU switches from one process to another.

**Steps involved**:
1. Save context (CPU registers, program counter) of currently running process
2. Update PCB of the current process
3. Move PCB to appropriate queue
4. Select a new process to run
5. Update PCB of the new process
6. Restore context of the new process

```c
// Context switch pseudocode
void context_switch(process_t *current, process_t *next) {
    // Save context of current process
    save_cpu_context(&current->context);
    
    // Update PCB state
    current->state = READY;
    
    // Add to ready queue if still active
    if (current->state != TERMINATED) {
        add_to_ready_queue(current);
    }
    
    // Update current process pointer
    current_process = next;
    next->state = RUNNING;
    
    // Restore context of new process
    restore_cpu_context(&next->context);
    
    // Continue execution of new process
    // (Program counter is now pointing to next process's code)
}
```

Context switching is expensive due to:
- Saving and restoring registers
- Switching memory maps
- Flushing TLB (Translation Lookaside Buffer)
- Cache pollution

### Inter-Process Communication (IPC)

IPC allows processes to communicate and synchronize with each other.

#### Shared Memory

Processes communicate by reading and writing to a shared memory region.

```c
// Shared memory example in C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <string.h>

int main() {
    // Key for the shared memory segment
    key_t key = ftok("shmfile", 65);
    
    // Create shared memory segment
    int shmid = shmget(key, 1024, 0666 | IPC_CREAT);
    
    // Attach to shared memory
    char *shared_memory = (char*)shmat(shmid, NULL, 0);
    
    printf("Write data to shared memory: ");
    char buffer[100];
    fgets(buffer, 100, stdin);
    strcpy(shared_memory, buffer);
    
    printf("Data written to shared memory: %s\n", shared_memory);
    
    // Detach from shared memory
    shmdt(shared_memory);
    
    // Delete the shared memory segment
    shmctl(shmid, IPC_RMID, NULL);
    
    return 0;
}
```

#### Message Passing

Processes communicate by exchanging messages through the OS.

```c
// Message queue example in C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/msg.h>
#include <string.h>

struct message {
    long message_type;
    char message_text[100];
};

int main() {
    // Key for the message queue
    key_t key = ftok("msgfile", 65);
    
    // Create message queue
    int msgid = msgget(key, 0666 | IPC_CREAT);
    
    struct message msg;
    msg.message_type = 1;
    
    printf("Write message: ");
    fgets(msg.message_text, 100, stdin);
    
    // Send message
    msgsnd(msgid, &msg, sizeof(msg), 0);
    
    printf("Message sent: %s\n", msg.message_text);
    
    // Receive message
    msgrcv(msgid, &msg, sizeof(msg), 1, 0);
    
    printf("Message received: %s\n", msg.message_text);
    
    // Delete message queue
    msgctl(msgid, IPC_RMID, NULL);
    
    return 0;
}
```

### Pipes

A pipe is a unidirectional communication channel between processes.

```c
// Pipe example in C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipe_fd[2]; // 0 for reading, 1 for writing
    pid_t pid;
    char write_msg[100] = "Hello from parent!";
    char read_msg[100];
    
    // Create pipe
    if (pipe(pipe_fd) == -1) {
        perror("Pipe creation failed");
        exit(1);
    }
    
    // Create child process
    pid = fork();
    
    if (pid < 0) {
        perror("Fork failed");
        exit(1);
    }
    
    if (pid > 0) { // Parent process
        // Close read end
        close(pipe_fd[0]);
        
        // Write to pipe
        write(pipe_fd[1], write_msg, strlen(write_msg) + 1);
        printf("Parent wrote: %s\n", write_msg);
        
        // Close write end
        close(pipe_fd[1]);
    } else { // Child process
        // Close write end
        close(pipe_fd[1]);
        
        // Read from pipe
        read(pipe_fd[0], read_msg, sizeof(read_msg));
        printf("Child read: %s\n", read_msg);
        
        // Close read end
        close(pipe_fd[0]);
    }
    
    return 0;
}
```

### Zombie Processes

A zombie process is a process that has completed execution but still has an entry in the process table.

```c
// Creating a zombie process in C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        // Fork failed
        perror("Fork failed");
        exit(1);
    } else if (pid == 0) {
        // Child process
        printf("Child process (PID: %d) is running\n", getpid());
        // Child process exits
        exit(0);
    } else {
        // Parent process
        printf("Parent process (PID: %d) created child (PID: %d)\n", getpid(), pid);
        
        // Sleep for a while without waiting for child
        // During this time, child becomes a zombie
        printf("Parent sleeping for 10 seconds...\n");
        sleep(10);
        
        // Now wait for the zombie child to be cleaned up
        wait(NULL);
        printf("Child has been reaped\n");
    }
    
    return 0;
}
```

The maximum number of zombie processes a system can handle depends on:
- Available process ID (PID) range
- System memory for process table entries

In practice, while there's no fixed limit, having too many zombie processes can exhaust the process table and prevent new processes from being created. Usually, parent processes should call `wait()` or `waitpid()` to clean up terminated child processes.

## Process Scheduling

### Why Process Scheduling is Needed

Process scheduling is crucial for:
1. **CPU Utilization**: Keeping the CPU as busy as possible
2. **Throughput**: Maximizing the number of processes completed per time unit
3. **Fairness**: Ensuring all processes get a fair share of CPU time
4. **Response Time**: Minimizing the time from request to first response
5. **Turnaround Time**: Minimizing the time to complete a process
6. **Waiting Time**: Minimizing the time processes spend waiting in the ready queue

### CPU Burst Cycle

Processes alternate between:
- **CPU Burst**: Process is executing on the CPU
- **I/O Burst**: Process is waiting for I/O completion

```
   CPU Burst      I/O Burst      CPU Burst      I/O Burst
┌─────────────┐┌─────────────┐┌─────────────┐┌─────────────┐
│  Process    ││  Process    ││  Process    ││  Process    │
│  using CPU  ││  waiting    ││  using CPU  ││  waiting    │...
│             ││  for I/O    ││             ││  for I/O    │
└─────────────┘└─────────────┘└─────────────┘└─────────────┘
```

CPU-bound processes have long CPU bursts and short I/O bursts.
I/O-bound processes have short CPU bursts and long I/O bursts.

### CPU Scheduler

The CPU scheduler selects a process from the ready queue to allocate the CPU.

#### When Scheduling Decisions Occur
1. When a process switches from running to waiting state (I/O request)
2. When a process switches from running to ready state (interrupt)
3. When a process switches from waiting to ready state (I/O completion)
4. When a process terminates

#### Types of Scheduling

**Preemptive Scheduling**:
- Currently running process can be interrupted and moved to ready state
- More responsive to high-priority or interactive processes
- Used in time-sharing systems
- Can lead to race conditions in shared data access

**Non-Preemptive Scheduling**:
- Currently running process runs until completion, voluntary yield, or I/O block
- No interruption mid-execution
- Simpler to implement
- Can lead to convoy effect (short processes waiting for long ones)

### Dispatcher

The dispatcher is the module that gives control of the CPU to the process selected by the scheduler.

**Role of Dispatcher**:
1. Context switching
2. Switching to user mode
3. Jumping to the proper location in the user program to restart

**Dispatch Latency**: Time taken by the dispatcher to stop one process and start another.

```
                  ┌───────────────────┐
                  │     Scheduler     │
                  │ (selects process) │
                  └─────────┬─────────┘
                            │
                            ▼
┌────────────┐     ┌───────────────────┐     ┌────────────┐
│  Process A │     │     Dispatcher    │     │  Process B │
│  (running) │────▶│ (performs context │────▶│  (running) │
│            │     │      switch)      │     │            │
└────────────┘     └───────────────────┘     └────────────┘
                            ▲
                            │
                  ┌─────────┴─────────┐
                  │  Dispatch Latency │
                  │    (time cost)    │
                  └───────────────────┘
```

### Scheduling Criteria

1. **CPU Utilization**: Keep the CPU as busy as possible (40-90%)
2. **Throughput**: Number of processes completed per time unit
3. **Turnaround Time**: Time from submission to completion
   ```
   Turnaround Time = Completion Time - Arrival Time
   ```
4. **Waiting Time**: Time spent in the ready queue
   ```
   Waiting Time = Turnaround Time - Burst Time
   ```
5. **Response Time**: Time from submission to first response
   ```
   Response Time = First Run Time - Arrival Time
   ```

### Scheduling Algorithms

#### 1. First-Come, First-Served (FCFS)
- Simplest scheduling algorithm
- Non-preemptive
- Processes are executed in order of arrival
- Can cause "convoy effect"

```c
// FCFS implementation pseudocode
void fcfs_schedule() {
    while (!is_empty(ready_queue)) {
        process_t *proc = dequeue(ready_queue);
        execute_process(proc);
        // Process runs until completion
    }
}
```

**Example**:
Consider 3 processes with CPU burst times:
- P1: 24 units
- P2: 3 units
- P3: 3 units

If they arrive in order P1, P2, P3:
- P1 runs for 24 units
- P2 runs for 3 units
- P3 runs for 3 units

Waiting times:
- P1: 0
- P2: 24
- P3: 27

Average waiting time: (0 + 24 + 27) / 3 = 17 units

#### 2. Shortest Job First (SJF)
- Process with shortest CPU burst time is scheduled first
- Can be preemptive or non-preemptive
- Optimal for minimizing average waiting time
- Difficult to implement because burst times are unknown

```c
// Non-preemptive SJF implementation pseudocode
void sjf_schedule() {
    while (!is_empty(ready_queue)) {
        // Find process with shortest burst time
        process_t *shortest = find_shortest_burst(ready_queue);
        remove_from_queue(ready_queue, shortest);
        
        execute_process(shortest);
        // Process runs until completion
    }
}
```

**Example**:
Consider 4 processes with arrival and CPU burst times:
- P1: arrival = 0, burst = 8
- P2: arrival = 1, burst = 4
- P3: arrival = 2, burst = 9
- P4: arrival = 3, burst = 5

Non-preemptive SJF execution order: P1, P2, P4, P3
Waiting times:
- P1: 0
- P2: 7
- P3: 17
- P4: 12

Average waiting time: (0 + 7 + 17 + 12) / 4 = 9 units

#### 3. Priority-Based Scheduling
- Each process is assigned a priority
- Process with highest priority is scheduled first
- Can be preemptive or non-preemptive
- May lead to starvation of low-priority processes

```c
// Priority scheduling implementation pseudocode
void priority_schedule() {
    while (!is_empty(ready_queue)) {
        // Find process with highest priority
        process_t *highest = find_highest_priority(ready_queue);
        remove_from_queue(ready_queue, highest);
        
        execute_process(highest);
        // Process runs until completion (non-preemptive)
        // or until higher priority process arrives (preemptive)
    }
}
```

**Example**:
Consider 4 processes with priorities (lower number means higher priority):
- P1: priority = 3, burst = 10
- P2: priority = 1, burst = 5
- P3: priority = 4, burst = 3
- P4: priority = 2, burst = 2

Execution order: P2, P4, P1, P3
Waiting times:
- P1: 7
- P2: 0
- P3: 17
- P4: 5

Average waiting time: (7 + 0 + 17 + 5) / 4 = 7.25 units

#### 4. Round-Robin (RR)
- Each process gets a small unit of CPU time (time quantum)
- After time quantum expires, process is preempted and added to the end of ready queue
- Fair allocation of CPU time, good for time-sharing systems
- Performance depends on the size of time quantum

```c
// Round-Robin implementation pseudocode
void round_robin_schedule(int time_quantum) {
    while (!is_empty(ready_queue)) {
        process_t *proc = dequeue(ready_queue);
        
        if (proc->remaining_time <= time_quantum) {
            // Process can complete within time quantum
            execute_process(proc, proc->remaining_time);
            proc->remaining_time = 0;
        } else {
            // Process needs more time
            execute_process(proc, time_quantum);
            proc->remaining_time -= time_quantum;
            enqueue(ready_queue, proc); // Put back in ready queue
        }
    }
}
```

**Example**:
Consider 3 processes with CPU burst times and time quantum = 4:
- P1: burst = 20
- P2: burst = 3
- P3: burst = 5

Execution sequence: P1(4), P2(3), P3(4), P1(4), P3(1), P1(4), P1(4), P1(4)

Waiting times:
- P1: (0 + (7-4) + (15-8) + (19-12) + (23-16)) = 24
- P2: 4
- P3: (7 + (15-11)) = 11

Average waiting time: (24 + 4 + 11) / 3 = 13 units

#### 5. Multilevel Queue Scheduling (MLQS)
- Ready queue is divided into separate queues for different process types
- Each queue has its own scheduling algorithm
- There must be scheduling between queues

```
High Priority  ┌─────────────────────┐
               │  System Processes   │ ← FCFS
               └─────────────────────┘
               ┌─────────────────────┐
               │ Interactive Process │ ← Round Robin
               └─────────────────────┘
               ┌─────────────────────┐
               │   Batch Processes   │ ← SJF
               └─────────────────────┘
Low Priority   ┌─────────────────────┐
               │ Student Processes   │ ← FCFS
               └─────────────────────┘
```

```c
// Multilevel Queue implementation pseudocode
void multilevel_queue_schedule() {
    if (!is_empty(system_queue)) {
        // Service system processes first (highest priority)
        process_t *proc = dequeue(system_queue);
        execute_process(proc);
    } else if (!is_empty(interactive_queue)) {
        // Service interactive processes
        round_robin_schedule(interactive_queue, 4); // Time quantum = 4
    } else if (!is_empty(batch_queue)) {
        // Service batch processes
        sjf_schedule(batch_queue);
    } else if (!is_empty(student_queue)) {
        // Service student processes (lowest priority)
        fcfs_schedule(student_queue);
    }
}
```

#### 6. Multilevel Feedback Queue Scheduling (MLFQS)
- Similar to MLQS but allows processes to move between queues
- If a process uses too much CPU time, it is moved to a lower-priority queue
- If a process waits too long, it may be moved to a higher-priority queue
- Adapts to process behavior

```
                    ┌─────────────────────┐
                ┌──▶│       Queue 0       │──┐
                │   │    (RR, q = 8)      │  │
                │   └─────────────────────┘  │
                │                            │ Too much
        New     │   ┌─────────────────────┐  │ CPU time
    processes   ├──▶│       Queue 1       │◀─┘
       join     │   │    (RR, q = 16)     │  │
                │   └─────────────────────┘  │
                │                            │ Too much
                │   ┌─────────────────────┐  │ CPU time
                └──▶│       Queue 2       │◀─┘
                    │       (FCFS)        │
                    └─────────────────────┘
```

```c
// Multilevel Feedback Queue implementation pseudocode
void add_process_to_queue(process_t *proc) {
    // New processes go to highest priority queue
    enqueue(high_priority_queue, proc);
    proc->priority_level = HIGH;
    proc->time_in_queue = 0;
}

void multilevel_feedback_queue_schedule() {
    // Check highest priority queue first
    if (!is_empty(high_priority_queue)) {
        process_t *proc = dequeue(high_priority_queue);
        
        // Time quantum for high priority is 8
        if (proc->remaining_time <= 8) {
            execute_process(proc, proc->remaining_time);
            proc->remaining_time = 0;
        } else {
            execute_process(proc, 8);
            proc->remaining_time -= 8;
            
            // Demote to medium priority queue
            enqueue(medium_priority_queue, proc);
            proc->priority_level = MEDIUM;
        }
    }
    // Then check medium priority queue
    else if (!is_empty(medium_priority_queue)) {
        process_t *proc = dequeue(medium_priority_queue);
        
        // Time quantum for medium priority is 16
        if (proc->remaining_time <= 16) {
            execute_process(proc, proc->remaining_time);
            proc->remaining_time = 0;
        } else {
            execute_process(proc, 16);
            proc->remaining_time -= 16;
            
            // Demote to low priority queue
            enqueue(low_priority_queue, proc);
            proc->priority_level = LOW;
        }
    }
    // Finally check low priority queue
    else if (!is_empty(low_priority_queue)) {
        process_t *proc = dequeue(low_priority_queue);
        
        // FCFS for low priority
        execute_process(proc, proc->remaining_time);
        proc->remaining_time = 0;
    }
    
    // Age processes that have waited too long
    age_processes();
}

void age_processes() {
    // Promote processes that have waited too long
    for (each process in medium_priority_queue) {
        if (process->time_in_queue > AGING_THRESHOLD) {
            remove_from_queue(medium_priority_queue, process);
            enqueue(high_priority_queue, process);
            process->priority_level = HIGH;
            process->time_in_queue = 0;
        }
    }
    
    for (each process in low_priority_queue) {
        if (process->time_in_queue > AGING_THRESHOLD) {
            remove_from_queue(low_priority_queue, process);
            enqueue(medium_priority_queue, process);
            process->priority_level = MEDIUM;
            process->time_in_queue = 0;
        }
    }
}
```

### Real-World OS Scheduling Algorithms

1. **Linux**:
   - Completely Fair Scheduler (CFS) for regular processes
   - Real-Time scheduler for real-time processes
   - Uses priority-based preemptive scheduling

2. **Windows**:
   - Priority-based preemptive scheduling
   - Uses multilevel feedback queue
   - Boosts priority of I/O-bound processes

3. **macOS/iOS**:
   - Priority-based preemptive scheduling
   - Uses multilevel feedback queue

### Important Concepts

#### Starvation
Starvation occurs when a process is indefinitely denied necessary resources (like CPU time).

**Causes**:
- Low-priority processes never get CPU time in priority scheduling
- Resource hogging by high-priority processes
- Inadequate resource allocation policy

#### Aging
Aging is a technique to prevent starvation by gradually increasing the priority of processes that wait in the system for a long time.

```c
// Aging implementation pseudocode
void apply_aging() {
    for (each process in ready_queue) {
        // Increase priority as waiting time increases
        process->priority += process->waiting_time / AGING_FACTOR;
        
        // Cap priority at maximum value
        if (process->priority > MAX_PRIORITY) {
            process->priority = MAX_PRIORITY;
        }
    }
}
```

### Preventing Starvation

1. **Aging**: Gradually increase the priority of waiting processes
2. **Resource Reservation**: Reserve resources for low-priority processes
3. **Fair Queuing**: Ensure each process gets a fair share of resources
4. **Priority Inversion Protocols**: Temporarily boost priorities of processes holding resources needed by higher-priority processes
5. **Time Slicing**: Ensure each process gets at least some CPU time

```c
// Example of priority inheritance to prevent priority inversion
void acquire_resource(process_t *proc, resource_t *res) {
    if (res->owner != NULL) {
        // Resource is owned by another process
        if (proc->priority > res->owner->priority) {
            // Temporarily boost the priority of the resource owner
            res->owner->original_priority = res->owner->priority;
            res->owner->priority = proc->priority;
            printf("Boosting process %d priority to %d\n", 
                   res->owner->pid, proc->priority);
        }
        
        // Block the process until resource is available
        proc->state = BLOCKED;
        add_to_resource_queue(res, proc);
    } else {
        // Resource is available, acquire it
        res->owner = proc;
    }
}

void release_resource(process_t *proc, resource_t *res) {
    // Restore original priority if it was boosted
    if (proc->priority != proc->original_priority) {
        proc->priority = proc->original_priority;
        printf("Restoring process %d priority to %d\n", 
               proc->pid, proc->priority);
    }
    
    // Release the resource
    res->owner = NULL;
    
    // Wake up a waiting process if any
    if (!is_empty(res->waiting_queue)) {
        process_t *waiting_proc = dequeue(res->waiting_queue);
        waiting_proc->state = READY;
        add_to_ready_queue(waiting_proc);
    }
}
```

## Thread Concepts

### What is a Thread?

A thread is the smallest unit of processing that can be scheduled by an operating system. It is a lightweight process that exists within a process and shares resources such as memory space, code segment, and open files with other threads in the same process.

```c
// Visual representation of threads within a process
/*
    Process
    ┌───────────────────────────────────────────────┐
    │                                               │
    │  Code Segment (shared by all threads)         │
    │                                               │
    │  Data Segment (shared by all threads)         │
    │                                               │
    │  Files/Resources (shared by all threads)      │
    │                                               │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────┐│
    │  │  Thread 1   │  │  Thread 2   │  │Thread 3 ││
    │  │             │  │             │  │         ││
    │  │ - Registers │  │ - Registers │  │- Regist.││
    │  │ - Stack     │  │ - Stack     │  │- Stack  ││
    │  │ - State     │  │ - State     │  │- State  ││
    │  └─────────────┘  └─────────────┘  └─────────┘│
    │                                               │
    └───────────────────────────────────────────────┘
*/
```

### Benefits of Multithreading

1. **Resource Sharing**: Threads share the same address space and resources
2. **Responsiveness**: Application remains responsive during intensive operations
3. **Economy**: Creating and context-switching threads is less expensive than processes
4. **Scalability**: Better utilization of multiprocessor architectures
5. **Improved Throughput**: Multiple threads can execute in parallel

```c
// Example of a multithreaded server in C
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_CLIENTS 5

void *handle_client(void *arg) {
    int client_id = *(int*)arg;
    printf("Handling client %d\n", client_id);
    
    // Simulate processing
    sleep(2);
    
    printf("Finished handling client %d\n", client_id);
    return NULL;
}

int main() {
    pthread_t threads[NUM_CLIENTS];
    int client_ids[NUM_CLIENTS];
    
    printf("Server starting...\n");
    
    for (int i = 0; i < NUM_CLIENTS; i++) {
        client_ids[i] = i + 1;
        pthread_create(&threads[i], NULL, handle_client, &client_ids[i]);
        printf("Created thread for client %d\n", client_ids[i]);
    }
    
    // Wait for all client threads to complete
    for (int i = 0; i < NUM_CLIENTS; i++) {
        pthread_join(threads[i], NULL);
    }
    
    printf("All clients have been handled\n");
    return 0;
}
```

### Examples of Multithreaded Applications

1. **Web Browsers**:
   - Separate threads for rendering, downloading, JavaScript execution
   - Allows browsing to continue while pages load

2. **Web Servers**:
   - Thread per client connection
   - Allows handling multiple clients simultaneously

3. **Database Management Systems**:
   - Separate threads for query processing, logging, cleanup
   - Improves response time for concurrent queries

4. **Video Games**:
   - Separate threads for rendering, physics, AI, sound
   - Ensures smooth gameplay experience

5. **Video Editing Software**:
   - Separate threads for UI, rendering, encoding
   - Maintains responsive interface during intensive tasks

### Thread Models

#### 1. Many-to-One Model
- Many user-level threads mapped to a single kernel thread
- Thread management is done in user space
- Examples: GNU Portable Threads

**Advantages**:
- Efficient thread management without kernel involvement
- Works on systems without thread support

**Disadvantages**:
- If a thread performs a blocking operation, the entire process blocks
- Cannot take advantage of multiprocessing

```
    User Space   ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
                 │ T1  │ │ T2  │ │ T3  │ │ T4  │
                 └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
                    │       │       │       │
                    └───────┼───────┼───────┘
                            │       │
    Kernel Space            └───┐   │
                                ▼   │
                            ┌───────┐
                            │Kernel │
                            │Thread │
                            └───────┘
```

#### 2. One-to-One Model
- Each user thread corresponds to a kernel thread
- Examples: Windows, Linux (NPTL)

**Advantages**:
- Better concurrency
- Can utilize multiple CPUs
- If a thread blocks, others can still run

**Disadvantages**:
- Creating a user thread requires creating a kernel thread
- Limited number of threads due to overhead

```
    User Space   ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
                 │ T1  │ │ T2  │ │ T3  │ │ T4  │
                 └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
                    │       │       │       │
                    ▼       ▼       ▼       ▼
    Kernel Space  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
                  │ KT1 │ │ KT2 │ │ KT3 │ │ KT4 │
                  └─────┘ └─────┘ └─────┘ └─────┘
```

#### 3. Many-to-Many Model
- Maps many user-level threads to a smaller or equal number of kernel threads
- Examples: Solaris, Windows with ThreadFiber package

**Advantages**:
- Combines benefits of both models
- Developers can create as many threads as needed
- Kernel needs to manage only a few threads

**Disadvantages**:
- Complex implementation
- Scheduling is more challenging

```
    User Space   ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
                 │ T1  │ │ T2  │ │ T3  │ │ T4  │
                 └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
                    │       │       │       │
                    └─┬─────┼───────┼───┐   │
                      │     └───┐   │   │   │
                      ▼         ▼   ▼   ▼   ▼
    Kernel Space  ┌─────┐     ┌─────┐ ┌─────┐
                  │ KT1 │     │ KT2 │ │ KT3 │
                  └─────┘     └─────┘ └─────┘
```

### Best Threading Model

The "best" threading model depends on specific requirements:

- **One-to-One** is generally preferred for modern systems because:
  - Takes advantage of multiprocessors
  - Provides better concurrency
  - Supported by modern operating systems
  - Thread libraries and frameworks handle optimization

- **Many-to-Many** can be better for specific high-concurrency scenarios where thousands of threads are needed

- **Many-to-One** is mostly obsolete but may be useful for legacy systems

### Optimal Number of Threads

The optimal number of threads depends on:

1. **Number of CPU cores**: A good starting point is N threads = N cores
2. **Nature of work**: 
   - CPU-bound tasks: N threads = N cores
   - I/O-bound tasks: N threads > N cores

A common formula is:
```
Number of threads = Number of cores * (1 + Wait time / Compute time)
```

For example, if tasks spend 90% of time waiting (I/O) and 10% computing:
```
Number of threads = 8 cores * (1 + 0.9/0.1) = 8 * 10 = 80 threads
```

```c
// Example to determine optimal thread count
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

// Function to measure performance with different thread counts
void measure_performance(int num_threads, int work_items) {
    // Implementation details
    clock_t start = clock();
    
    // Create threads and distribute work
    pthread_t threads[num_threads];
    
    // Thread work here...
    
    // Join threads
    
    clock_t end = clock();
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    printf("Threads: %d, Time: %.2f seconds\n", num_threads, cpu_time_used);
}

int main() {
    int num_cores = 8; // Assume 8 cores system
    int work_items = 10000; // Total work to be done
    
    // Test performance with different thread counts
    for (int i = 1; i <= num_cores * 4; i *= 2) {
        measure_performance(i, work_items);
    }
    
    return 0;
}
```

### Effect of Multiple Cores on Multithreading

Multiple CPU cores allow threads to execute truly in parallel instead of just concurrently.

**Benefits**:
- True parallelism, not just time-slicing
- Linear performance scaling (ideally)
- Better utilization of hardware resources

**Challenges**:
1. **Race Conditions**: Multiple threads accessing shared data
2. **Cache Coherence**: Ensuring all cores see consistent memory state
3. **False Sharing**: Performance degradation due to cache line contention
4. **Synchronization Overhead**: Locks, mutexes slow down performance
5. **Uneven Work Distribution**: Some threads may finish early

```c
// Example demonstrating false sharing
#include <stdio.h>
#include <pthread.h>
#include <time.h>

// Array with values that will be incremented by threads
struct thread_data {
    int value;       // Value to increment
    // Adding padding to prevent false sharing
    char padding[60]; // Assumes 64-byte cache line
} thread_data_array[8];

// Without padding, these values would be on the same cache line
// causing false sharing and performance degradation

void *increment_counter(void *arg) {
    int thread_id = *(int*)arg;
    
    // Increment counter 10 million times
    for (int i = 0; i < 10000000; i++) {
        thread_data_array[thread_id].value++;
    }
    
    return NULL;
}

int main() {
    pthread_t threads[8];
    int thread_ids[8];
    clock_t start, end;
    
    // Initialize values
    for (int i = 0; i < 8; i++) {
        thread_data_array[i].value = 0;
    }
    
    start = clock();
    
    // Create threads
    for (int i = 0; i < 8; i++) {
        thread_ids[i] = i;
        pthread_create(&threads[i], NULL, increment_counter, &thread_ids[i]);
    }
    
    // Wait for threads to complete
    for (int i = 0; i < 8; i++) {
        pthread_join(threads[i], NULL);
    }
    
    end = clock();
    
    // Print results
    for (int i = 0; i < 8; i++) {
        printf("Thread %d: %d\n", i, thread_data_array[i].value);
    }
    
    printf("Time taken: %.2f seconds\n", 
           ((double)(end - start)) / CLOCKS_PER_SEC);
    
    return 0;
}
```

### Thread vs Process (Comparison)

| Feature | Process | Thread |
|---------|---------|--------|
| Definition | Program in execution | Lightweight unit of execution within a process |
| Creation | Expensive (requires new address space) | Inexpensive (shares address space) |
| Communication | Requires IPC mechanisms | Direct access to shared memory |
| Context Switch | Expensive (must save/restore more state) | Less expensive (maintains process context) |
| Memory | Separate memory space | Shared memory with other threads |
| Resources | Has own resources | Shares resources with other threads |
| Isolation | Protected from other processes | Vulnerable to other threads |
| Termination | Resources reclaimed by OS | Resources remain with process until all threads exit |

### Why C++ Static Variables are Dangerous in Real-Life OS

Static variables in multithreaded environments can cause serious problems:

1. **Thread Safety Issues**: Static variables are shared across all threads, creating potential race conditions

2. **Initialization Order Problems**: The order of initialization of static variables across translation units is undefined

3. **Resource Leaks**: Static variables persist for the program's lifetime, potentially leading to resource exhaustion

4. **Hidden Dependencies**: Static variables create implicit dependencies that make code harder to understand and test

5. **Global State**: Makes code less modular and harder to reason about

```cpp
// Example showing problems with static variables in multithreaded code
#include <iostream>
#include <thread>
#include <vector>
#include <mutex>

// Dangerous static variable (global state)
static int shared_counter = 0;

// Better approach with thread-local storage
thread_local int thread_local_counter = 0;

// Function using the dangerous static variable
void increment_shared(int iterations) {
    for (int i = 0; i < iterations; i++) {
        // Race condition here!
        shared_counter++;
    }
}

// Thread-safe version using mutex
std::mutex counter_mutex;
void increment_shared_safe(int iterations) {
    for (int i = 0; i < iterations; i++) {
        std::lock_guard<std::mutex> lock(counter_mutex);
        shared_counter++;
    }
}

// Function using thread-local storage (safe)
void increment_local(int iterations) {
    for (int i = 0; i < iterations; i++) {
        thread_local_counter++;
    }
    std::cout << "Thread " << std::this_thread::get_id() 
              << " counter: " << thread_local_counter << std::endl;
}

int main() {
    const int NUM_THREADS = 10;
    const int ITERATIONS = 100000;
    
    // Demonstrate race condition
    {
        shared_counter = 0;
        std::vector<std::thread> threads;
        
        for (int i = 0; i < NUM_THREADS; i++) {
            threads.push_back(std::thread(increment_shared, ITERATIONS));
        }
        
        for (auto& t : threads) {
            t.join();
        }
        
        std::cout << "Expected value: " << NUM_THREADS * ITERATIONS << std::endl;
        std::cout << "Actual value: " << shared_counter << std::endl;
    }
    
    // Thread-safe version
    {
        shared_counter = 0;
        std::vector<std::thread> threads;
        
        for (int i = 0; i < NUM_THREADS; i++) {
            threads.push_back(std::thread(increment_shared_safe, ITERATIONS));
        }
        
        for (auto& t : threads) {
            t.join();
        }
        
        std::cout << "Thread-safe expected value: " << NUM_THREADS * ITERATIONS << std::endl;
        std::cout << "Thread-safe actual value: " << shared_counter << std::endl;
    }
    
    // Thread-local storage version
    {
        std::vector<std::thread> threads;
        
        for (int i = 0; i < 3; i++) { // Just use 3 threads for demonstration
            threads.push_back(std::thread(increment_local, 5));
        }
        
        for (auto& t : threads) {
            t.join();
        }
    }
    
    return 0;
}
```

## Synchronization

### Why Process Coordination/Synchronization is Needed

Process synchronization ensures orderly execution of cooperating processes to maintain data consistency and system integrity.

It's needed because:

1. **Data Inconsistency**: Without synchronization, concurrent access can corrupt data
2. **Race Conditions**: Multiple processes may try to modify the same data simultaneously
3. **Deterministic Execution**: Ensures predictable behavior in concurrent systems
4. **Deadlock Prevention**: Manages resource allocation to prevent deadlocks

### Physical Address Space vs Logical Address Space

**Logical Address Space**:
- Addresses generated by the CPU during execution
- Also called virtual addresses
- Used by programs without knowing the actual physical location
- Allows for memory protection and efficient memory utilization

**Physical Address Space**:
- Actual addresses in the physical memory (RAM)
- Address seen by the memory unit
- Typically hidden from application programs
- Limited by the amount of RAM installed

Translation between logical and physical addresses is performed by the Memory Management Unit (MMU).

```
┌─────────────────┐      ┌─────────────┐      ┌────────────────┐
│  Logical/Virtual│      │    MMU      │      │  Physical      │
│    Address      │─────▶│ (Translation)│─────▶│  Address       │
│   0 to MAX_LOG  │      │             │      │ 0 to MAX_PHYS  │
└─────────────────┘      └─────────────┘      └────────────────┘
                         Base & Limit
                         Page Tables
                         Segment Tables
```

### Important Terms in Synchronization

#### Mutual Exclusion
Mutual exclusion (mutex) ensures that only one process can use a resource or execute a particular section of code at any given time.

```c
// Mutual exclusion using POSIX mutex
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int shared_resource = 0;

void* access_resource(void* arg) {
    int thread_id = *(int*)arg;
    
    pthread_mutex_lock(&mutex);
    // Critical section begins
    shared_resource++;
    printf("Thread %d: Resource value = %d\n", thread_id, shared_resource);
    // Critical section ends
    pthread_mutex_unlock(&mutex);
    
    return NULL;
}

int main() {
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;
    
    pthread_create(&t1, NULL, access_resource, &id1);
    pthread_create(&t2, NULL, access_resource, &id2);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Final resource value: %d\n", shared_resource);
    
    pthread_mutex_destroy(&mutex);
    return 0;
}
```

#### Critical Section
A critical section is a segment of code that accesses shared resources and must not be executed by more than one process simultaneously.

```c
// Critical section problem illustration
void process() {
    // Entry section - gain exclusive access
    acquire_lock();
    
    // Critical section
    // Access and modify shared resources
    shared_data++;
    
    // Exit section - release exclusive access
    release_lock();
    
    // Remainder section
    // Non-critical operations
}
```

### Critical Section Problem and Peterson's Solution

#### Critical Section Problem
Design protocols that processes can use to cooperate, ensuring:

1. **Mutual Exclusion**: Only one process in critical section at a time
2. **Progress**: If no process is in critical section, a process that wants to enter should be able to
3. **Bounded Waiting**: Limits on how many times other processes can enter while one is waiting

#### Peterson's Solution (for two processes)
Peterson's solution uses two variables:
- `turn`: Indicates whose turn it is to enter the critical section
- `flag[]`: Indicates if a process is ready to enter the critical section

```c
// Peterson's solution implementation
#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>

// Shared variables
int turn;
bool flag[2] = {false, false};
int shared_counter = 0;

void enter_critical_section(int process) {
    int other = 1 - process; // The other process
    
    flag[process] = true;    // I'm interested
    turn = other;            // Give preference to the other process
    
    // Wait until the other process is not interested or it's my turn
    while (flag[other] && turn == other) {
        // Busy wait (spin)
    }
    
    // Critical section
    // Now this process can access shared resources
}

void exit_critical_section(int process) {
    // Indicate this process is no longer interested
    flag[process] = false;
}

void* process_function(void* arg) {
    int process_id = *(int*)arg;
    
    for (int i = 0; i < 100000; i++) {
        enter_critical_section(process_id);
        
        // Critical section
        shared_counter++;
        
        exit_critical_section(process_id);
    }
    
    return NULL;
}

int main() {
    pthread_t p0, p1;
    int id0 = 0, id1 = 1;
    
    pthread_create(&p0, NULL, process_function, &id0);
    pthread_create(&p1, NULL, process_function, &id1);
    
    pthread_join(p0, NULL);
    pthread_join(p1, NULL);
    
    printf("Final counter value: %d\n", shared_counter);
    printf("Expected value: %d\n", 2 * 100000);
    
    return 0;
}
```

### Preemptive vs Non-Preemptive Kernel

#### Non-Preemptive Kernel
- A process keeps the CPU until it releases it voluntarily or blocks
- No process can be forcibly suspended
- Simpler to implement (no need for synchronization in kernel code)
- Can lead to poor response time for interactive applications

#### Preemptive Kernel
- Allows the CPU to be taken away from a process
- Better response time for high-priority processes
- More complex to implement (requires synchronization mechanisms)
- Used in modern operating systems (Linux, Windows, macOS)

A preemptive kernel is generally better because:
1. It improves system responsiveness
2. It prevents any single process from monopolizing the CPU
3. It allows real-time processing
4. It handles hardware interrupts more efficiently

### Semaphores

A semaphore is a synchronization tool that provides a more sophisticated way to control access to shared resources.

#### Binary Semaphore / Mutex Lock
- Can only have values 0 or 1
- Used for mutual exclusion (similar to mutex)

```c
// Binary semaphore example
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t binary_sem;
int shared_variable = 0;

void* increment_function(void* arg) {
    int thread_id = *(int*)arg;
    
    for (int i = 0; i < 1000000; i++) {
        // Wait
        sem_wait(&binary_sem);
        
        // Critical section
        shared_variable++;
        
        // Signal
        sem_post(&binary_sem);
    }
    
    printf("Thread %d completed\n", thread_id);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;
    
    // Initialize semaphore with value 1
    sem_init(&binary_sem, 0, 1);
    
    pthread_create(&t1, NULL, increment_function, &id1);
    pthread_create(&t2, NULL, increment_function, &id2);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Final value: %d\n", shared_variable);
    printf("Expected value: %d\n", 2 * 1000000);
    
    sem_destroy(&binary_sem);
    return 0;
}
```

#### Counting Semaphore
- Can have arbitrary non-negative values
- Used for resource counting and synchronization

```c
// Counting semaphore example for producer-consumer
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5

sem_t empty;    // Counts empty buffer slots
sem_t full;     // Counts full buffer slots
sem_t mutex;    // Binary semaphore for mutual exclusion

int buffer[BUFFER_SIZE];
int in = 0, out = 0;

void* producer(void* arg) {
    int item = 0;
    
    for (int i = 0; i < 10; i++) {
        item = i;
        
        // Wait for an empty slot
        sem_wait(&empty);
        
        // Wait for mutex
        sem_wait(&mutex);
        
        // Critical section
        buffer[in] = item;
        printf("Producer: Inserted item %d at position %d\n", item, in);
        in = (in + 1) % BUFFER_SIZE;
        
        // Release mutex
        sem_post(&mutex);
        
        // Signal a full slot
        sem_post(&full);
        
        // Sleep to simulate varying production time
        usleep(rand() % 1000000);
    }
    
    return NULL;
}

void* consumer(void* arg) {
    int item;
    
    for (int i = 0; i < 10; i++) {
        // Wait for a full slot
        sem_wait(&full);
        
        // Wait for mutex
        sem_wait(&mutex);
        
        // Critical section
        item = buffer[out];
        printf("Consumer: Removed item %d from position %d\n", item, out);
        out = (out + 1) % BUFFER_SIZE;
        
        // Release mutex
        sem_post(&mutex);
        
        // Signal an empty slot
        sem_post(&empty);
        
        // Sleep to simulate varying consumption time
        usleep(rand() % 1000000);
    }
    
    return NULL;
}

int main() {
    pthread_t prod, cons;
    
    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE); // All slots are empty initially
    sem_init(&full, 0, 0);            // No slot is full initially
    sem_init(&mutex, 0, 1);           // Binary semaphore for mutual exclusion
    
    pthread_create(&prod, NULL, producer, NULL);
    pthread_create(&cons, NULL, consumer, NULL);
    
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);
    
    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);
    
    return 0;
}
```

### Busy Waiting and Spin Lock

#### Busy Waiting
Busy waiting (or spinning) is a technique where a process repeatedly checks if a condition is true rather than yielding the CPU.

**Advantages**:
- No context switch overhead
- Effective for very short waits

**Disadvantages**:
- Wastes CPU cycles
- Not energy efficient

#### Spin Lock
A spin lock is a lock that uses busy waiting instead of blocking when the lock is not available.

```c
// Spin lock example using atomic operations
#include <stdio.h>
#include <pthread.h>
#include <stdatomic.h>

// Spin lock using atomic flag
atomic_flag lock = ATOMIC_FLAG_INIT;

void acquire_spinlock() {
    // Spin until we acquire the lock
    while (atomic_flag_test_and_set(&lock)) {
        // Busy wait (spin)
    }
}

void release_spinlock() {
    atomic_flag_clear(&lock);
}

int shared_counter = 0;

void* increment_function(void* arg) {
    int thread_id = *(int*)arg;
    
    for (int i = 0; i < 1000000; i++) {
        acquire_spinlock();
        // Critical section
        shared_counter++;
        release_spinlock();
    }
    
    printf("Thread %d completed\n", thread_id);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;
    
    pthread_create(&t1, NULL, increment_function, &id1);
    pthread_create(&t2, NULL, increment_function, &id2);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Final value: %d\n", shared_counter);
    printf("Expected value: %d\n", 2 * 1000000);
    
    return 0;
}
```

### Real-World Implementation of Binary Semaphore

In real-world code, binary semaphores can be implemented using platform-specific APIs or libraries:

```c
// POSIX semaphore implementation
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

// Named semaphore for inter-process synchronization
int main() {
    sem_t *sem;
    
    // Create or open a named semaphore
    sem = sem_open("/my_semaphore", O_CREAT, 0644, 1);
    if (sem == SEM_FAILED) {
        perror("sem_open failed");
        return 1;
    }
    
    printf("Waiting to enter critical section...\n");
    sem_wait(sem);
    
    // Critical section
    printf("In critical section\n");
    sleep(3);
    printf("Leaving critical section\n");
    
    sem_post(sem);
    
    // Close and unlink semaphore
    sem_close(sem);
    sem_unlink("/my_semaphore");
    
    return 0;
}
```

### Deadlock and Starvation

#### Deadlock
A deadlock occurs when two or more processes are waiting indefinitely for events that will never occur.

**Example**:
Process A holds Resource 1 and waits for Resource 2
Process B holds Resource 2 and waits for Resource 1

```c
// Deadlock example with two threads and two mutexes
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER;

void* thread1_function(void* arg) {
    printf("Thread 1: Trying to acquire mutex1\n");
    pthread_mutex_lock(&mutex1);
    printf("Thread 1: Acquired mutex1\n");
    
    // Sleep to give thread 2 a chance to acquire mutex2
    sleep(1);
    
    printf("Thread 1: Trying to acquire mutex2\n");
    pthread_mutex_lock(&mutex2);
    printf("Thread 1: Acquired mutex2\n");
    
    // Critical section
    printf("Thread 1: In critical section\n");
    
    pthread_mutex_unlock(&mutex2);
    pthread_mutex_unlock(&mutex1);
    
    return NULL;
}

void* thread2_function(void* arg) {
    printf("Thread 2: Trying to acquire mutex2\n");
    pthread_mutex_lock(&mutex2);
    printf("Thread 2: Acquired mutex2\n");
    
    // Sleep to give thread 1 a chance to acquire mutex1
    sleep(1);
    
    printf("Thread 2: Trying to acquire mutex1\n");
    pthread_mutex_lock(&mutex1);
    printf("Thread 2: Acquired mutex1\n");
    
    // Critical section
    printf("Thread 2: In critical section\n");
    
    pthread_mutex_unlock(&mutex1);
    pthread_mutex_unlock(&mutex2);
    
    return NULL;
}

int main() {
    pthread_t t1, t2;
    
    pthread_create(&t1, NULL, thread1_function, NULL);
    pthread_create(&t2, NULL, thread2_function, NULL);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Both threads completed\n");
    
    pthread_mutex_destroy(&mutex1);
    pthread_mutex_destroy(&mutex2);
    
    return 0;
}
```

#### Starvation
Starvation occurs when a process is denied necessary resources indefinitely.

**Causes**:
- Low-priority processes never get CPU time
- Biased resource allocation policy
- Indefinite blocking

```c
// Example of potential starvation with biased reader-writer lock
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

int readers_count = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t resource = PTHREAD_MUTEX_INITIALIZER;

void* reader_function(void* arg) {
    int reader_id = *(int*)arg;
    
    while (1) {
        // Entry section
        pthread_mutex_lock(&mutex);
        readers_count++;
        if (readers_count == 1) {
            // First reader locks the resource
            pthread_mutex_lock(&resource);
        }
        pthread_mutex_unlock(&mutex);
        
        // Critical section
        printf("Reader %d is reading\n", reader_id);
        usleep(100000); // Read for 0.1 seconds
        
        // Exit section
        pthread_mutex_lock(&mutex);
        readers_count--;
        if (readers_count == 0) {
            // Last reader unlocks the resource
            pthread_mutex_unlock(&resource);
        }
        pthread_mutex_unlock(&mutex);
        
        // Non-critical section
        usleep(10000); // Think for 0.01 seconds
    }
    
    return NULL;
}

void* writer_function(void* arg) {
    int writer_id = *(int*)arg;
    
    while (1) {
        // Entry section
        printf("Writer %d is waiting\n", writer_id);
        pthread_mutex_lock(&resource);
        
        // Critical section
        printf("Writer %d is writing\n", writer_id);
        usleep(50000); // Write for 0.05 seconds
        
        // Exit section
        pthread_mutex_unlock(&resource);
        
        // Non-critical section
        usleep(200000); // Think for 0.2 seconds
    }
    
    return NULL;
}

int main() {
    pthread_t readers[5], writers[2];
    int reader_ids[5], writer_ids[2];
    
    // Create readers
    for (int i = 0; i < 5; i++) {
        reader_ids[i] = i + 1;
        pthread_create(&readers[i], NULL, reader_function, &reader_ids[i]);
    }
    
    // Create writers
    for (int i = 0; i < 2; i++) {
        writer_ids[i] = i + 1;
        pthread_create(&writers[i], NULL, writer_function, &writer_ids[i]);
    }
    
    // Let the simulation run for 5 seconds
    sleep(5);
    
    // In this example, writers might starve because there's always a reader
    
    return 0;
}
```

### Classic Synchronization Problems

#### Bounded Buffer (Producer-Consumer) Problem
Producers generate data and place it in a buffer, while consumers remove data from the buffer.

```c
// Bounded buffer solution using semaphores
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <stdlib.h>

#define BUFFER_SIZE 5
#define NUM_PRODUCERS 2
#define NUM_CONSUMERS 2
#define ITEMS_PER_PRODUCER 10

typedef struct {
    int items[BUFFER_SIZE];
    int in;
    int out;
} buffer_t;

buffer_t buffer = {{0}, 0, 0};

sem_t empty;    // Counts empty buffer slots
sem_t full;     // Counts full buffer slots
sem_t mutex;    // Binary semaphore for mutual exclusion

void* producer(void* arg) {
    int producer_id = *(int*)arg;
    
    for (int i = 0; i < ITEMS_PER_PRODUCER; i++) {
        int item = producer_id * 100 + i;
        
        // Wait for an empty slot
        sem_wait(&empty);
        
        // Wait for mutex
        sem_wait(&mutex);
        
        // Critical section
        buffer.items[buffer.in] = item;
        printf("Producer %d: Inserted item %d at position %d\n", 
               producer_id, item, buffer.in);
        buffer.in = (buffer.in + 1) % BUFFER_SIZE;
        
        // Release mutex
        sem_post(&mutex);
        
        // Signal a full slot
        sem_post(&full);
        
        // Sleep to simulate varying production time
        usleep(rand() % 500000);
    }
    
    printf("Producer %d finished\n", producer_id);
    return NULL;
}

void* consumer(void* arg) {
    int consumer_id = *(int*)arg;
    int items_consumed = 0;
    
    while (items_consumed < (NUM_PRODUCERS * ITEMS_PER_PRODUCER) / NUM_CONSUMERS) {
        // Wait for a full slot
        sem_wait(&full);
        
        // Wait for mutex
        sem_wait(&mutex);
        
        // Critical section
        int item = buffer.items[buffer.out];
        printf("Consumer %d: Removed item %d from position %d\n", 
               consumer_id, item, buffer.out);
        buffer.out = (buffer.out + 1) % BUFFER_SIZE;
        items_consumed++;
        
        // Release mutex
        sem_post(&mutex);
        
        // Signal an empty slot
        sem_post(&empty);
        
        // Sleep to simulate varying consumption time
        usleep(rand() % 800000);
    }
    
    printf("Consumer %d finished\n", consumer_id);
    return NULL;
}

int main() {
    pthread_t producers[NUM_PRODUCERS], consumers[NUM_CONSUMERS];
    int producer_ids[NUM_PRODUCERS], consumer_ids[NUM_CONSUMERS];
    
    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE); // All slots are empty initially
    sem_init(&full, 0, 0);            // No slot is full initially
    sem_init(&mutex, 0, 1);           // Binary semaphore for mutual exclusion
    
    // Create producers
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        producer_ids[i] = i + 1;
        pthread_create(&producers[i], NULL, producer, &producer_ids[i]);
    }
    
    // Create consumers
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        consumer_ids[i] = i + 1;
        pthread_create(&consumers[i], NULL, consumer, &consumer_ids[i]);
    }
    
    // Wait for producers to finish
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        pthread_join(producers[i], NULL);
    }
    
    // Wait for consumers to finish
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        pthread_join(consumers[i], NULL);
    }
    
    // Clean up semaphores
    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);
    
    printf("All producers and consumers have finished\n");
    return 0;
}
```

#### Readers-Writers Problem
Multiple processes want to access shared data - some only read it (readers), some update it (writers).

```c
// Readers-Writers solution with writer priority
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

#define NUM_READERS 5
#define NUM_WRITERS 2
#define NUM_ITERATIONS 5

pthread_mutex_t resource_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t reader_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t writer_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t order_mutex = PTHREAD_MUTEX_INITIALIZER;

int active_readers = 0;
int waiting_writers = 0;
int active_writers = 0;
int shared_data = 0;

void* reader(void* arg) {
    int reader_id = *(int*)arg;
    
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        // Request entry
        pthread_mutex_lock(&order_mutex);  // Ensure FIFO ordering
        pthread_mutex_lock(&reader_mutex);
        
        // Check if writers are waiting or active
        if (waiting_writers > 0 || active_writers > 0) {
            printf("Reader %d: Waiting because writers are active or waiting\n", 
                   reader_id);
            pthread_mutex_unlock(&reader_mutex);
            pthread_mutex_unlock(&order_mutex);
            
            // Wait for a while and try again
            usleep(rand() % 100000);
            i--; // Try again for this iteration
            continue;
        }
        
        // No writers, so increment active readers
        active_readers++;
        if (active_readers == 1) {
            // First reader acquires the resource
            pthread_mutex_lock(&resource_mutex);
        }
        
        pthread_mutex_unlock(&reader_mutex);
        pthread_mutex_unlock(&order_mutex);
        
        // Critical section - read
        printf("Reader %d: Reading data: %d\n", reader_id, shared_data);
        usleep(rand() % 200000); // Simulate reading
        
        // Exit critical section
        pthread_mutex_lock(&reader_mutex);
        active_readers--;
        if (active_readers == 0) {
            // Last reader releases the resource
            pthread_mutex_unlock(&resource_mutex);
        }
        pthread_mutex_unlock(&reader_mutex);
        
        // Do something with the data
        usleep(rand() % 300000);
    }
    
    printf("Reader %d: Finished\n", reader_id);
    return NULL;
}

void* writer(void* arg) {
    int writer_id = *(int*)arg;
    
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        // Request entry - indicate a writer is waiting
        pthread_mutex_lock(&writer_mutex);
        waiting_writers++;
        pthread_mutex_unlock(&writer_mutex);
        
        pthread_mutex_lock(&order_mutex);
        pthread_mutex_lock(&resource_mutex);
        
        pthread_mutex_lock(&writer_mutex);
        waiting_writers--;
        active_writers++;
        pthread_mutex_unlock(&writer_mutex);
        
        pthread_mutex_unlock(&order_mutex);
        
        // Critical section - write
        shared_data = writer_id * 100 + i;
        printf("Writer %d: Updated data to %d\n", writer_id, shared_data);
        usleep(rand() % 200000); // Simulate writing
        
        // Exit critical section
        pthread_mutex_lock(&writer_mutex);
        active_writers--;
        pthread_mutex_unlock(&writer_mutex);
        
        pthread_mutex_unlock(&resource_mutex);
        
        // Do something else
        usleep(rand() % 500000);
    }
    
    printf("Writer %d: Finished\n", writer_id);
    return NULL;
}

int main() {
    pthread_t readers[NUM_READERS], writers[NUM_WRITERS];
    int reader_ids[NUM_READERS], writer_ids[NUM_WRITERS];
    
    // Create readers
    for (int i = 0; i < NUM_READERS; i++) {
        reader_ids[i] = i + 1;
        pthread_create(&readers[i], NULL, reader, &reader_ids[i]);
    }
    
    // Create writers
    for (int i = 0; i < NUM_WRITERS; i++) {
        writer_ids[i] = i + 1;
        pthread_create(&writers[i], NULL, writer, &writer_ids[i]);
    }
    
    // Wait for readers to finish
    for (int i = 0; i < NUM_READERS; i++) {
        pthread_join(readers[i], NULL);
    }
    
    // Wait for writers to finish
    for (int i = 0; i < NUM_WRITERS; i++) {
        pthread_join(writers[i], NULL);
    }
    
    // Clean up mutexes
    pthread_mutex_destroy(&resource_mutex);
    pthread_mutex_destroy(&reader_mutex);
    pthread_mutex_destroy(&writer_mutex);
    pthread_mutex_destroy(&order_mutex);
    
    printf("Final shared data value: %d\n", shared_data);
    printf("All readers and writers have finished\n");
    return 0;
}
```

#### Dining Philosophers Problem
Five philosophers sit at a round table with five forks. Each philosopher needs two forks to eat.

```c
// Dining Philosophers solution with resource hierarchy
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

#define NUM_PHILOSOPHERS 5
#define NUM_MEALS 3

pthread_mutex_t forks[NUM_PHILOSOPHERS];
int meals_eaten[NUM_PHILOSOPHERS] = {0};

void* philosopher(void* arg) {
    int id = *(int*)arg;
    int left_fork = id;
    int right_fork = (id + 1) % NUM_PHILOSOPHERS;
    
    // Resource hierarchy solution: always pick up lower-numbered fork first
    if (left_fork > right_fork) {
        int temp = left_fork;
        left_fork = right_fork;
        right_fork = temp;
    }
    
    while (meals_eaten[id] < NUM_MEALS) {
        // Think
        printf("Philosopher %d is thinking\n", id);
        usleep(rand() % 500000);
        
        // Pick up forks
        printf("Philosopher %d is hungry and trying to pick up forks\n", id);
        pthread_mutex_lock(&forks[left_fork]);
        printf("Philosopher %d picked up fork %d\n", id, left_fork);
        pthread_mutex_lock(&forks[right_fork]);
        printf("Philosopher %d picked up fork %d\n", id, right_fork);
        
        // Eat
        printf("Philosopher %d is eating (meal %d)\n", id, meals_eaten[id] + 1);
        usleep(rand() % 300000);
        meals_eaten[id]++;
        
        // Put down forks
        pthread_mutex_unlock(&forks[right_fork]);
        printf("Philosopher %d put down fork %d\n", id, right_fork);
        pthread_mutex_unlock(&forks[left_fork]);
        printf("Philosopher %d put down fork %d\n", id, left_fork);
    }
    
    printf("Philosopher %d is satisfied after eating %d meals\n", id, meals_eaten[id]);
    return NULL;
}

int main() {
    pthread_t philosophers[NUM_PHILOSOPHERS];
    int ids[NUM_PHILOSOPHERS];
    
    // Initialize mutexes for forks
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_mutex_init(&forks[i], NULL);
    }
    
    // Create philosopher threads
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        ids[i] = i;
        pthread_create(&philosophers[i], NULL, philosopher, &ids[i]);
    }
    
    // Wait for philosophers to finish
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_join(philosophers[i], NULL);
    }
    
    // Clean up mutexes
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_mutex_destroy(&forks[i]);
    }
    
    printf("All philosophers have eaten their meals\n");
    return 0;
}
```

## Deadlocks

### What is a Deadlock?

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting to acquire a resource held by another process.

Multithreaded programs are particularly susceptible to deadlocks because threads can compete for shared resources.

```
Process 1 ──(holds)──▶ Resource A ◀──(needed by)─── Process 2
    ▲                                                   │
    │                                                   │
    └───(needs)───── Resource B ◀───(held by)───────────┘
```

### Effects of Deadlock

1. **Blocked Processes**: Processes involved in deadlock cannot progress
2. **Resource Underutilization**: Resources held by deadlocked processes are wasted
3. **System Performance**: Even processes not directly involved may be affected
4. **System Instability**: In severe cases, the system may need to be restarted
5. **Performance Overhead**: Deadlock prevention or detection mechanisms add overhead

### Necessary Conditions for Deadlock

All four conditions must be present for a deadlock to occur:

1. **Mutual Exclusion**: At least one resource must be held in a non-sharable mode
2. **Hold and Wait**: A process holding resources can request additional resources
3. **No Preemption**: Resources cannot be forcibly taken from a process
4. **Circular Wait**: A circular chain of processes, each waiting for a resource held by the next

```c
// Example illustrating the four necessary conditions
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t resource_A = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t resource_B = PTHREAD_MUTEX_INITIALIZER;

// This function demonstrates all four conditions for deadlock
void* process_1(void* arg) {
    printf("Process 1: Trying to acquire Resource A\n");
    pthread_mutex_lock(&resource_A);  // Mutual Exclusion
    printf("Process 1: Acquired Resource A\n");
    
    sleep(1);  // Give Process 2 time to acquire Resource B
    
    printf("Process 1: Trying to acquire Resource B\n");
    pthread_mutex_lock(&resource_B);  // Hold and Wait, No Preemption, Circular Wait
    printf("Process 1: Acquired Resource B\n");
    
    // Use both resources
    printf("Process 1: Using both resources\n");
    
    pthread_mutex_unlock(&resource_B);
    pthread_mutex_unlock(&resource_A);
    
    return NULL;
}

void* process_2(void* arg) {
    printf("Process 2: Trying to acquire Resource B\n");
    pthread_mutex_lock(&resource_B);  // Mutual Exclusion
    printf("Process 2: Acquired Resource B\n");
    
    sleep(1);  // Give Process 1 time to acquire Resource A
    
    printf("Process 2: Trying to acquire Resource A\n");
    pthread_mutex_lock(&resource_A);  // Hold and Wait, No Preemption, Circular Wait
    printf("Process 2: Acquired Resource A\n");
    
    // Use both resources
    printf("Process 2: Using both resources\n");
    
    pthread_mutex_unlock(&resource_A);
    pthread_mutex_unlock(&resource_B);
    
    return NULL;
}

int main() {
    pthread_t t1, t2;
    
    pthread_create(&t1, NULL, process_1, NULL);
    pthread_create(&t2, NULL, process_2, NULL);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    pthread_mutex_destroy(&resource_A);
    pthread_mutex_destroy(&resource_B);
    
    return 0;
}
```

### Methods for Deadlock Handling

#### 1. Deadlock Prevention
Prevent deadlocks by ensuring at least one of the four necessary conditions cannot hold.

##### Mutual Exclusion
- Some resources can be made sharable (e.g., read-only files)
- Not always possible for resources that require exclusive access

##### Hold and Wait
- Require processes to request all resources at once
- Or require a process to release all resources before requesting new ones

```c
// Hold and Wait prevention
void process_function() {
    // Acquire all resources at once
    acquire_all_resources();
    
    // Use resources
    
    // Release all resources
    release_all_resources();
}
```

##### No Preemption
- Allow preemption of resources when a process requesting a resource is blocked
- Typically used for resources whose state can be saved and restored

```c
// No Preemption prevention
void request_resource(int resource_id) {
    if (resource_available(resource_id)) {
        allocate_resource(resource_id);
    } else {
        // Release all currently held resources
        release_all_current_resources();
        
        // Wait for all needed resources to be available
        wait_for_resources();
    }
}
```

##### Circular Wait
- Impose a total ordering on resource types
- Require processes to request resources in increasing order

```c
// Circular Wait prevention
void safe_resource_allocation() {
    // Resources must be acquired in order of their IDs
    acquire_resource(1);
    acquire_resource(2);
    acquire_resource(3);
    
    // Use resources
    
    // Release in any order
    release_resource(2);
    release_resource(1);
    release_resource(3);
}
```

#### 2. Deadlock Avoidance
Allow processes to request resources dynamically, but ensure the system never enters an unsafe state.

##### Banker's Algorithm

The Banker's Algorithm determines if a resource allocation state is safe:

1. Initialize `Work` and `Finish` arrays
2. Find a process that can complete with current resources
3. Add its resources back to available pool
4. Mark process as finished
5. Repeat until all processes are finished or no eligible process found

```c
// Banker's Algorithm implementation
#include <stdio.h>
#include <stdbool.h>

#define NUM_PROCESSES 5
#define NUM_RESOURCES 3

// Available resources
int available[NUM_RESOURCES] = {3, 3, 2};

// Maximum demand of each process
int maximum[NUM_PROCESSES][NUM_RESOURCES] = {
    {7, 5, 3},  // Process 0
    {3, 2, 2},  // Process 1
    {9, 0, 2},  // Process 2
    {2, 2, 2},  // Process 3
    {4, 3, 3}   // Process 4
};

// Resources allocated to each process
int allocation[NUM_PROCESSES][NUM_RESOURCES] = {
    {0, 1, 0},  // Process 0
    {2, 0, 0},  // Process 1
    {3, 0, 2},  // Process 2
    {2, 1, 1},  // Process 3
    {0, 0, 2}   // Process 4
};

// Remaining need of each process
int need[NUM_PROCESSES][NUM_RESOURCES];

// Calculate need matrix
void calculate_need() {
    for (int i = 0; i < NUM_PROCESSES; i++) {
        for (int j = 0; j < NUM_RESOURCES; j++) {
            need[i][j] = maximum[i][j] - allocation[i][j];
        }
    }
}

// Check if the current state is safe
bool is_safe() {
    int work[NUM_RESOURCES];
    bool finish[NUM_PROCESSES] = {false};
    
    // Initialize work array
    for (int i = 0; i < NUM_RESOURCES; i++) {
        work[i] = available[i];
    }
    
    // Find an unfinished process that can be completed
    bool found;
    do {
        found = false;
        for (int i = 0; i < NUM_PROCESSES; i++) {
            if (!finish[i]) {
                // Check if process i can be completed
                bool can_allocate = true;
                for (int j = 0; j < NUM_RESOURCES; j++) {
                    if (need[i][j] > work[j]) {
                        can_allocate = false;
                        break;
                    }
                }
                
                if (can_allocate) {
                    // Process i can complete, update work array
                    for (int j = 0; j < NUM_RESOURCES; j++) {
                        work[j] += allocation[i][j];
                    }
                    finish[i] = true;
                    found = true;
                    printf("Process %d can complete\n", i);
                }
            }
        }
    } while (found);
    
    // Check if all processes are finished
    for (int i = 0; i < NUM_PROCESSES; i++) {
        if (!finish[i]) {
            return false;
        }
    }
    
    return true;
}

// Request resources for a process
bool request_resources(int process_id, int request[]) {
    // Check if request is valid
    for (int i = 0; i < NUM_RESOURCES; i++) {
        if (request[i] > need[process_id][i]) {
            printf("Error: Process %d requested more than its maximum claim\n", 
                   process_id);
            return false;
        }
        if (request[i] > available[i]) {
            printf("Error: Process %d must wait, resources not available\n", 
                   process_id);
            return false;
        }
    }
    
    // Try to allocate resources
    for (int i = 0; i < NUM_RESOURCES; i++) {
        available[i] -= request[i];
        allocation[process_id][i] += request[i];
        need[process_id][i] -= request[i];
    }
    
    // Check if the resulting state is safe
    if (is_safe()) {
        printf("Resources allocated to Process %d\n", process_id);
        return true;
    } else {
        // Rollback changes
        for (int i = 0; i < NUM_RESOURCES; i++) {
            available[i] += request[i];
            allocation[process_id][i] -= request[i];
            need[process_id][i] += request[i];
        }
        printf("Request denied: resulting state would be unsafe\n");
        return false;
    }
}

int main() {
    calculate_need();
    
    printf("Initial state:\n");
    for (int i = 0; i < NUM_PROCESSES; i++) {
        printf("Process %d - Allocation: [", i);
        for (int j = 0; j < NUM_RESOURCES; j++) {
            printf("%d ", allocation[i][j]);
        }
        printf("], Need: [");
        for (int j = 0; j < NUM_RESOURCES; j++) {
            printf("%d ", need[i][j]);
        }
        printf("]\n");
    }
    
    printf("Available resources: [");
    for (int i = 0; i < NUM_RESOURCES; i++) {
        printf("%d ", available[i]);
    }
    printf("]\n");
    
    if (is_safe()) {
        printf("The system is in a safe state\n");
    } else {
        printf("The system is in an unsafe state\n");
    }
    
    // Example resource request
    int request[NUM_RESOURCES] = {1, 0, 2};
    printf("\nProcess 1's resource request: [");
    for (int i = 0; i < NUM_RESOURCES; i++) {
        printf("%d ", request[i]);
    }
    printf("]\n");
    
    request_resources(1, request);
    
    return 0;
}
```

#### 3. Deadlock Detection and Recovery

Allow deadlocks to occur, detect them, and then recover.

##### Detection
Similar to Banker's Algorithm, but checks the current allocation state.

```c
// Deadlock detection pseudocode
void detect_deadlock() {
    int work[NUM_RESOURCES];
    bool finish[NUM_PROCESSES] = {false};
    
    // Initialize work array with available resources
    for (int i = 0; i < NUM_RESOURCES; i++) {
        work[i] = available[i];
    }
    
    // Mark processes with no allocation as finished
    for (int i = 0; i < NUM_PROCESSES; i++) {
        bool has_allocation = false;
        for (int j = 0; j < NUM_RESOURCES; j++) {
            if (allocation[i][j] > 0) {
                has_allocation = true;
                break;
            }
        }
        if (!has_allocation) {
            finish[i] = true;
        }
    }
    
    // Find processes that can complete
    bool found;
    do {
        found = false;
        for (int i = 0; i < NUM_PROCESSES; i++) {
            if (!finish[i]) {
                bool can_complete = true;
                for (int j = 0; j < NUM_RESOURCES; j++) {
                    if (request[i][j] > work[j]) {
                        can_complete = false;
                        break;
                    }
                }
                
                if (can_complete) {
                    for (int j = 0; j < NUM_RESOURCES; j++) {
                        work[j] += allocation[i][j];
                    }
                    finish[i] = true;
                    found = true;
                }
            }
        }
    } while (found);
    
    // Deadlocked processes are those that are not finished
    bool deadlock_found = false;
    printf("Deadlocked processes: ");
    for (int i = 0; i < NUM_PROCESSES; i++) {
        if (!finish[i]) {
            printf("%d ", i);
            deadlock_found = true;
        }
    }
    
    if (!deadlock_found) {
        printf("No deadlock detected\n");
    } else {
        printf("\nDeadlock detected\n");
    }
}
```

##### Recovery Methods

1. **Process Termination**:
   - Terminate all deadlocked processes
   - Terminate one process at a time until deadlock is resolved

2. **Resource Preemption**:
   - Select a victim process
   - Roll back the process and preempt its resources
   - Restart the process later

#### 4. Deadlock Ignorance (Ostrich Algorithm)

Pretend deadlocks don't exist and let users handle them (e.g., by rebooting).

- Used in many operating systems (e.g., Windows, Linux)
- Assumes deadlocks are rare enough that prevention overhead isn't justified
- User can kill deadlocked processes manually

## Memory Management Strategies

### Goals of Memory Management

1. **Process Isolation**: Protect processes from each other
2. **Automatic Allocation/Deallocation**: Allocate memory as needed by processes
3. **Support for Modular Programming**: Allow modules to be compiled separately
4. **Protection and Access Control**: Prevent unauthorized access to memory
5. **Long-term Storage**: Support for files and databases

### Memory Management Organization

#### Important Points
- CPU can directly access registers and main memory
- Protection of memory space is handled by hardware
- OS loads base and limit registers
- Memory Management Unit (MMU) maps logical to physical addresses
- OS memory is divided into three sections:
  - OS resident portion
  - User processes
  - Free memory

```
           ┌─────────────────┐
High Addr  │                 │
           │  Operating      │
           │  System         │
           │  Resident       │
           │  Portion        │
           │                 │
           ├─────────────────┤
           │                 │
           │  User           │
           │  Process        │
           │  Memory         │
           │                 │
           ├─────────────────┤
           │                 │
           │  Free           │
           │  Memory         │
           │                 │
Low Addr   └─────────────────┘
```

### Swapping

Swapping is a memory management technique where a process can be temporarily swapped out to disk to free up memory.

**Characteristics**:
- Used in systems with multiprogramming
- Executed by the dispatcher (swapper)
- High context switch time
- OS can't swap processes with pending I/O

```c
// Swapping pseudocode
void swap_out_process(process_t *proc) {
    // Check if process has pending I/O
    if (has_pending_io(proc)) {
        return; // Can't swap out with pending I/O
    }
    
    // Allocate space on disk
    disk_address = allocate_swap_space(proc->size);
    
    // Copy process memory to disk
    copy_memory_to_disk(proc->memory, disk_address, proc->size);
    
    // Update process control block
    proc->state = SWAPPED;
    proc->swap_address = disk_address;
    
    // Free physical memory
    free_memory(proc->memory, proc->size);
}

void swap_in_process(process_t *proc) {
    // Allocate physical memory
    proc->memory = allocate_memory(proc->size);
    
    // Copy process from disk to memory
    copy_disk_to_memory(proc->swap_address, proc->memory, proc->size);
    
    // Update process control block
    proc->state = READY;
    
    // Free swap space
    free_swap_space(proc->swap_address, proc->size);
}
```

### Memory Allocation

#### Contiguous Memory Allocation

Memory is allocated in a single contiguous block for each process.

##### Address Translation: Base and Limit Registers
- Base register: Contains starting physical address of the process
- Limit register: Contains length of the logical address space

```
   Logical Address Space                     Physical Address Space
┌───────────────────────┐                  ┌───────────────────────┐
│                       │                  │                       │
│                       │                  │                       │
│                       │                  │                       │
│       Logical         │  Base Register   │       Physical        │
│       Address    ────────┬────────────▶ │       Address         │
│       Space       │    │                 │       Space           │
│                   │    │                 │                       │
│                   │    │                 │                       │
│                   │    │                 │                       │
└───────────────────┼────┘                 └───────────────────────┘
                    │
                    │  Limit Register
                  ┌─┴───┐
                  │     │ ◀── Check if logical address < limit
                  └─────┘
```

```c
// Address translation with base and limit registers
physical_address_t translate_address(logical_address_t logical_addr, 
                                     process_t *proc) {
    // Check if address is within bounds
    if (logical_addr > proc->limit) {
        raise_memory_violation_exception();
        return INVALID_ADDRESS;
    }
    
    // Translate logical to physical address
    physical_address_t physical_addr = proc->base + logical_addr;
    return physical_addr;
}
```

##### Fixed Partitioning
- Memory is divided into fixed-size partitions
- Simple to implement but inflexible
- Internal fragmentation occurs when processes are smaller than their partition

```
┌─────────────────────┐
│                     │
│    OS Resident      │
│    Portion          │
│                     │
├─────────────────────┤
│                     │
│    Partition 1      │
│    (Process A)      │
│                     │
├─────────────────────┤
│                     │
│    Partition 2      │
│    (Process B)      │
│                     │
├─────────────────────┤
│                     │
│    Partition 3      │
│    (Process C)      │
│                     │
├─────────────────────┤
│                     │
│    Partition 4      │
│    (Free)           │
│                     │
└─────────────────────┘
```

##### Variable Partitioning
- Memory is allocated exactly as needed
- More efficient use of memory
- External fragmentation can occur

```
┌─────────────────────┐
│                     │
│    OS Resident      │
│    Portion          │
│                     │
├─────────────────────┤
│                     │
│    Process A        │
│    (20 MB)          │
│                     │
├─────────────────────┤
│                     │
│    Process B        │
│    (15 MB)          │
│                     │
├─────────────────────┤
│                     │
│    Free Space       │
│    (5 MB)           │
│                     │
├─────────────────────┤
│                     │
│    Process C        │
│    (35 MB)          │
│                     │
└─────────────────────┘
```

##### Dynamic Storage Allocation Problem
When using variable partitioning, the OS must decide which free memory block to allocate.

1. **First Fit**:
   - Allocate the first free block that's large enough
   - Faster but may create small unusable fragments at the beginning

2. **Best Fit**:
   - Allocate the smallest free block that's large enough
   - Minimizes wasted space but may create many tiny unusable fragments

3. **Worst Fit**:
   - Allocate the largest free block
   - Leaves larger remaining fragments that might be usable
   - Generally performs worse than first fit or best fit

```c
// First Fit implementation
void* first_fit_allocate(size_t size) {
    memory_block_t *current = free_list_head;
    
    while (current != NULL) {
        if (current->size >= size) {
            // Found a block large enough
            if (current->size > size + MINIMUM_BLOCK_SIZE) {
                // Split the block
                memory_block_t *new_block = (memory_block_t*)((char*)current + size);
                new_block->size = current->size - size - sizeof(memory_block_t);
                new_block->next = current->next;
                
                current->size = size;
                current->next = new_block;
            }
            
            // Remove from free list
            if (current == free_list_head) {
                free_list_head = current->next;
            } else {
                memory_block_t *prev = free_list_head;
                while (prev->next != current) {
                    prev = prev->next;
                }
                prev->next = current->next;
            }
            
            return (void*)((char*)current + sizeof(memory_block_t));
        }
        
        current = current->next;
    }
    
    return NULL; // No suitable block found
}
```

##### Fragmentation Issues

1. **Internal Fragmentation**:
   - Wasted space inside allocated blocks
   - Occurs when more memory is allocated than needed
   - Common in fixed partitioning

2. **External Fragmentation**:
   - Free memory exists but is fragmented into small pieces
   - Total free memory is sufficient, but not contiguous
   - Common in variable partitioning

**Remedies for External Fragmentation**:

1. **Compaction**:
   - Shuffle memory contents to place all free memory together
   - Requires relocation and can be expensive

```c
// Compaction pseudocode
void compact_memory() {
    // Sort processes by base address
    sort_processes_by_base_address();
    
    physical_address_t next_free_addr = MEMORY_START;
    
    for (each process in process_list) {
        if (process->base != next_free_addr) {
            // Move process to new location
            move_process_memory(process, next_free_addr);
            
            // Update process base address
            process->base = next_free_addr;
        }
        
        // Update next free address
        next_free_addr += process->size;
    }
    
    // Update free memory information
    free_memory_start = next_free_addr;
    free_memory_size = MEMORY_END - next_free_addr;
}
```

2. **Non-Contiguous Allocation**:
   - Allow a process to use multiple, non-adjacent memory areas
   - Implemented via paging or segmentation

#### Paging

Paging divides physical memory into fixed-size blocks called frames and logical memory into pages of the same size.

```
  Logical Address Space             Physical Address Space
┌─────────────────────┐          ┌─────────────────────┐
│                     │          │                     │
│       Page 0        │          │      Frame 3        │
│                     │          │                     │
├─────────────────────┤          ├─────────────────────┤
│                     │          │                     │
│       Page 1        │          │      Frame 1        │
│                     │          │                     │
├─────────────────────┤          ├─────────────────────┤
│                     │          │                     │
│       Page 2        │          │      Frame 7        │
│                     │          │                     │
├─────────────────────┤          ├─────────────────────┤
│                     │          │                     │
│       Page 3        │          │      Frame 2        │
│                     │          │                     │
└─────────────────────┘          └─────────────────────┘
```

- **Page Table**: Maps pages to frames
- **Page Number**: High-order bits of logical address used as index into page table
- **Page Offset**: Low-order bits indicating position within page/frame
- **Page Table Limit Register (PTLR)**: Indicates size of page table

```
    Logical Address
┌─────────────┬─────────────┐
│  Page No.   │   Offset    │
└──────┬──────┴──────┬──────┘
       │             │
       ▼             │
┌─────────────┐      │
│ Page Table  │      │
├─────────────┤      │
│ Frame No. 3 │      │
└──────┬──────┘      │
       │             │
       └─────┐       │
             ▼       ▼
        ┌─────────────┬─────────────┐
        │  Frame No.  │   Offset    │
        └─────────────┴─────────────┘
             Physical Address
```

```c
// Address translation with paging
physical_address_t translate_address(logical_address_t logical_addr, 
                                     process_t *proc) {
    // Extract page number and offset
    page_number_t page_num = logical_addr / PAGE_SIZE;
    offset_t offset = logical_addr % PAGE_SIZE;
    
    // Check if page number is valid
    if (page_num >= proc->page_table_size) {
        raise_memory_violation_exception();
        return INVALID_ADDRESS;
    }
    
    // Get frame number from page table
    frame_number_t frame_num = proc->page_table[page_num];
    
    // Calculate physical address
    physical_address_t physical_addr = (frame_num * PAGE_SIZE) + offset;
    return physical_addr;
}
```

#### Segmentation

Segmentation divides logical address space into variable-sized segments based on logical units (e.g., code, data, stack).

- **Segment Table**: Maps segments to physical memory
- **Base Register**: Starting physical address of the segment
- **Limit Register**: Length of the segment

```
    Logical Address
┌─────────────┬─────────────┐
│ Segment No. │   Offset    │
└──────┬──────┴──────┬──────┘
       │             │
       ▼             │
┌─────────────────┐  │
│ Segment Table   │  │
├────────┬────────┤  │
│ Base   │ Limit  │  │
└────┬───┴────────┘  │
     │       ▲       │
     │       │       │
     │       └───────┼──── Check if offset < limit
     │               │
     └───────┐       │
             ▼       ▼
        ┌─────────────────────┐
        │   Physical Address  │
        └─────────────────────┘
```

```c
// Address translation with segmentation
physical_address_t translate_address(logical_address_t logical_addr, 
                                     process_t *proc) {
    // Extract segment number and offset
    segment_number_t seg_num = logical_addr >> OFFSET_BITS;
    offset_t offset = logical_addr & OFFSET_MASK;
    
    // Check if segment number is valid
    if (seg_num >= proc->segment_table_size) {
        raise_memory_violation_exception();
        return INVALID_ADDRESS;
    }
    
    // Check if offset is within segment limits
    if (offset >= proc->segment_table[seg_num].limit) {
        raise_memory_violation_exception();
        return INVALID_ADDRESS;
    }
    
    // Calculate physical address
    physical_address_t physical_addr = proc->segment_table[seg_num].base + offset;
    return physical_addr;
}
```

### Why Paging Increases Context-Switch Time

Paging increases context-switch time for several reasons:

1. **TLB Flush**: The Translation Lookaside Buffer must be flushed
2. **Cache Invalidation**: Memory caches may need to be invalidated
3. **Page Table Management**: Page tables must be switched
4. **Working Set Restoration**: New process's working set must be loaded

```c
// Context switch with paging (simplified)
void context_switch_with_paging(process_t *old_proc, process_t *new_proc) {
    // Save CPU registers
    save_cpu_state(old_proc);
    
    // Flush TLB
    flush_tlb();
    
    // Switch page tables
    cr3_register = new_proc->page_table_base; // On x86, CR3 points to page table
    
    // Restore CPU registers
    restore_cpu_state(new_proc);
}
```

### Page vs Frame

- **Page**: Unit of logical memory allocation in the virtual address space of a process
- **Frame**: Unit of physical memory allocation (same size as a page)

```
   Process Virtual Memory                 Physical Memory
┌─────────────────────────┐            ┌─────────────────────────┐
│                         │            │                         │
│         Page 0          │            │        Frame 0          │
│                         │            │                         │
├─────────────────────────┤            ├─────────────────────────┤
│                         │            │                         │
│         Page 1          │            │        Frame 1          │
│                         │            │                         │
├─────────────────────────┤            ├─────────────────────────┤
│                         │            │                         │
│         Page 2          │            │        Frame 2          │
│                         │            │                         │
├─────────────────────────┤            ├─────────────────────────┤
│          ...            │            │          ...            │
└─────────────────────────┘            └─────────────────────────┘
```

The page table maps virtual pages to physical frames.

### TLB Miss

A TLB (Translation Lookaside Buffer) miss occurs when the CPU can't find a virtual-to-physical address translation in the TLB cache.

**TLB Miss Handling**:
1. CPU detects the TLB miss
2. Page table is searched for the mapping
3. If found, the mapping is loaded into the TLB
4. If not found, a page fault occurs

```
   CPU generates      Check TLB       TLB Miss        Search Page       Update TLB
   virtual address     for mapping                      Table
┌─────────────┐      ┌─────────┐     ┌─────────┐     ┌─────────┐      ┌─────────┐
│             │      │         │     │         │     │         │      │         │
│ 0x1234ABCD  │────▶│  TLB    │────▶│ MMU     │────▶│  Page   │────▶│   TLB   │
│             │      │ Cache   │     │ walks   │     │  Table  │      │ updated │
│             │      │         │     │ page    │     │         │      │         │
└─────────────┘      └─────────┘     │ table   │     └─────────┘      └─────────┘
                                     └─────────┘                           │
                                                                          ▼
                                                                    ┌─────────┐
                                                                    │         │
                                                                    │ Return  │
                                                                    │physical │
                                                                    │ address │
                                                                    └─────────┘
```

A TLB miss is different from:
- **Cache Miss**: CPU can't find data in its cache memory
- **Page Fault**: Required page is not in main memory and must be loaded from disk

## Virtual Memory Management

### Goals of Virtual Memory

- **Transparency**: Make paging and memory management invisible to processes
- **Efficiency**: Minimize overhead of memory management
- **Protection**: Prevent processes from accessing each other's memory
- **Sharing**: Allow controlled memory sharing between processes
- **Physical Organization**: Hide details of physical memory

### Virtual Memory Concept

Virtual memory creates an illusion that each process has access to a large, continuous memory space, regardless of physical memory constraints.

**Implementation**:
- Pages are loaded into memory only when needed (demand paging)
- Pages not currently needed are stored on disk (swap space)
- OS maintains mappings between virtual and physical memory

### Demand Paging

Demand paging is a strategy to load pages into memory only when they are accessed.

- **Lazy Swapper/Pager**: Loads pages only when needed
- **Page Fault**: Occurs when a program accesses a page not in physical memory

```c
// Page fault handler pseudocode
void page_fault_handler(virtual_address_t addr) {
    // Get the page number from the virtual address
    page_number_t page_num = addr / PAGE_SIZE;
    
    // Find a free frame or evict a page
    frame_number_t frame = find_free_frame();
    if (frame == NO_FREE_FRAME) {
        // No free frames, need to evict a page
        frame = page_replacement_algorithm();
        
        if (is_dirty(frame)) {
            // Write back dirty page to disk
            write_to_disk(frame);
        }
    }
    
    // Load the required page from disk
    read_from_disk(page_num, frame);
    
    // Update page table
    update_page_table(page_num, frame);
    
    // Update TLB
    update_tlb(page_num, frame);
    
    // Return to the instruction that caused the page fault
    return_to_faul
