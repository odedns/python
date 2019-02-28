
def is_isogram(s):
    # Your code here...
    dict = {}
    res = True
    for c in s:
        count = dict.get(c,0)
        if(count == 0):
            dict[c] =1
        else:
            res = False
            break
    return(res)


phrase = input("Enter a phrase:")
print(phrase)
print(is_isogram(phrase))
# can use list of letters and set


 