I didn't understand how the multiple layers of abstraction functioned with Mongo Engine or other ORM packages, so I decided to go a layer deeper and use PyMongo to interface directly with the MongoDB - old school style.  Figuring all this out within Flask was too much.  So I decided to continue breaking down piece by piece and I looked for examples of how to interface with MongoDB using PyMongo.

The official docs are helplful with examples.  I found a CRUD example at codehandbook.org where the link is included here for reference since I managed to get his code working after typing it in piece by piece.  I modified it slightly to get it to work with Python 3.

I also slightly modified some of the examples in https://pymongo.readthedocs.io/en/stable/ and got them to work and edit a MongoDB database successfully.

I want to build on this knowledge and rewrite the code here.  After that, I can overlay this layer with the flask routes layer to make it a true web application.

References:

https://pymongo.readthedocs.io/en/stable/

https://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/

https://www.geeksforgeeks.org/json-pretty-print-using-python/

https://stackoverflow.com/questions/30333299/pymongo-bson-convert-python-cursor-cursor-object-to-serializable-json-object

https://datagy.io/python-pretty-print-json/

https://iqcode.com/code/python/python-except-exception-as-e

https://github.com/jay3dec/CRUD_Python_MongoDb/blob/master/MongoDbCRUD.py

https://www.generacodice.com/en/articolo/240333/How-do-I-use-raw_input-in-Python-3

