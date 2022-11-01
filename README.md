<table>
    <td>
        <img src="https://i.imgur.com/L3d1zgP.png" alt="HBNB LOGO" width="200px">
    </td>
    <td>
        <h1>HBnB Command Console</h1>
        <h3>Command interface for project data manipulation</h3>
        <h4>By: Ivan Hansen & German Izquierdo</h4>
    </td>
</table>

<h2>About</h2>
<p>
    This project presents a basic command interpreter built with
    Python for object manipulation. It features a command interface,
    a class and subclass system and a basic local file storage management
    engine.
</p>

<h3>What can this command interface do?</h3>
<p>
    This interface can:
</p>
<ul>
    <li>Create a new object (ex: a new User or a new Place)</li>
    <li>Retrieve an object from a file, a database etc…</li>
    <li>Do operations on objects (count, compute stats, etc…)</li>
    <li>Update attributes of an object</li>
    <li>Destroy an object</li>
</ul>

<h2>Installation</h2>
<p>
    This project requires <strong>(at least) Python 3.8</strong> to work correctly.
</p>

<h2>Contact</h2>
<p>
    Corresponding contact info can be found in the <code>AUTHORS</code> file
</p>

<h2>Usage</h2>
<p>
    First of all, you need to run the program by calling it from the console:
</p>

```bash
python3 console.py
```

<p>
    Then, a command prompt will be shown, showing the interpreter is ready to recieve commands
</p>

```
(hbnb) 
```
<h2>Function list</h2>
<h3>Create</h3>
<p>
    This function allows the user to create an object of a specific class or subclass.
    If succesful, the function will return the associated unique identifier for the created object.
</p>
<h4>Usage: <code>create &lt;class_name&gt;</code></h4>
<h4>Example:</h4>

```
(hbnb) create BaseModel
988095cc-b604-402b-b6bf-b098c30b15fe
```
<br>
<h3>Update</h3>
<p>
    This function allows the user to update an object of a specific class or subclass.
</p>
<h4>Usage: <code>update &lt;class name&gt; &lt;id&gt; &lt;attribute&gt; "&lt;value&gt;"</code></h4>
<h4>Example:</h4>

```
(hbnb) update State 5cabdba5-ea3b-46fa-bf23-11394c9611ee name "Ohio"
```
<br>
<h3>Show</h3>
<p>
    This function allows the user to show a specific object by 
    passing its unique identifier to the interpreter.
</p>
<h4>Usage: <code>show &lt;class_name&gt; &lt;id&gt;</code></h4>
<h4>Example:</h4>

```
(hbnb) show State 5cabdba5-ea3b-46fa-bf23-11394c9611ee
[State] (5cabdba5-ea3b-46fa-bf23-11394c9611ee) {'id': '5cabdba5-ea3b-46fa-bf23-11394c9611ee', 'created_at': datetime.datetime(2022, 10, 18, 0, 10, 20, 248037), 'updated_at': datetime.datetime(2022, 10, 18, 0, 10, 20, 248046)}
```
<br>
<h3>Destroy</h3>
<p>
    This function allows the user to create an object of a specific class or subclass.
</p>
<h4>Usage: <code>destroy &lt;class_name&gt; &lt;id&gt;</code></h4>
<h4>Example:</h4>

```
(hbnb) destroy State 5cabdba5-ea3b-46fa-bf23-11394c9611ee
(hbnb) show State 5cabdba5-ea3b-46fa-bf23-11394c9611ee
** no instance found **
```
<br>
<h3>All</h3>
<p>
    This function allows the user to show all stored objects 
    from a specific class or subclass.
</p>
<h4>Usage: <code>all &lt;class_name&gt;</code></h4>
<h4>Example:</h4>

```
(hbnb) all State
["[State] (5607eb1c-6aa2-40fe-a591-a44de7908a75) {'id': '5607eb1c-6aa2-40fe-a591-a44de7908a75', 'created_at': datetime.datetime(2022, 10, 18, 0, 5, 52, 772185), 'updated_at': datetime.datetime(2022, 10, 18, 0, 5, 52, 772194)}", "[State] (6757de50-fdad-4b71-b149-cc3de3e500d2) {'id': '6757de50-fdad-4b71-b149-cc3de3e500d2', 'created_at': datetime.datetime(2022, 10, 18, 0, 20, 55, 454779), 'updated_at': datetime.datetime(2022, 10, 18, 0, 20, 55, 454787)}"]
```
