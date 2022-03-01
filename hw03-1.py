from mrjob.job import MRJob 
import csv

# class that inherits from MRJob class 
class MRWordFrequencyCount(MRJob):
    # accepts some key (_) and value (header)...key is _ bc we never use it
    def mapper(self,_,header):
        # yield is like "return" except it doesn't exit from the fxt
        # instead it returns and keeps running the fxt to return more things
        # yield type is generator (kinda like a tuple but is saying that "idk when im done here, but you can still read me")
        
        data = csv.reader([header])
        # cvs.reader returns a reader object that will iterate over lines in cvs file

        for header in data:
            # header[4] == text, aka the review
            word = header[4].split() # split per space
            word_list = len(word)
            yield 'average words', word_list 
        
        
    def reducer(self,key,word_list):
        # takes each yield above and creates a list of values simplified by the keys
        # gives 3 outputs (chars, words, lines)

        # need to find the AVERAGE = words per(/) reviews
        words, reviews, average = 0, 0, 0 
        for text in word_list:
            words+=text
            reviews+=1
        average = words/reviews
        # return what will print in terminal: 
        yield key, average


if __name__ == '__main__':
    MRWordFrequencyCount.run()

