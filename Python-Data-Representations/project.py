
__author__ = "aliyyousuf@gmail.com"

IDENTICAL = -1

# Problem 01:

def lensame(line1, line2):

    """This function is applied both the strings has the equal length"""

    if len(line1) == len(line2):
        for ind in range(0, len(line1)):
            if line1[ind] != line2[ind]:
                return ind
                break
    return IDENTICAL



def singleline_diff(line1, line2):

    """
        Inputs:
          line1 - first single line string
          line2 - second single line string
        Output:
          Returns the index where the first difference between
          line1 and line2 occurs.

          Returns IDENTICAL if the two lines are the same.
        """

    if len(line1) == len(line2):
        return lensame(line1, line2)
    elif len(line1) > len(line2):
        line1 = line1[:len(line2)]
        if lensame(line1, line2) == -1:
            return len(line2)
        else:
            return lensame(line1, line2)
    else:
        line2 = line2[:len(line1)]
        if lensame(line2, line1) == -1:
            return len(line1)
        else:
            return lensame(line2, line1)





# second problem:

def singleline_diff_format(line1, line2, idx):
    """  Inputs:
         line1 - first single line string
         line2 - second single line string
         idx   - index of first difference between the lines
       Output:
         Returns a three line formatted string showing the location
         of the first difference between line1 and line2.

         If either input line contains a newline or carriage return,
         then returns an empty string.

         If idx is not a valid index, then returns an empty string.
       """



    if "\n" in line1 or "\n" in line2:
        return ""
    elif idx < 0:
        return ""

    elif "\r" in line1 or "\r" in line2:
        return ""

    elif len(line1) > len(line2):
        if idx > len(line2):
            return ""
        else:
            return line1 + '\n' + "=" * idx + "^" + '\n' + line2 + '\n'

    elif len(line1) < len(line2):
        if idx > len(line1):
            return ""
        else:
            return line1 + '\n' + "=" * idx + "^" + '\n' + line2 + '\n'
    elif len(line1) == len(line2):
        if idx > len(line1):
            return ""
        else:
            return line1 + '\n' + "=" * idx + "^" + '\n' + line2 + '\n'
    else:
        return line1 + '\n' + "=" * idx + "^" + '\n' + line2 + '\n'



# Third problem:

def temporary(list1, list2):

    """This function works as the base of the problem three:"""

    L = []
    for w1, w2 in zip(list1, list2):
        if len(w1) == len(w2):
            if w1 == w2:
                L.append((IDENTICAL, IDENTICAL))
            else:
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        L.append((list1.index(w1), list1[list1.index(w1)].index(c1)))
                        break
        elif len(w1) > len(w2):
            if w1[:len(w2)] == w2:
                L.append((list1.index(w1), len(w2)))
            else:
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        L.append((list1.index(w1), list1[list1.index(w1)].index(c1)))
                        break
        else:
            # len(w1) < len(w2)
            if w2[:len(w1)] == w1:
                L.append((list2.index(w2), len(w1)))
            else:
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        L.append((list2.index(w2), list2[list2.index(w2)].index(c2)))
                        break

    for i in L:
        if i == (-1, -1):
            L.remove(i)
        else:
            pass
    if len(L) == 0:
        return IDENTICAL, IDENTICAL
    else:
        return L[0]


def multiline_diff(list1, list2):
    """
        Inputs:
          lines1 - list of single line strings
          lines2 - list of single line strings
        Output:
          Returns a tuple containing the line number (starting from 0) and
          the index in that line where the first difference between lines1
          and lines2 occurs.

          Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
        """
    if len(list1) > len(list2):
        if temporary(list1, list2) == (-1, -1):
            return len(list2), 0
        else:
            return temporary(list1, list2)
    elif len(list1) < len(list2):
        if temporary(list1, list2) == (-1, -1):
            return len(list1), 0
        else:
            return temporary(list1, list2)
    else:
        return temporary(list1, list2)



# Fourth Problem:

def get_file_lines(filename):
    """
      Inputs:
        filename - name of file to read
      Output:
        Returns a list of lines from the file named filename.  Each
        line will be a single line string with no newline ('\n') or
        return ('\r') characters.

        If the file does not exist or is not readable, then the
        behavior of this function is undefined.
      """
    f = open(filename, 'r')
    L = []

    for line in f.readlines():
        L.append(line.replace("\n", ""))
    f.close()
    return L


def temporary2(list1, list2):
    """this function is a helper function for last problem"""
    L = []
    for w1, w2 in zip(list1, list2):
        if len(w1) == len(w2):
            if w1 == w2:
                L.append((IDENTICAL, IDENTICAL))
            else:
                for ind1 in range(0, len(w2)):
                    if w1[ind1] != w2[ind1]:
                        L.append((list1.index(w1), ind1))
                        break
        elif len(w1) > len(w2):
            if w1[:len(w2)] == w2:
                L.append((list1.index(w1), len(w2)))
            else:
                for ind in range(0, len(w2)):
                    if w1[ind] != w2[ind]:
                        L.append((list1.index(w1), ind))
                        break
        elif len(w1) < len(w2):
            # len(w1) < len(w2)
            if w2[:len(w1)] == w1:
                L.append((list2.index(w2), len(w1)))
            else:
                for ind in range(0, len(w1)):
                    if w1[ind] != w2[ind]:
                        L.append((list2.index(w2), ind))
                        break
    for i in L:
        if i == (-1, -1):
            L.remove(i)
        else:
            pass

    if len(L) == 0:
        return IDENTICAL, IDENTICAL
    else:
        return L[0]


def multiline_diff_v2(list1, list2):
    """Slightly modified function"""
    if len(list1) > len(list2):
        if temporary2(list1, list2) == (-1, -1):
            return len(list2), 0
        else:
            return temporary2(list1, list2)
    elif len(list1) < len(list2):
        if temporary2(list1, list2) == (-1, -1):
            return len(list1), 0
        else:
            return temporary2(list1, list2)
    else:
        return temporary2(list1, list2)


# Fifth problem:

def file_diff_format(file1, file2):

    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    F1_L = get_file_lines(file1)
    F2_L = get_file_lines(file2)

    if len(F1_L) == 1 and len(F2_L) == 0:
        return whenzero(F1_L, F2_L)
    elif len(F1_L) == 0 and len(F2_L) == 1:
        return whenzero(F1_L, F2_L)

    line_no, mismatch_idx = multiline_diff_v2(F1_L, F2_L)

    if line_no == -1 and mismatch_idx == -1:
        return "No differences\n"
    else:
        return ("Line " + str(line_no) + ":" + "\n" + F1_L[line_no] + "\n" + mismatch_idx * "=" + "^" + "\n" + F2_L[
            line_no] + "\n")



def whenzero(list1, list2):


    """When one file contains nothing, but another file has strings"""

    if len(list1) == 1 and len(list2) == 0:
        return "Line " + "0" + ":" + '\n' + list1[0] + '\n^\n\n'
    elif len(list1) == 0 and len(list2) == 1:
        return "Line " + "0" + ":" + '\n' + list2[0] + '\n^\n\n'


#print(file_diff_format("file8.txt","file9.txt"))