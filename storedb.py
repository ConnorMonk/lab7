




import sqlite3

def create(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("CREATE TABLE Store(idStore INT, SquareFeet INT, StoreType VARCHAR, LocationType CHAR, Address VARCHAR, City VARCHAR, StoreState VARCHAR, ZipCode VARCHAR)" )
    c.execute("CREATE TABLE Store_Product(ProductID INT, StoreID INT, Quantity INT)" )
    c.execute("CREATE TABLE Product(idProduct INT, Name VARCHAR, Price DECIMAL, CategoryID INT, Description VARCHAR)" )
    c.execute("CREATE TABLE Category(idCategory INT, name VARCHAR, desc VARCHAR)" )
    conn.commit()
    conn.close()
    
     
def fill(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    bg = "Baked Goods"
    bg_d = "Bread, cakes, pastries, and similar items of food that are cooked in an oven"
    fruit = "Fruits"
    fruit_d = "The sweet and fleshy product of a tree or other plant that contains seed and can be eaten as food"
    veg = "Vegetables"
    veg_d = "A plant or part of a plant used as food"
    
    # Category
    c.execute("INSERT INTO Category VALUES (0,?, ?);", (bg, bg_d))
    c.execute("INSERT INTO Category VALUES (1,?, ?);", (fruit, fruit_d))
    c.execute("INSERT INTO Category VALUES (2,?, ?);", (veg, veg_d))
    # Stores
    st1 = "Grocery", "C", "First", "Denver", "Colorado", "80808"
    st2 = "Grocery", "A", "Apple Blvd", "Colorado Springs", "Colorado", "80122"
    st3 = "Grocery", "B", "35 Bowl Rd", "Durango", "Colorado", "80005"
    c.execute("INSERT INTO Store VALUES (0, 200, ?, ?, ?, ?, ?, ?);", st1)
    c.execute("INSERT INTO Store VALUES (1, 300, ?, ?, ?, ?, ?, ?);", st2)
    c.execute("INSERT INTO Store VALUES (2, 400, ?, ?, ?, ?, ?, ?);", st3)
    # Products
    # SelectStatement0 = "SELECT Category.idCategory FROM Product JOIN Category ON Product.CategoryID=Category.rowid" 
    # SelectStatement1 = "SELECT idCategory FROM Category WHERE Name='Vegetables'"
    # SelectStatement2 = "SELECT idCategory FROM Category WHERE Name='Baked Goods'"
     
    c.execute("INSERT INTO Product VALUES (0,'Apple', 1.00, 1, 'The fruit of an apple tree')")
    c.execute("INSERT INTO Product VALUES (1,'Cabbage', 0.50, 2, 'A cultivated plant eaten as a vegetable, having thick green or purple leaves surrounding a spherical heart or head of young leaves')")
    c.execute("INSERT INTO Product VALUES (2,'Bread', 1.50, 0, 'Food made of flour, water, and yeast or another leavening agent, mixed together and baked')")
    # Store_Product
    selectSP0 = "SELECT idProduct FROM Product WHERE Name='Apple'", "SELECT idStore FROM Store WHERE City='Denver'"
    selectSP1 = "SELECT idProduct FROM Product WHERE Name='Cabbage'", "SELECT idStore FROM Store WHERE City='Colorado Springs'"
    selectSP2 = "SELECT idProduct FROM Product WHERE Name='Bread'", "SELECT idStore FROM Store WHERE City='Durango'"
    
    c.execute("SELECT Product.idProduct FROM Product JOIN Store_Product ON Store_Product.ProductID=Product.rowid")
    c.execute("UPDATE Store_Product SET Quantity=5 WHERE rowid=0")
    c.execute("UPDATE Store_Product SET Quantity=15 WHERE rowid=1")
    c.execute("UPDATE Store_Product SET Quantity=25 WHERE rowid=2")
    # c.execute("INSERT INTO Store_Product VALUES (?,?,10);", selectSP1)
    # c.execute("INSERT INTO Store_Product VALUES (?,?,15);", selectSP2    conn.close()
    
    conn.commit() 
    conn.close()

def print_tables(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    

    print ("\nTables:")
    for t in c.fetchall() :
        print ("\t[%s]"%t[0])

     ##   print ("\tColumns of", t[0])
        c.execute("PRAGMA table_info(%s);"%t[0])
        for attr in c.fetchall() :
            print ("\t\t", attr)
            
            
    c.execute("SELECT * FROM Store_Product;")
    print(c.fetchall())



if __name__ == "__main__":     
    
    thedb = create("mydb")
    fill("mydb")
    print_tables("mydb")
    