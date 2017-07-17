# Sentence generation 
This program  will generates random English paragraphs. The generated text should follow the statistical properties of input text. One way to accomplish this is a technique called Markov chain algorithm. If we imagine the input as a sequence of overlapping phrases, the algorithm divides each phrase into two parts, a multi-word prefix (containing P words) and a single suffix word that follows the prefix. A Markov chain algorithm emits output phrases by randomly choosing the suffix that follows the prefix, according to the statistics of the prefix and conditional probabilities of suffix.

Program will read files containing English paragraphs, one paragraph per line. The files are in a directory and the directory will be specified on the command line. Two positive integers P, specifying the desired prefix length, and N, specifying the desired number of randomly generated paragraph, will also be entered in the command line.

  >sentenceGenerator.py input_directory_name P N
  
Sample input text:

  >Show your flowcharts and conceal your tables and I will be mystified.
  
  >Show your tables and your flowcharts will be obvious.

Sample output with prefix length P = 2 and number of output paragraphs N = 2
  
   >show your flowcharts will be mystified.
   
   >show your tables and i will be mystified.
