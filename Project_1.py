correct = 1
miss = -1
space = -1

string1 = "IRCIGVSNRDFVEGMSGGTWVDVVLEHGGCVTVMAQDKPTVDIELVTTTVSNMAEVRSYCYEASISDMASDSRCPTQGEAYLDKQSDTQYVCKRTLVDRGWGNGCGLFGKGSLVTCAKFACSKKMTGKSIQPENLEYRIMLSVHGSQHSGMIVNDTGHETDENRAKVEITPNSPRAEATLGGFGSLGLDCEPRTGLDFSDLYYLTMNNKHWLVHKEWFHDIPLPWHAGADTGTPHWNNKEALVEFKDAHAKRQTVVVLGSQEGAVHTALAGALEAEMDGAKGRLSSGHLKCRLKMDKLRLKGVSYSLCTAAFTFTKIPAETLHGTVTVEVQYAGTDGPCKVPAQMAVDMQTLTPVGRLITANPVITESTENSKMMLELDPPFGDSYIVIGVGEKKITHHWHRSGSTIGKAFEATVRGAKRMAVLGDTAWDFGSVGGALNSLGKGIHQIFGAAFKSLFGGMSWFSQILIGTLLMWLGLNTKNGSISLMCLALGGVLIFLSTAVSA"
string2 = "SRCTHLENRDFVTGTQGTTRVTLVLELGGCVTITAEGKPSMDVWLDAIYQENPAKTREYCLHAKLSDTVAARCPTMGPATLAEEHQGGTVCKRDQSDRGWGNHCGLFGKGSIVACVKAACEAKKKATGHVYDANKIVYTVKVEPHTGDYVAANETHSGRKTASFTISSEKTILTMGEYGDVSLLCRVASGVDLAQTVILELDKTVEHLPTAWQVHRDWFNDLALPWKHEGAQNWNNAERLVEFGAPHAVKMDVYNLGDQTGVLLKALAGVPVAHIEGTKYHLKSGHVTCEVGLEKLKMKGLTYTMCDKTKFTWKRAPTDSGHDTVVMEVTFSGTKPCRIPVRAVAHGSPDVNVAMLITPNPTIENNGGGFIEMQLPPGDNIIYVGELSHQWFQK"

def zeroMatrix(row, column):
    list = []
    for x in range(row):
        list.append([])
        for y in range(column):
            list[-1].append(0)
    return list

def scoring(first, second):
    if first == second:
        return correct
    elif first == '-' or second == '-':
        return space
    else:
        return miss

def nWAlgorithm(string1, string2):
    n = len(string1)  
    m = len(string2)
    
    storeScore = zeroMatrix(m+1, n+1)
    
    for i in range(0, m + 1):
        storeScore[i][0] = space * i
    for j in range(0, n + 1):
        storeScore[0][j] = space * j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diagonal = storeScore[i - 1][j - 1] + scoring(string1[j-1], string2[i-1])
            top = storeScore[i - 1][j] + space
            left = storeScore[i][j - 1] + space
            storeScore[i][j] = max(diagonal, top, left)
    
    alignment1 = ""
    alignment2 = ""
    i = m
    j = n
    
    while i > 0 and j > 0:
        topScore = storeScore[i][j-1]
        leftScore = storeScore[i-1][j]
        diagonalScore = storeScore[i-1][j-1]
        currentScore = storeScore[i][j]

        if currentScore == topScore + space:
            alignment1 += string1[j-1]
            alignment2 += '-'
            j -= 1
        elif currentScore == leftScore + space:
            alignment1 += '-'
            alignment2 += string2[i-1]
            i -= 1
        elif currentScore == diagonalScore + scoring(string1[j-1], string2[i-1]):
            alignment1 += string1[j-1]
            alignment2 += string2[i-1]
            i -= 1
            j -= 1

    while j > 0:
        alignment1 += string1[j-1]
        alignment2 += '-'
        j -= 1
    while i > 0:
        alignment1 += '-'
        alignment2 += string2[i-1]
        i -= 1
    
    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    return(alignment1, alignment2)
def secondLine(string1, string2):
    n = len(string1)  
    m = len(string2)
    symbols =''
    alignment1, alignment2 = nWAlgorithm(string1, string2)
    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    for i in range (0, max(n+1, m+1)):
        if alignment1[i] == alignment2[i]:
            symbols += '|'
        elif ((alignment1[i] == '-' and alignment2 != '-') or (alignment1[i] != '-' and alignment2 == '-')):
            symbols += ' '
        else:
            symbols += '*'
    return symbols

output1, output2 = nWAlgorithm(string1, string2)
symbol = secondLine(string1, string2)
print(output1)
print(symbol)
print(output2)