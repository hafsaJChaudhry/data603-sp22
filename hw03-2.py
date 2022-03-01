from mrjob.job import MRJob 
import csv

# class that inherits from MRJob class 
class MRWordFrequencyCount(MRJob):
    # accepts some key (_) and value (header)...key is _ bc we never use it
    def mapper(self,_,header):
        # cvs.reader returns a reader object that will iterate over lines in cvs file
        # header = business_id, date, review_id, stars, text, type, user_id, cool, useful, funny  
        data = csv.reader([header])

        
       # what do we need to find and pass through? dates and # of reviews
       # date already written year-month-date, return first 7 chars of "date"
        count = 1 
        for header in data: 
            yield header[1][:7], count
        
        
    def reducer(self,key,count):
        # return what will print in terminal: 
        yield key, sum(count)


if __name__ == '__main__':
    MRWordFrequencyCount.run()

