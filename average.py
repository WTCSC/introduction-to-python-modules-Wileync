 #imports the module where our word counter is
import text_utils 
#imports argparse so we cam have command line interaction
import argparse    


#names the function
def average_words_per_line(filename):  

# sets initial line count to 0
  count_lines = 0   
  # sets initial word count to 0
  count_words = 0   

#opens the file
  file = open(filename, 'r')    
 #tells to read the files lines
  lines = file.readlines()    
#gives a for statement that will iterate over all lines in the file
  for line in lines:     

 #adds 1 to the line count for every line it goes over
    count_lines = count_lines + 1   
    #adds a 1 to word count for every word it goes over in lines
    count_words = count_words + text_utils.count_words(line)  

#closes the file that we've opened
  file.close()
#gives am average where it divides the lines by words
  count_average = count_words // count_lines   
#returns the average words per line
  return(count_average)   

def main():
  parser = argparse.ArgumentParser(description='Count lines in a file.')
  parser.add_argument('filename', help='The file to count lines from')
  args = parser.parse_args()

  avewords = average_words_per_line(args.filename)
  print(f"Average words per line: {avewords}")

if __name__ == '__main__':
  main()



"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""