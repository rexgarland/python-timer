#!/usr/bin/python

import sys, time, os

ERROR = "Enter an appropriate time."

def terminal_size():
    cr = struct.unpack('hh', fcntl.ioctl(os.open(os.ctermid(), os.O_RDONLY), termios.TIOCGWINSZ, '1234'))
    return int(cr[1]), int(cr[0])

def format_time(s):
    return str(s//60) + ':' + str(s%60)

def parse_time(t):
    if ':' in t:
        min = t[:t.index(':')]
        sec = t[t.index(':')+1:]
    else:
        min = t
        sec = '0'
    return valid(min, sec)

def valid(min, sec):
    try:
        a = int(min)
        b = int(sec)
        if b >= 60:
            raise
    except:
        print ERROR
        exit(0)
    return a, b

def print_time(min, sec):
    if sec<10:
        sec = '0'+str(sec)
    if min<10:
        min = '0'+str(min)
    sys.stdout.write(str(min)+':'+str(sec)+'\r')
    sys.stdout.flush()

def decrement(min, sec):
    if sec == 0:
        return min-1, 59
    else:
        return min, sec-1

def clock(min, sec):
    num = min*60 + sec
    for i in range(num):
        print_time(min, sec)
        time.sleep(1)
        min, sec = decrement(min, sec)
    t1 = time.time()
    os.system("""screen python ~/Documents/Python/Miscellaneous/flash.py """)
    t = time.time()-t1
    min = int((t-t%60)/60)
    sec = int(round(t-min*60))
    format = lambda sec: str(sec) if sec>9 else '0'+str(sec)
    print format(min)+':'+format(sec)+' late'
    exit(0)

def main():
    if len(sys.argv)==2:
        t = sys.argv[1]
        min, sec = parse_time(t)
        try:
            clock(min,sec)
            while True:
                sys.stdout.write('\a')
                sys.stdout.flush()
                time.sleep(1)
        except KeyboardInterrupt:
            print ''
    else:
        print ERROR

if __name__=='__main__':
    main()
