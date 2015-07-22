import csv
import sys

class SpellCount:
    """ class to build the spell count from inputdata.csv"""

    def __init__(self,filename):
        self.filename=filename
        self.solution_list=[]
        self.output_filename="outputdata.csv"

    def process(self):
        self.process_input_csv()
        self.process_output_csv()
    
    def process_input_csv(self):
        """ Open a csv file for reading and process the data for spell count"""
        try:
            # open a csv file
            f = open(self.filename, 'rt')
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        try:
            reader = csv.reader(f)
            for row in reader:
                for column in row:
                    #dictionary to keep the spell count of the word
                    count_dict={} 
                    for letter in column.upper():
                        try:
                            count_dict[letter]+=1
                        except:
                            count_dict[letter]=1
                    self.solution_list.append(count_dict)

        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        finally:
            f.close()

    
    def process_output_csv(self):
        """ Open a csv file for reading and process the data for spell count"""
        try:
            # open a csv file
            f = open(self.output_filename, 'w')
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        try:
            for spell_dict in self.solution_list:
                for key,value in spell_dict.iteritems():
                    f.write(key+"-"+str(value)+"\n")
                f.write("\n\n")
        except Exception as e:
            print "Exception Occured "+str(e)
            sys.exit(1)

        finally:
            f.close()
            print "Output written to outputdata.csv file"

if __name__=="__main__":
    filename=raw_input("Enter the input filename: ")
    s=SpellCount(filename)
    s.process()



