from mrjob.job import MRJob 
import csv

# class that inherits from MRJob class 
class MRWordFrequencyCount(MRJob):
    # accepts some key (_) and value (header)...key is _ bc we never use it
    def mapper(self,_,header):
        # cvs.reader returns a reader object that will iterate over lines in cvs file
        # header = business_id, date, review_id, stars, text, type, user_id, cool, useful, funny  
        data = csv.reader([header])

        
       # what do we need to find and pass through? rating (stars) for "cool" reviews
       # stars = header[3]
       # cool = header[7]
        count = 1 
        for header in data:
            if header[7] == "cool":
                return

            # if there is a cool rating 
            if int(header[7]) != 0:  
                yield "average rating", header[3] # then return the star rating
        
        
    def reducer(self,key,ratings):
        # NEED TO FIND AVERAGE RATINGS
        all_ratings = 0
        count = 0 
        # so need: all ratings added up / # of ratings
        for rating in ratings:
            all_ratings = all_ratings + int(rating)
            count = count + 1
        average = all_ratings/count
        
        # return what will print in terminal:
        yield key, average


if __name__ == '__main__':
    MRWordFrequencyCount.run()
