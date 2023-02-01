# Optimal-Binary-Search-Tree
This is Assignment 2 of CS6013: Advanced Data Structures and Algorithms [IITH] - Optimal Binary Search Tree



-------------------------------------------------------------------
# Programming Assignment 2
### Name        : Manan Darji
### Roll Number : ************
### Subject     : Advance Data Structure and Algorithm (CS6013)
### Topic       : Optimal Binary Search Tree
-------------------------------------------------------------------

### Flow Of Code:
* So first we take user INPUT.
* We verify INPUT for 3 cases
  * **CASE-1** : Probabilities not add up to 1.
    * at end we check sum.
  * **CASE-2** : words and probabilities are distinct.
    * I Have created extra sets so we chn check same word/prob already exist.
  * **CASE-3** : words are in sorted order.
    * while looping through check current word is grater than the last word
* After which we initialize appropriate 2D Memoization Tables.
* Then we calculate cost For **Optimal BST**.
* And at the end we print Pre-Order Using One of the Mamo Table.
   
<br/>



<div style="page-break-after: always"></div>

## Few output Examples 
---
### Ex 1
```
----------------------------------------------------------------------------------

How many strings do you want to insert in the BST : 5
----------------------------------------------------------------------------------

Enter 5 strings in sorted Dictionary order along with their probabilities:
----------------------------------------------------------------------------------

Enter in pair of name and probabilities Ex. 'Banana 0.25'
----------------------------------------------------------------------------------

Enter Entry No 1 : dog 0.4
Enter Entry No 2 : and 0.2
Enter Entry No 3 : cop 0.1
Enter Entry No 4 : part 0.1
Enter Entry No 5 : speech 0.2
----------------------------------------------------------------------------------

The strings entered are not in sorted order.
The strings entered are not in sorted order.
The probabilities are not distinct.
The probabilities are not distinct.
```

### Ex 2
```
----------------------------------------------------------------------------------

How many strings do you want to insert in the BST : 3
----------------------------------------------------------------------------------

Enter 3 strings in sorted Dictionary order along with their probabilities:
----------------------------------------------------------------------------------

Enter in pair of name and probabilities Ex. 'Banana 0.25'
----------------------------------------------------------------------------------

Enter Entry No 1 : dog 0.4
Enter Entry No 2 : part 0.3
Enter Entry No 3 : speech 0.2
----------------------------------------------------------------------------------

The probabilities don’t add up to 1.
```

### Ex 3
```
----------------------------------------------------------------------------------

How many strings do you want to insert in the BST : 7
----------------------------------------------------------------------------------

Enter 7 strings in sorted Dictionary order along with their probabilities:
----------------------------------------------------------------------------------

Enter in pair of name and probabilities Ex. 'Banana 0.25'
----------------------------------------------------------------------------------

Enter Entry No 1 : a 0.22
Enter Entry No 2 : am 0.18
Enter Entry No 3 : and 0.2
Enter Entry No 4 : egg 0.05
Enter Entry No 5 : if 0.25
Enter Entry No 6 : the 0.02
Enter Entry No 7 : two 0.08
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

The minimum expected total access time is 2.1500.
----------------------------------------------------------------------------------

Pre-order traversal of the BST that provides minimum expected total access time is:
and a am if egg two the
----------------------------------------------------------------------------------

```

</br>
</br>

<center>
<h1>Thank You</h1>
</center>
