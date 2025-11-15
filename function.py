def Caesar1(text:str, num:int):
    List_of_letters = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    for ch in text:
        if ch in List_of_letters:
         for i, che in enumerate (List_of_letters):
           if ch in List_of_letters:
             if ch == che:
              index_of_list = List_of_letters[(i+num)%26]
              encrypted_text += index_of_list
        else: 
             encrypted_text += ch
    return encrypted_text



            
def Caesar2(text:str, num:int):
    List_of_letters = "abcdefghijklmnopqrstuvwxyz"
    Returned_text = ""
    for ch in text:
        if ch in List_of_letters:
         for i, che in enumerate (List_of_letters):
           if ch in List_of_letters:
             if ch == che:
              index_of_list = List_of_letters[(i-num)%26]
              Returned_text += index_of_list
        else: 
             Returned_text += ch
    return Returned_text




def fence1(text:str):
   List_of_letters = "abcdefghijklmnopqrstuvwxyz"
   new_text = ""
   for ch in text:
      if ch in List_of_letters:
         new_text += ch


   text1 = ""
   text2 = ""
   for i, che in enumerate (new_text):
      if i%2 == 0:
         text1 += che
      else:
         text2 += che
   return text1 + text2




def fence2(text: str):
    n = len(text)
    result = ""
    i,j = 0,0
    if n % 2 == 0:
     first_half = text[:(n//2)]
     second_half = text[(n//2):]
    else:
     first_half = text[:(n+1)//2]
     second_half = text[(n+1)//2:]
     

    while i < len(first_half) or j < len(second_half): 
       if i < len(first_half):
            result += first_half[i]
            i += 1
       if j < len(second_half):
            result += second_half[j]
            j += 1
   
    return result





 