__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'


#Write a function named n_letter_dictionary that receives a string (words separated by spaces)
#  as parameter and returns a dictionary whose keys are numbers and whose values are lists
# that contain unique words that have the number of letters equal to the keys.

# For example, when your function is called as:

# n_letter_dictionary("The way you see people is the way you treat them and the Way you treat
# them is what they become")
# Then, your function should return a dictionary such as
# {2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat']
# , 6: ['become', 'people']}


def n_letter_dictionary(S):
    SL = S.split()
    SC = []
    for i in SL:
        SC.extend([len(i)])
    SC = list(set(SC))

    D = {}
    WF = []
    for i in SC:
        W = [i]
        for k in SL:
            if len(k) == i:
                W.extend([k.lower()])
        WF += [list(set(W))]

    for i in WF:
        for k in i:
            if type(k) == int:
                i.remove(k)
                D[k] = sorted(i)
    return D
