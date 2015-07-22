import csv
import sys
from paycode import PayCode

class PayCalc:
    """ class to calculate the pay hours as per the given timesheet csv for multiple weeks"""

    def __init__(self,filename):
        self.filename=filename
        self.paycode=PayCode()
        self.all_weeks=[]

    def process(self):
        self.process_input_csv()
        self.generate_output()
    
    def process_input_csv(self):
        """ process input from the csv file"""
        try:
            # open the input csv file
            f = open(self.filename, 'rt')
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        try:
            reader = csv.reader(f)
            next(reader, None) #skip the first line
            for row in reader: #process mutile rows in the timesheet
                pay_type=self.paycode.process(row) # obtain pay_type from the paycode module
                self.all_weeks.append(pay_type)
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        finally:
            f.close()

    
    def generate_output(self):
        """ Generate the output for one or more weeks"""
        try:
            # Process the pay type for multiple weeks and sum it together
            regulartime=0
            timenhalf=0
            doubletime=0
            totaltime=0
            for week in self.all_weeks:
                regulartime+=week['regular']
                timenhalf+=week['timenhalf'] 
                doubletime+=week['double'] 
                totaltime+=week['total'] 
            
            #generate the final output
            print "Regular time = "+str(regulartime)
            print "Time and a half = "+str(timenhalf)
            print "Double time = "+str(doubletime)
            print "Total pay hours = "+str(totaltime)
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

if __name__=="__main__":
    filename=raw_input("Enter the input filename: ")
    p=PayCalc(filename)
    p.process()



