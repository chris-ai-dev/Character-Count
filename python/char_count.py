def char_count(str):
  # Your code here
  #create empty dict/ob
  tracker = {}
  list_tracker = []
  
  #iterate through tracker to append letter to tracker
  for character in str:
    # tracker['a'] += 1
    # #check if character is None/undefined meaning it doesn't exist
    if character == " ":
      continue
    if tracker.get(character) == None:
      tracker[character] = 1
    else:
      tracker[character] += 1
  #turn into list format 
  for key, value in tracker.items():
    temp = [key,value]
    list_tracker.append(temp)    
  list_tracker.sort()    
  return list_tracker
  
  
  
  
print(char_count("an apple a day will keep the doctor away"))