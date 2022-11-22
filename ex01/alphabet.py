import random
count=0

def shutudai(qa_lst):
    qa= random.sample(qa_lst["a"],10)
    pb= random.sample(qa_lst["b"],10)
    print(qa)
    print(pb)




if __name__=="__main__":
    qa_lst=[
        {"a":["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]},
        {"b":["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]},

        
    ]