# Getting the second digit

Right now that you have managed to work out the number of thousands I want you to __complete the function called `numberOfHundreds` in `main.py`__.  This function should take an integer with a value less than or equal to 9999, which we shall call `N` as input.  The function should then return the second-digit of that number, i.e. if 3260 is input the function should return 2. 

Remember that a number like 3260 is constructed as follows:

1. First, multiply three by one thousand.
2. Next, multiply two by one hundred.
3. Next, multiply six by ten.
4. Next, multiply one by zero.
5. The number we are interested in is the sum of the four numbers that you obtained from these four multiplications.

Furthermore, remember also that you know how to determine the number of thousands in the number and how to use the floor operator.
