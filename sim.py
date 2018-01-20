# this is ===> version 1.2
#supports two-line loops
import sys
print("This is not fully functional yet.Only functions and other things work.")
print("Also,loops and the def function doesn't work.")
print("And for last, this thing doesn't return things.")
print("you have to set it as a variable.")
print("And not for last,modules don't work")
print("there are also exclusive functions like face(),and many more.")
print("for a complete list, type excusive_list().")
#EXCLUSIVES!!!!
def face():
    print("///H///////////////H///")
    print("///H///////////////H///")
    print("///H///////////////H///")
    print("///H///////////////H///")
    print("///H///////////////H///")
    print("///H///////////////H///")
    print("/H///////////////////H/")
    print("//H/////////////////H//")
    print("///H///////////////H///")
    print("////H/////////////H////")
    print("/////H///////////H/////")
    print("//////H////////H///////")
    print("///////H//////H////////")
    print("////////HHHHHH/////////")
def hi():
    print("////H//////H//////II////")
    print("////H//////H//////II////")
    print("////H//////H//////II////")
    print("////H//////H//////II////")
    print("////HHHHHHHH//////II////")
    print("////H//////H//////II////")
    print("////H//////H//////II////")
    print("////H//////H//////II////")
    print("////H//////H//////II////")
    print("////H//////H//////II////")
def  exclusive_list():
    print("list")
    print("1: face()")
    print("2: hi()")

print("=========================================RESTART=========================================")
print("Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32")
#initialize variables
print("Type copyright, credits ,or license() for more information.")
time=0
b=0
s=4
#main loop

while s==4:
    time=0
    time=time+1
    
    loop= False
    try:    
        a=input(">>> ")
            
        if ":" in str(a):
            loop=True
            wer=input("... ")
            what=str(a)+str(wer)
            exec(str(a)+str(wer))
            what.count('\n')
        else:
            exec(str(a))
            loop=False
    except NameError as error:
        if loop==True:
            pass
        else:
            print("Traceback (most recent call last):")
            print("File  \"<stdin>\", line "+str(time)+" , in <module>")
            time=0
            
            print("NameError:"+str(error))
    except TypeError as error:
        if loop==True:
            pass
        else:
            print("Traceback (most recent call last):")
            print("File  \"<stdin>\", line "+str(time)+" , in <module>")
            time=0
            
            print("TypeError:"+str(error))
    except ModuleNotFoundError as error:
        if loop==True:
            pass
        else:
            print("Traceback (most recent call last):")
            print("File  \"<stdin>\", line "+str(time)+" , in <module>")
            time=0
            
            print("ModuleNotFoundError:"+str(error))
    except KeyboardInterrupt as error:
        if loop==True:
            pass
        else:
            print("Traceback (most recent call last):")
            print("File  \"<stdin>\", line "+str(time)+" , in <module>")
            time=0
            
            print("KeyboardInterrupt")
            sys.exit()
    except Exception as error:
        if loop==True:
            pass
        else:
            print("Traceback (most recent call last):")
            print("File  \"<stdin>\", line "+str(time)+" , in <module>")
            time=0
            print(error)
