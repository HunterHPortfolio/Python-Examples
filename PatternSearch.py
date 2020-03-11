#Hunter Holcombe
#IT-140
#Final Project Four Script

import re

#Strings that will be used to search and modify using regular expressions
original_text='''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Pattern1 is using the expression \W to indicate all non-alphanumeric characters (in that range using special characters).
#The script then uses the findall function to find all occurences in lorem_ipsum.
#It then prints the number of occurrences.
pattern1 = ['\W']
results = ''

for p in pattern1:
  match = re.findall(p, lorem_ipsum)
  results = match
  print(len(results))
  
#Pattern2 is using the expression 'sit-amet|sit:amet' to indicate either 'sit-amet' or 'sit:amet' (literal and special characters).
#The script then uses the findall function to find all occurences of both in lorem_ipsum.
#It then prints the number of occurrences.
pattern2 = [r'sit-amet|sit:amet']
occurrences_sit_amet = ''

for p in pattern2:
  match = re.findall(p, lorem_ipsum)
  occurrences_sit_amet = match

print(len(occurrences_sit_amet))

#Replace_results uses the re.sub function to find all occurences of 'sit-amet' or 'sit:amet'.
#It then replaces both values with 'sit amet' in lorem_ipsum.
replace_results = re.sub('sit-amet|sit:amet',  'sit amet', lorem_ipsum) 

#Pattern3 is using the expression 'sit amet' (literal).
#The script then uses the findall function to find all occurences of 'sit amet' in replace_results.
#It then prints the number of occurrences.
pattern3 = ['sit amet']
occurrence_sit_amet = ''

for p in pattern3:
  match = re.findall(p, replace_results)
  occurrence_sit_amet = match
 
print(len(occurrence_sit_amet))



