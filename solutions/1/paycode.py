import sys

class PayCode:
    """Class to calculate the pay type for a week"""
    def __init__(self):
        self.week_time=None
        self.pay_type=None
    
    def process(self,num_list):
        #sanitize intial input
        self.sanitize_data(num_list)
        
        #real calculation happens here
        self.calculate_pay_code()
        
        #print self.pay_type for debugging purpose
        #print self.pay_type

        #return weekly hours data by pay type
        return self.pay_type
    
    # basic checks and sanitize the data - convert str to int
    def sanitize_data(self,num_list):
        self.week_time=[]
        if len(num_list)!=7:
           print "Number of days should be exactly seven in the timesheet"
           sys.exit(1)
        for num in num_list:
            try:
                time=float(num)
                if time>24:
                    #"Time cannot be more than 24 hours so using 24 hours"
                    time=24
                if time<0:
                    #"Time cannot be negative so taking 0 hours"
                    time=0
                self.week_time.append(time)
            except:
                #if time is not a number add 0 hours
                self.week_time.append(0)
                
    def calculate_pay_code(self):
        self.pay_type={'regular':0,'timenhalf':0,'double':0,'total':0}
        
        #double time for saturday and sunday
        self.pay_type['double']=self.week_time[0]+self.week_time[-1]

        #calculate time for monday to friday
        for time in self.week_time[1:-1]:
            #for regular hours
            if time<=8:
                self.pay_type['regular']+=time

            #for time and half
            if time>8 and time<=12:
                self.pay_type['regular']+=8
                self.pay_type['timenhalf']+=time-8
            #for double time
            if time>12:
                self.pay_type['double']+=time-12
                self.pay_type['timenhalf']+=4
                self.pay_type['regular']+=8
        
        # calculate the total hours
        self.pay_type['total']=self.pay_type['regular']+self.pay_type['timenhalf']*1.5+self.pay_type['double']*2
        
if __name__=="__main__":
    p=PayCode()
    # basic testcases for this individual module
    p.process(['', '8', '3', '12', '8', '8', ''])
    p.process(['', '8', '7', '15', '2', '9', '4'])
    p.process(['', '-1', '25', '0', '0', '0', '0'])
