# Strings

text = "X-DSPAM-Confidence:    0.8475"

A=text.find(":")
B=text[A+5:]
C=float(B)
print(C)