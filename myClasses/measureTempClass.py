##########################################
# Readning and returning CPU-temperature #
##########################################
import subprocess

class classReadCPUTemp:
    def __init__(self):
        """ Init the class """
        self.strToGetInfoFromShell = "vcgencmd measure_temp"
        self.strToTrimResultFromLeftIn_vcgencmd_measure_temp = "temp="
        self.strToTrimResultFromRightIn_vcgencmd_measure_temp = "'C\n"
        self.tempInFloat = 0.0
    
    def func_decode_and_trim_vcgencmd_measure_temp(self, tempMeasure):
        subprocess_return = tempMeasure.stdout.read()
        tempDecoded = subprocess_return.decode()
        tempDecodedAndStriped = tempDecoded.strip(self.strToTrimResultFromLeftIn_vcgencmd_measure_temp).rstrip(self.strToTrimResultFromRightIn_vcgencmd_measure_temp)
        self.tempInFloat = float(tempDecodedAndStriped) #Convert tempDecodedAndStriped to a float

        return self.tempInFloat
        
    
    def func_get_cpu_temp(self):
        """
            Readning and returning CPU-temperature
            Example Of Usage:
                readCpuTemp = classReadCPUTemp()
                while True:
                    actualCPUTemp = readCpuTemp.func_get_cpu_temp()
                    print(actualCPUTemp)
        """
        
        tempMeasure = subprocess.Popen(self.strToGetInfoFromShell, shell=True, stdout=subprocess.PIPE) # Reading CPU-temperature
        return self.func_decode_and_trim_vcgencmd_measure_temp(tempMeasure) # Call the func_decode_and_trim function
        



