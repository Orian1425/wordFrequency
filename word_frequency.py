
with open ("file.txt", "w") as file:
    file.write("hello world bye world bye ok bye")


import sys
print(sys.argv)

def common_words_in_file(file_name):
        with open(file_name,"r") as file:
            data = file.read()
        data = data.lower()
        if (data.replace(" ","")).isalpha():

            words = data.split(" ")
            
            #word_list = [word.strip() for word in words]
            

            word_dic = dict()
            for word in words:
                if word in word_dic:
                    word_dic[word] += 1 
                else:
                    word_dic[word]=1

            sorted_words = (sorted(word_dic.items(), key=lambda x:x[1],reverse=True))
            
            n = sys.argv[len(sys.argv)-1]
            
            if int(n) > len(sorted_words): n = len(sorted_words)
            for i in range(int(n)):
                print(sorted_words[i])
        else:
            print("not real words")

common_words_in_file("file.txt")