import hashlib
def p1(userInput,userInput2=None):
    def get_num_of_characters(str):
        return len(str)
    def output_without_whitespace(s):
        msg = s.replace(" ","")
        return msg
    def get_acronym(st):
        tpl = st.split(" ")
        msg = ""
        for i in tpl:
            msg+=i[0]
        return msg
    def get_safe(sg):
        return str(hashlib.sha256(sg.encode('utf8')).hexdigest())
    if userInput2 == None and userInput != None:
        print("The number of characters in the string is",str(get_num_of_characters(userInput)) 
          + "\nThe output without whitespace is",output_without_whitespace(userInput))
    elif userInput2 != None and userInput == None:
        print("The acronym is",get_acronym(userInput2) 
          + "\nThe sha256 output is",get_safe(userInput2))
