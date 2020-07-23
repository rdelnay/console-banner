compressed_alphabet = '386cc6c6fec6c600\
fcc6c6fcc6c6fc00\
3c66c0c0c0663c00\
f8ccc6c6c6ccf800\
fec0c0fcc0c0fe00\
fec0c0fcc0c0c000\
3e60c0cec6663e00\
c6c6c6fec6c6c600\
7e18181818187e00\
0606060606c67c00\
c6ccd8f0f8dcce00\
6060606060607e00\
c6eefefed6c6c600\
c6e6f6fedecec600\
7cc6c6c6c6c67c00\
fcc6c6c6fcc0c000\
7cc6c6c6decc7a00\
fcc6c6cef8dcc600\
78ccc07c06c67c00\
7e18181818181800\
c6c6c6c6c6c67c00\
c6c6c6ee7c381000\
c6c6d6fefeeec600\
c6ee7c387ceec600\
6666663c18181800\
fe0e1c3870e0fe00\
0000000000000000\
00007c067ec67e00\
c0c0fcc6c6c67c00\
00007ec0c0c07e00\
06067ec6c6c67e00\
00007cc6fec07c00\
0e187e1818181800\
00007ec6c67e067c\
c0c0fcc6c6c6c600\
1800381818187e00\
0c001c0c0c0c0c78\
c0c0cef8f8dcce00\
3818181818187e00\
0000fcb6b6b6b600\
0000fcc6c6c6c600\
00007cc6c6c67c00\
0000fcc6c6fcc0c0\
00007ec6c67e0606\
00006e7060606000\
00007cc07c06fc00\
18187e1818181800\
0000c6c6c6c67e00\
00006666663c1800\
0000b6b6b6b67e00\
0000c6fe38fec600\
0000c6c6c67e067c\
0000fe1c3870fe00'
# ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz

# messed up the character set early on so I had to add a few extra special cases
def get_position(letter,layer_number=0):
      orig_position = ord(letter)
      if orig_position == 32: # accommodate for <space> out of order of the normal ascii char set
            orig_position = 39
      elif orig_position >= 97: # accommodate for lowercase out of the normal ascii char set
            orig_position -= 5
      pos = abs(orig_position-65)*16+(layer_number*2)
      return pos

def print_letter(letter):
      letter = letter[0] # limit input the first char
      pos = get_position(letter)
      for _ in range(8): # goes through the height of the letter
            piece = compressed_alphabet[pos:pos+2] # grabs a substring (2 chars, or one lines worth) of the letters compressed form
            line = str('{0:08b}'.format(int(piece, 16))) # converts the hex to binary
            for x in line: # prints the respective symbol from the binary
                  if x == "0":
                        print('░', end='')
                  elif x == "1":
                        print('█', end='')
            print("")
            pos = pos + 2 # move the position to the next substring of 2 chars

def print_line(phrase:str,layer_number):
      for letter in phrase:
            pos = get_position(letter,layer_number)
            piece = compressed_alphabet[pos:pos+2] # grabs the 2 char string it needs based on the position
            line = str('{0:08b}'.format(int(piece, 16))) # converts the hex piece to binary
            for x in line: # prints the respective symbol from the binary
                  if x == "0":
                        print('░', end='')
                  elif x == "1":
                        print('█', end='')
      print('')

def print_phrase(phrase):
      for i in range(8):
            print_line(phrase,i)

def vert_banner(letters):
      for i in letters:
            print_letter(i)

# old version, don't use (messed up on lowercase z, something was probably misalligned somewhere)
# should probably delete tbh
def get_position_old(letter,layer_number=0):
      orig_position = ord(letter)
      if orig_position == 32:
            pos = 416
      elif orig_position >= 97:
            orig_position -= 58
            pos = (orig_position-65)*16+(layer_number*2)
      else:
            pos = (orig_position-65)*16+(layer_number*2)
      return pos

# TESTS
#print_letter(' ')
print_phrase('test')