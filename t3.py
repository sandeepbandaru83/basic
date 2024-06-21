{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9214f513-fb51-4df3-8c89-45a10767bdf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many passwords do you want to generate?  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generating 2 passwords\n",
      "Minimum length of password should be 3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the length of Password #1  5\n",
      "Enter the length of Password #2  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Password #1 = 4niqP\n",
      "Password #2 = s9nG\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def generatePassword(pwlength):\n",
    "\n",
    "    alphabet = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "\n",
    "    passwords = [] \n",
    "\n",
    "    for i in pwlength:\n",
    "        \n",
    "        password = \"\" \n",
    "        for j in range(i):\n",
    "            next_letter_index = random.randrange(len(alphabet))\n",
    "            password = password + alphabet[next_letter_index]\n",
    "        \n",
    "        password = replaceWithNumber(password)\n",
    "        password = replaceWithUppercaseLetter(password)\n",
    "        \n",
    "        passwords.append(password) \n",
    "    \n",
    "    return passwords\n",
    "\n",
    "\n",
    "def replaceWithNumber(pword):\n",
    "    for i in range(random.randrange(1,3)):\n",
    "        replace_index = random.randrange(len(pword)//2)\n",
    "        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]\n",
    "        return pword\n",
    "\n",
    "\n",
    "def replaceWithUppercaseLetter(pword):\n",
    "    for i in range(random.randrange(1,3)):\n",
    "        replace_index = random.randrange(len(pword)//2,len(pword))\n",
    "        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]\n",
    "        return pword\n",
    "\n",
    "\n",
    "\n",
    "def main():\n",
    "    \n",
    "    numPasswords = int(input(\"How many passwords do you want to generate? \"))\n",
    "    \n",
    "    print(\"Generating \" +str(numPasswords)+\" passwords\")\n",
    "    \n",
    "    passwordLengths = []\n",
    "\n",
    "    print(\"Minimum length of password should be 3\")\n",
    "\n",
    "    for i in range(numPasswords):\n",
    "        length = int(input(\"Enter the length of Password #\" + str(i+1) + \" \"))\n",
    "        if length<3:\n",
    "            length = 3\n",
    "        passwordLengths.append(length)\n",
    "    \n",
    "    \n",
    "    Password = generatePassword(passwordLengths)\n",
    "\n",
    "    for i in range(numPasswords):\n",
    "        print (\"Password #\"+str(i+1)+\" = \" + Password[i])\n",
    "\n",
    "\n",
    "\n",
    "main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9dfaf2fd-4c04-4abb-ac57-3382c09884e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
