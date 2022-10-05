from time import time


def typingErrors(prompt):
    global iwords       #global keyword, the variable belongs to the global scope:
    words = prompt.split()
    errors = 0
    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] ==words[i]:
                if(words[i+1]) == (iwords[i+1]) &(iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors +=1
    return errors


def typingSpeed(ipromt, stime, etime):
    global time
    global iwords

    iwords = ipromt.split()
    twords = len(iwords)
    Speed = twords / time
    return Speed


def timeElapsed(stime, etime):
    time = etime - stime
    return time

if __name__ == '__main__':
    prompt = "And now it is time to put yourself first."
    print("Type these sentence :- \t'", prompt, "'")
    input("\nPress 'Enter' when you are ready!\t")

    stime = time()
    iprompt = input()
    etime = time()

    time = round(timeElapsed(stime, etime), 2)
    Speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    print("\nTotal Time Elapsed :\t ", time, "s")
    print("\nYour average typing speed was :\t")
    print("\nWith a total of :\t ", errors, "errors")
    input("\npress 'Enter' when you are ready!\t")


    stime = time()
    iprompt = input()
    etime = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    print("\nTotal Time elapsed :\t", time, "s")
    print("\nYour average typing speed was :\t", Speed, "words /minute")
    print("\tWith a total of :\t", errors, "errors")










