# PasswordCracker


This purpose of this project was to crack 50 hashed passwords that had already been salted. To begin, an output file is declared and the rest of the code is placed inside this file decleration. This one is called "output.txt"

<h2> Hash Inputs </h2>
  <p>The input file for this project is a file of 50 salted passwors sperated by each line of the file. This file is named "hashes.txt." This file is read in at the start of the program. In this, each line is placed into an array named hashes. An array named hashed is also instantiated at this point with all 0s with a size of 50 elements. There will also be a file named "salt.txt" with the salt used to desguise the actual password.</p>

<h2> Dictionary Attack </h2>
  <p>To deduce the passwords, Three dictionary files are used to guess the password for each hashed value. These files are named "rockyou.txt", "passwordDatabase.txt", and "morewords.txt." When going through each of these files, the password guess on each line is stripped of the new line character and added is encoded using a salt. Lastly, it is hashed and compared to the current hash value in hashes that is trying to be cracked. Once a match is found the index of the current hash in hashed is changed from a 0 to a 1 so that this hash will not be checked again with a different text file.</p>


<h2> Brute Force </h2>
  <p>For the remaining passwords, for loops through an array of all letters, digits, and symbols was iterated through to create a list of all possible combinations of 2 characters and 3 characters. These values were used to try to match with the hashes using the same method as the text files used in the dictionary attack.</p>
  
<h2> Output </h2>
  <p>The output for the passwords is given in the "output.txt" file with the hash value given in "hashes.txt" paired up with the password found by the program. The unfound passwords were then listed after the total number of passwords found.</p>
