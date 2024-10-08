# Notes on Python 

<br>

- Reference Count in Python : As  we know that variable name reference to a memory location in a memory which has its types, data and also has a reference count. And if we change reference of the memory location for the same variable name, the past reference of the memory shoud be remove by the garbage collector if that memory location refernce not used by any other variable name.There are some ways to know the reference count for any particular memory location value.Some method for refernce count import from sys but its not work properly.

![ReferenceCOunt](../Screenshots/referenceCOunt.png)


<br>


- Describe from below code :

![ImageDes](../Screenshots/imgDes.png)

Description: first create a variable name which ref a memory location which hold a number value 7 then create another variable name which ref another memory location which hold a number value 3. Now again when we initiate a calculation in first variable name according to python internal whenever any calculation initiate if there is any variable name declare on the calculation first get the ref value from the ref memory location and then calculate or process the calculation. After the calcultion complete the result value then hold into a newly created memory location and then reference that value from the memory location to first variable name. After that if the past value from the mem loc is not in use then delete it by garbage collector(not immediately)

<br>
- Description about List :  List is mutable so the value could be change

![ListDes](../Screenshots/listDes.png)

But in Some cases like below

![ListDesSumm](../Screenshots/listDesMore.png)

We can trick to make a copy of list by useing sliceing [:]. Ya ofcourse we can also use copy by import it. like >>> import copy >>> li2 = copy.copy(li1) . We also use deepcopy to copy the inner list between a list

![ListSumm](../Screenshots/listSumm.png)

If "x == y" then it check the value of x and y are same or not, and if "x is y" then it check both x and y point to same memory reference or not

![ListSumm1](../Screenshots/list1.png)


- Oparator Overloading : If we add two string like 'mit' + 'bit', then + or oparator automatically distinguish the value whether it is string or number or anything. This featur is called oparator overloading.


- repr() : repr is a built in python function return the printable representation of specify object as string.
![Repr](../Screenshots/repr.png)

- Enumarator : Enumarator in python add a counter to an iterable returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function. 
  
    ![Enumerator](../Screenshots/enumerator.png)


- open() method: open() method actually open a file but we can do many things with it by useing some modes. there are many  modes in open() like 'w' which is stands for write mode if you write open method like this open('<file_name with extenstion>', 'w') then it will create a new file as the file_name if it was not exist befor. so we need to be causious to use 'w' mode in open() suppose if a file already exist and someone already start to modify with 'w' mode and at the same time you also trying to do so it cause some error. To prevent this we use try/catch block.
 
    ![OpenMethod1](../Screenshots/openMode1.png)

Or there is a simple way to use write mode in open method:

![OpenMethod2](../Screenshots/openMode2.png)

- **Sqlite3** : It is very easy to use sqlite in python. Its a very basic database to work with by useing python. Some of sqlite code syntex are:
    > 1.  First we must have to import the sqlite3 by: 
    <br>
        ``` import sqlite3 ```
    
    > 2. We need to connect with the database file by:
    <br>
        ``` connection = sqlite3.connection("<file_name>")```

    > 3. Create a cursor to doing all neccessary action on the db:
    <br>
        ``` cursor = connection.cursor() ```
    
    > 4. Execute all CRUD by useing the cursor onto the db:
        ``` cur.execute("SELECT * FROM videos") ```
