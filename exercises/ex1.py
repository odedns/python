 # -*- coding: utf-8 -*-

 

import string

 

paragraph = """The question we writers are asked most often, the favorite question, is: Why do you write?
I write because I have an innate need to write. I write because I can’t do normal work as other people do.
I write because I want to read books like the ones I write. I write because I am angry at everyone.
I write because I love sitting in a room all day writing.
I write because I can partake of real life only by changing it.
I write because I want others, the whole world, to know what sort of life we lived, and continue to live,
in Istanbul, in Turkey. I write because I love the smell of paper, pen, and ink.
I write because I believe in literature, in the art of the novel, more than I believe in anything else.
I write because it is a habit, a passion. I write because I am afraid of being forgotten.
I write because I like the glory and interest that writing brings.
Perhaps I write because I hope to understand why I am so very, very angry at everyone."""


def word_histogram(s):
    # Your code here...
    s = s.lower()
    s = s.translate(",.?:");
# can use s.strip() to remove chars.
    dict = {}


    for word in s.split():
        count = dict.get(word,0)
        count+=1
        dict[word] = count
    return dict;

print(word_histogram(paragraph))