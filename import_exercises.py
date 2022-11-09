{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "984fa140",
   "metadata": {},
   "source": [
    "# import lesson portion\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "749b9b0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from function_exercises import get_letter_grade as gg\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from math import sqrt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3f58ca6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "sqrt(25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad7aabe0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "936b1339",
   "metadata": {},
   "source": [
    "# EXERCISES START\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f54c67ec",
   "metadata": {},
   "source": [
    "# 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "293cdd1a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from function_exercises import is_vowel, calculate_tip as c_t\n",
    "\n",
    "is_vowel(\"a\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b81cef84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.25"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c_t(5,25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7fc20adf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "be9e5092",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gg(75)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b98447d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'F'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gg(25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9a6cd4fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'D'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gg(65\n",
    "   \n",
    "  )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "faee4eea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'A'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gg ( 98\n",
    "   )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cc58673f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'B'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gg(80)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7a1b768",
   "metadata": {},
   "source": [
    "# 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c0ccc702",
   "metadata": {},
   "outputs": [],
   "source": [
    "from itertools import combinations as c,permutations as p\n",
    "\n",
    "  \n",
    "list = ('a','b','c',1,2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "16536443",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a', 'b', 'c')\n",
      "('a', 'b', 1)\n",
      "('a', 'b', 2)\n",
      "('a', 'b', 3)\n",
      "('a', 'c', 1)\n",
      "('a', 'c', 2)\n",
      "('a', 'c', 3)\n",
      "('a', 1, 2)\n",
      "('a', 1, 3)\n",
      "('a', 2, 3)\n",
      "('b', 'c', 1)\n",
      "('b', 'c', 2)\n",
      "('b', 'c', 3)\n",
      "('b', 1, 2)\n",
      "('b', 1, 3)\n",
      "('b', 2, 3)\n",
      "('c', 1, 2)\n",
      "('c', 1, 3)\n",
      "('c', 2, 3)\n",
      "(1, 2, 3)\n"
     ]
    }
   ],
   "source": [
    "for x in c(list,3):\n",
    "    print(x)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a72a256",
   "metadata": {},
   "source": [
    "# b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8c836b81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a', 'b')\n",
      "('a', 'c')\n",
      "('a', 'd')\n",
      "('b', 'c')\n",
      "('b', 'd')\n",
      "('c', 'd')\n"
     ]
    }
   ],
   "source": [
    "for x in c(\"abcd\",2):\n",
    "    print(x)\n",
    "    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4516646",
   "metadata": {},
   "source": [
    "# c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "66188a6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a', 'b')\n",
      "('a', 'c')\n",
      "('a', 'd')\n",
      "('b', 'a')\n",
      "('b', 'c')\n",
      "('b', 'd')\n",
      "('c', 'a')\n",
      "('c', 'b')\n",
      "('c', 'd')\n",
      "('d', 'a')\n",
      "('d', 'b')\n",
      "('d', 'c')\n"
     ]
    }
   ],
   "source": [
    "for x in p(\"abcd\",2):\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a3cf21b",
   "metadata": {},
   "source": [
    "# 3.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "630be69a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "from io import StringIO\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdceeea0",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
