<u><h>Semaphore</h></u>
<p>A semaphore is a counter with special properties. One is that the counting is atomic.
This means that there is a guarantee that the OS will not swap out the thread in the middle
of incrementing or decrementing the counter.

- The internal counter is incremented when you call `.release()` and decremented when you call
`.acquire()`. 
  
- If a thread calls`.acquire()` when the counter is zero that thread will block
until a different thread calls `.release()` and increments the counter to one.

Semaphores are frequently used to protect a resource that has limited capacity. An example
would be if you had a pool of connections and want to limit the size of that pool to a specific number.
</p>

<u><h>Timer</h></u>
<p>A threading.Timer is a way to schedule a function to be called after a 
certain amount of time has passed. You create a <b><i>Timer</i></b> by passing a number of seconds to wait
a function call:

`t = threading.Timer(30.0, my_function)`

You start the Timer by calling `.start()`. The function will be called at some point after
the time provided, but might not be at the exact time wanted.

You can cancel a Timer that you've started with `.cancel()`. It will not produce an error 
if you call it after the Timer has triggered.

An example is using this to prompt a user for action after a certain time. If the user
inputs before the Timer expires `.cancel()` will be called.
</p>

<u><h>Barrier</h></u>
<p> A threading.Barrier is used to maintain a fixed number of threads in sync. At creation
the caller must specify how many threads will be kept in sync. Each thread calls `.wait()`
on the Barrier until the specified number of threads are waiting. The barrier then releases
all threads at the same time.

At the same time is disingenuous as the OS will schedule the threads to run. They cannot 
all run at the same time.

A use for Barrier is to allow a pool of threads to initialise themselves. The threads must
wait on the Barrier before starting to guarantee all threads are initialised before operations
start.
</p>