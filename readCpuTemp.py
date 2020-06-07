import sys
from time import sleep
try:
    from myClasses.measureTempClass import classReadCPUTemp
except ModuleNotFoundError:
    print("************************************************************")
    print()
    print("Module not found!")
    print("Be sure that you have measureTemp.py in the myClasses folder")
    print()
    print("************************************************************")
    sys.exit(1)

readCpuTemp = classReadCPUTemp() # Make an instance of the class classReadCPUTemp

try: 
    while True:
        actualCpuTemp = readCpuTemp.func_get_cpu_temp()# Call function func_measure_cpu_temp() in classReadCPUTemp()
        print(actualCpuTemp)
        sleep(5) # Wait for five sec
except KeyboardInterrupt:
    print("Keyboard Interrupt")
