1. Important of Database in real-world AI systems:

    In my understanding, databases are very important in real-world AI systems because AI applications usually need to store, manage, and retrieve large amounts of data. AI models learn from data, and they also often need to access data while making predictions or providing services to users. Without a database, it would be very difficult to organize and manage this information efficiently.
    
    TYPES OF DATA TYPICALLY STORED IN DATABASE

    For example, many AI systems store different types of data in databases such as user information (names, emails), payment record, Order id in e-commerce, images, text data etc. A recommendation system might store user profiles and past purchases, while a food delivery system may store restaurant listing,Menu etc

    IMPORTANCE OF STRUCTURED STORAGE 

    Structured storage is necessary because it keeps the data organized and easy to access. When the data is structured properly, the system can quickly search, filter, and analyze the information. This is important for training AI models and for making real-time decisions in applications like recommendation systems, fraud detection, or smart assistants.

2. MENTAL MODEL OF RELATIONAL DATABASE:

    The relational database mental model is based on organizing data into tables. Each table contains rows and columns, which makes the data easy to store and manage in a structured way.

    A table represents a collection of related information about a specific entity. 
    Columns represent the attributes or properties of that entity. For example, in a users table, the columns might include user_id, name, email, and age. 
    Rows represent individual records. Each row contains the information for one specific instance of the entity, such as one particular user.

    Each table should represent a single entity because it keeps the data organized and avoids confusion. For example, a users table should only store user information, and an orders table should only store order information. If multiple entities are mixed in one table, it can make the database harder to maintain and lead to duplicate or inconsistent data.

3. CONCEPT OF PRIMARY KEY:
     
    A primary key uniquely identifies each record in a table. This means that every row in the table must have a different value for the primary key.

    Primary keys must be unique because they are used to distinguish one record from another.Primary keys must also be non-null, meaning they cannot contain empty values, because every record must have an identifier.

    For example, in a users table, the user_id column is usually used as the primary key. Each user will have a different user_id. This helps the database quickly find, update, or delete a specific record when needed. Also primary key helps maintain the relationship between  the two table as this will be referenced as the foreign key in the other table.

4. DATABASE SCHEMA:
    A database schema is the structure or blueprint of a database. It defines how the data is organized and what rules the database must follow.

    A schema usually defines the tables in the database, the columns in each table, the data types of those columns, and the relationships between different tables. It may also define constraints such as primary keys, foreign keys, and rules that ensure data validity.

    Schemas are important because they help maintain a consistent structure for the data. When the schema is clearly defined, developers and systems know exactly how the data should be stored and accessed. This reduces errors and ensures that the database remains organized and reliable as it grows.

5. HOW RELATIONSHIP BETWEEN TABLES WORK IN RELATIONAL DATABASES

    In relational databases, relationships between tables allow different types of data to be connected. This helps avoid duplication and keeps the database well organized.

    These relationships are usually created using foreign keys. A foreign key is a column in one table that refers to the primary key in another table. This creates a link between the two tables.

    For example, there might be a users table and an orders table. The users table contains information about users, while the orders table contains information about orders placed by those users. The orders table might include a user_id column that acts as a foreign key. This user_id refers to the primary key in the users table.

    Because of this relationship, the database can identify which user placed each order. This makes it possible to retrieve related data, such as finding all the orders made by a specific user, while keeping the data organized in separate tables.