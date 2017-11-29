text = "X-DSPAM-Confidence:    0.8475"

space_pos = text.find(' ')
snum = text[space_pos:]
snum = snum.strip()
inum = float(snum)
print(inum)