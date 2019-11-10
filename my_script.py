# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_Street View Motion-from-Structure-from-Motiontest.png')
print(encoder.get_ascii())

print("This is a Docerk test for IS601001, Windows 10, by Huan")