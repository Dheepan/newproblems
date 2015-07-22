import csv
import sys

class OddEven:
    """ class to find the Odd even from the given file"""

    def __init__(self,filename):
        self.filename=filename
        self.all_numbers=[]
        self.output_filename="outputdata.csv"

    def process(self):
        self.process_input_csv()
        self.process_output_csv()
    
    def process_input_csv(self):
        """ Open a csv file for reading and process the data and build list with the numbers"""
        try:
            # open a csv file
            f = open(self.filename, 'rt')
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        try:
            reader = csv.reader(f)
            for row in reader:
                try:
                    row=map(int, row)
                except:
                    print "Exception Occured - All Input should be integers in the file"
                self.all_numbers.extend(row)
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        finally:
            f.close()

    
    def process_output_csv(self):
        """ Open a csv file for writing and process odd/even data"""
        try:
            # open a csv file
            f = open(self.output_filename, 'w')
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        try:
            # list comprehension for building the odd even from all numbers data
            output=[ str(x)+"-Odd\n" if x%2!=0 else str(x)+"-Even\n" for x in self.all_numbers]
            for num in output:
                f.write(num)
                    
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        finally:
            f.close()
            print "Output written to outputdata.csv file"

if __name__=="__main__":
    filename=raw_input("Enter the input filename: ")
    o=OddEven(filename)
    o.process()



