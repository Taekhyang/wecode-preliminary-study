def get_len_of_str(s):
    # 아래 코드를 작성해주세요.
    word = list()
    word_set = list()

    loop_count = len(s)
    count = 0
    for i in s:
      count += 1
      if i in word:
        complete_word = ''.join(word)
        word_set.append(complete_word)
        word = list()   
      word.append(i)
      
      if count == loop_count:
        complete_word = ''.join(word)
        word_set.append(complete_word)
    return len(max(word_set, key=len)) if s else 0
