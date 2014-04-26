import simplegui

# define global variables
time_passed = 0
running = False
correct_stop = 0
total_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # convert time into minutes, tens_seconds, ones_seconds and tenths_seconds
    minutes = t/600
    tens_seconds = ((t/10) % 60) / 10
    ones_seconds = ((t/10) % 60) % 10
    tenths_seconds = t % 10

    return str(minutes) + ":" + str(tens_seconds) + str(ones_seconds) + "." + str(tenths_seconds)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    # starts the timer
    global running
    running = True
    timer.start()

def stop():
    # stops the timer and calculates number of stops
    global time_passed, running, correct_stop, total_stop
    if running == True:
        total_stop = total_stop + 1
        if time_passed % 10 == 0:
            correct_stop = correct_stop + 1
    running = False
    timer.stop()

def reset():
    # restarts the timer and resets counters
    global running, time_passed, correct_stop, total_stop
    running = False
    timer.stop()
    time_passed = 0
    correct_stop = 0
    total_stop = 0

# define event handler for timer with 0.1 sec interval
def time_increment():
    global time_passed
    time_passed = time_passed + 1

# define draw handler
def draw(canvas):
    canvas.draw_text( format(time_passed), [105, 150], 36, "White" )
    canvas.draw_text( str(correct_stop), [225, 50], 26, "Green" )
    canvas.draw_text( "/", [240, 50], 26, "Green" )
    canvas.draw_text( str(total_stop), [250, 50], 26, "Green" )

#create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, time_increment)
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()
