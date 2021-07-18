from collections import Counter

def main():
	
	start, until = 183564,657474
	total_different_passwords = 0

	for password in range(start, until):
	  text = str(password)
	  is_same = False

	  #Kondisi Mempunyai Dua Digit yang sama atau lebih
	  for x in range(5):
	    if text[x] == text[x+1]:
	      is_same = True


	  #Kondisi Never Decrease dari kiri ke kanan 
	  is_increase = True
	  for x in range(5):
	    if text[x] > text[x+1]:
	      is_increase = False

      #Kondisi Mengecek apakah range mempunyai dua digit yang sama atau lebih dan mengalamai peningkatan dari kiri ke kanan
	  if is_same and is_increase: 
	    total_different_passwords += 1

	print(total_different_passwords)
	


if __name__ == "__main__":
    main()


