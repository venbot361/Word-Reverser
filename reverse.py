word = raw_input ("give me a word and I will  reverse it") 
i = len(word)-1
back_word = ""
while i >=0:
  back_word =  back_word+word [i]
  i= i-1

print back_word
