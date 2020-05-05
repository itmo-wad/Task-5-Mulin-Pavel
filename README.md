# Task-4-Mulin-Pavel
Task-4-Mulin-Pavel


<h1> Task 4 </h1>

<h2> Web application from Task 3, which store data in MongoDB.</h2>

<h3>Link</h3>

https://regstr-mongo.herokuapp.com/


<h3>Functions</h3>

* store user authentication info in mongo collection "users"

* implemented session storage in browsers cookies

<h3>Testing MongoDB </h3>

Here is results which illustrates how important to use indexes in collections MongoDB:

**Without indexes(time in seconds):**

* 10000 executes for 0.012665987014770508
* 100000 executes for 0.10544300079345703
* 1000000 executes for 0.7582299709320068
* 10000000 executes for 6.999218940734863

**With indexes(time in seconds):**

* 10000 executes for 0.003239870071411133
* 100000 executes for 0.002683877944946289
* 1000000 executes for 0.0028836727142333984
* 10000000 executes for 0.013992786407470703

Also results represented in graph:
![Workflow](https://raw.githubusercontent.com/itmo-wad/Task-4-Mulin-Pavel/master/Figure_1.png)
