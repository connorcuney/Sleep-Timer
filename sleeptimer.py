import tkinter as tk
from threading import *
import os


def setHour(val):
    global sec
    global min
    global hour
    hour = int(val)
    if sec > 0 or min > 0 or hour > 0:
        startButton.configure(state="active")
    else:
        startButton.configure(state="disabled")
    if int(val) < 10:
        hourLabel.configure(text="0"+str(val))
    else:
        hourLabel.configure(text=str(val))


def setMin(val):
    global sec
    global min
    global hour
    min = int(val)
    if sec > 0 or min > 0 or hour > 0:
        startButton.configure(state="active")
    else:
        startButton.configure(state="disabled")
    if int(val) < 10:
        minuteLabel.configure(text="0"+str(val))
    else:
        minuteLabel.configure(text=str(val))


def setSec(val):
    global sec
    global min
    global hour
    sec = int(val)
    if sec > 0 or min > 0 or hour > 0:
        startButton.configure(state="active")
    else:
        startButton.configure(state="disabled")
    if int(val) < 10:
        secondsLabel.configure(text="0"+str(val))
    else:
        secondsLabel.configure(text=str(val))


def countdown():
    global stop
    if stop is True:
        return

    hourT = int(hourLabel.cget("text"))
    minT = int(minuteLabel.cget("text"))
    secT = int(secondsLabel.cget("text"))

    secT = secT - 1
    if secT < 0:
        secondsLabel.configure(text="59")
        minT = minT - 1
        if minT < 0:
            minuteLabel.configure(text="59")
            hourT = hourT - 1
            if hourT < 0:
                pass
            elif hourT < 10:
                hourLabel.configure(text="0" + str(hourT))
            else:
                hourLabel.configure(text=str(hourT))
        elif minT < 10:
            minuteLabel.configure(text="0" + str(minT))
        else:
            minuteLabel.configure(text=str(minT))
    elif secT < 10:
        secondsLabel.configure(text="0" + str(secT))
    else:
        secondsLabel.configure(text=str(secT))

    if secT == 0 and minT == 0 and hourT == 0:
        return

    Timer(1, lambda: countdown()).start()


def isAlive(self):
    assert self.__initialized, "Thread.__init__() not called"
    return self.__started.is_set() and not self.__stopped


def onClose():
    global stop
    global timer
    timer.cancel()
    stop = True
    master.destroy()


def startTimer():
    global hour
    global min
    global sec
    global timer
    global stop
    stop = False
    overallSeconds = (hour * 60 * 60) + (min * 60) + sec
    timer = Timer(overallSeconds, lambda: shutdown())
    Timer(1, lambda: countdown()).start()
    timer.start()
    startButton.configure(state="disabled")
    stopButton.configure(state="active")
    hourSlider.configure(state="disabled")
    minuteSlider.configure(state="disabled")
    secondSlider.configure(state="disabled")


def stopTimer():
    global timer
    global stop
    timer.cancel()
    stop = True
    startButton.configure(state="active")
    stopButton.configure(state="disabled")
    hourSlider.configure(state="active")
    minuteSlider.configure(state="active")
    secondSlider.configure(state="active")
    if hour < 10:
        hourLabel.configure(text="0"+str(hour))
    else:
        hourLabel.configure(text=str(hour))
    if min < 10:
        minuteLabel.configure(text="0"+str(min))
    else:
        minuteLabel.configure(text=str(min))
    if sec < 10:
        secondsLabel.configure(text="0"+str(sec))
    else:
        secondsLabel.configure(text=str(sec))


def shutdown():
    os.system("shutdown /s /t 1")


def placeholder():
    pass


timer = Timer(0, placeholder)
stop = False
hour = 0
min = 0
sec = 0

master = tk.Tk()
master.resizable(0, 0)
master.geometry("300x150")
master.title("Sleep Timer")
master.protocol("WM_DELETE_WINDOW", onClose)

clockFrame = tk.Frame(master, width=30)
hourLabel = tk.Label(clockFrame, text="00", font=("TkDefaultFont", 20), borderwidth=2, relief="sunken")
minuteLabel = tk.Label(clockFrame, text="00", font=("TkDefaultFont", 20), borderwidth=2, relief="sunken")
secondsLabel = tk.Label(clockFrame, text="00", font=("TkDefaultFont", 20), borderwidth=2, relief="sunken")

buttonFrame = tk.Frame(clockFrame)
startButton = tk.Button(buttonFrame, text="Start", borderwidth=3, command=startTimer, state="disabled")
stopButton = tk.Button(buttonFrame, text="Stop", borderwidth=3, state="disabled", command=stopTimer)
startButton.pack(side="left", pady=5)
stopButton.pack(side="left", padx=5, pady=5)
buttonFrame.pack(side="bottom")

sliderFrame = tk.Frame(master)
hourSlider = tk.Scale(sliderFrame, from_=12, to=0, command=setHour)
minuteSlider = tk.Scale(sliderFrame, from_=59, to=0,  command=setMin)
secondSlider = tk.Scale(sliderFrame, from_=59, to=0,  command=setSec)

hourLabel.pack(side="left")
minuteLabel.pack(side="left")
secondsLabel.pack(side="left")
clockFrame.pack(side="left", padx=23)

secondSlider.pack(side="right")
minuteSlider.pack(side="right")
hourSlider.pack(side="right")
sliderFrame.pack(side="right", padx=15)


master.mainloop()
