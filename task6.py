def analyze_text_file(file_name):
    try:
        with open(file_name,"r",encoding="utf-8") as f:
            text=f.read()
            print(text)
    #character_count
        char_count=len(text)
        print("char_count: ",char_count)
    #line_count
        with open(file_name,"r",encoding="utf-8") as f:
            line_count=len(f.readlines())
            print("line_count: ",line_count)
    #word_count
        words=text.split()
        word_count=len(words)
        print("word_count: ",word_count)
    #frequency
        word_freq={}
        for word in words:
            word=word.lower().strip(".,!?\"'(){}[]:;")
            if word:
                word_freq[word] = word_freq.get(word,0)+1
                sorted_freq=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
        for word,freq in sorted_freq:
            print(f"{word}-{freq}")
    except Exception as e:
        print(e)
        
        
#get input file        
file_name=input("enter a file name: ")
analyze_text_file(file_name)