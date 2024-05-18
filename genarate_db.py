import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ClassicModels.db')
cursor = conn.cursor()

# Drop tables if they exist
tables = [
    'Payments', 'OrderDetails', 'Orders', 'Products', 'ProductLines',
    'Customers', 'Employees', 'Offices'
]
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Create Offices table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Offices (
  officeCode TEXT PRIMARY KEY,
  city TEXT NOT NULL,
  phone TEXT NOT NULL,
  addressLine1 TEXT NOT NULL,
  addressLine2 TEXT,
  state TEXT,
  country TEXT NOT NULL,
  postalCode TEXT NOT NULL,
  territory TEXT NOT NULL
)
''')

# Create Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
  employeeNumber INTEGER PRIMARY KEY,
  lastName TEXT NOT NULL,
  firstName TEXT NOT NULL,
  extension TEXT NOT NULL,
  email TEXT NOT NULL,
  reportsTo INTEGER,
  jobTitle TEXT NOT NULL,
  officeCode TEXT NOT NULL,
  FOREIGN KEY (reportsTo) REFERENCES Employees(employeeNumber),
  FOREIGN KEY (officeCode) REFERENCES Offices(officeCode)
)
''')

# Create Customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
  customerNumber INTEGER PRIMARY KEY,
  customerName TEXT NOT NULL,
  contactLastName TEXT NOT NULL,
  contactFirstName TEXT NOT NULL,
  phone TEXT NOT NULL,
  addressLine1 TEXT NOT NULL,
  addressLine2 TEXT,
  city TEXT NOT NULL,
  state TEXT,
  postalCode TEXT,
  country TEXT NOT NULL,
  salesRepEmployeeNumber INTEGER,
  creditLimit REAL,
  FOREIGN KEY (salesRepEmployeeNumber) REFERENCES Employees(employeeNumber)
)
''')

# Create ProductLines table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ProductLines (
  productLine TEXT PRIMARY KEY,
  textDescription TEXT,
  htmlDescription TEXT,
  image BLOB
)
''')

# Create Products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
  productCode TEXT PRIMARY KEY,
  productName TEXT NOT NULL,
  productScale TEXT NOT NULL,
  productVendor TEXT NOT NULL,
  productDescription TEXT NOT NULL,
  quantityInStock INTEGER NOT NULL,
  buyPrice REAL NOT NULL,
  MSRP REAL NOT NULL,
  productLine TEXT,
  FOREIGN KEY (productLine) REFERENCES ProductLines(productLine)
)
''')

# Create Orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
  orderNumber INTEGER PRIMARY KEY,
  orderDate TEXT NOT NULL,
  requiredDate TEXT NOT NULL,
  shippedDate TEXT,
  status TEXT NOT NULL,
  comments TEXT,
  customerNumber INTEGER NOT NULL,
  FOREIGN KEY (customerNumber) REFERENCES Customers(customerNumber)
)
''')

# Create OrderDetails table
cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderDetails (
  orderNumber INTEGER NOT NULL,
  productCode TEXT NOT NULL,
  quantityOrdered INTEGER NOT NULL,
  priceEach REAL NOT NULL,
  orderLineNumber INTEGER NOT NULL,
  PRIMARY KEY (productCode, orderNumber),
  FOREIGN KEY (productCode) REFERENCES Products(productCode),
  FOREIGN KEY (orderNumber) REFERENCES Orders(orderNumber)
)
''')

# Create Payments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payments (
  checkNumber TEXT PRIMARY KEY,
  paymentDate TEXT NOT NULL,
  amount REAL NOT NULL,
  customerNumber INTEGER NOT NULL,
  FOREIGN KEY (customerNumber) REFERENCES Customers(customerNumber)
)
''')
product_lines = [
    ('Classic Cars', 'Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, dream sports cars or movie-inspired miniatures, you will find great choices in this category. These replicas feature superb attention to detail and craftsmanship and offer features such as working steering system, opening forward compartment, opening rear trunk with removable spare wheel, 4-wheel independent spring suspension, and so on. The models range in size from 1:10 to 1:24 scale and include numerous limited edition and several out-of-production vehicles. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office.', None, None),
    ('Motorcycles', 'Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity.', None, None),
    ('Planes', 'Unique, diecast airplane and helicopter replicas suitable for collections, as well as home, office or classroom decorations. Models contain stunning details such as official logos and insignias, rotating jet engines and propellers, retractable wheels, and so on. Most come fully assembled and with a certificate of authenticity from their manufacturers.', None, None),
    ('Ships', 'The perfect holiday or anniversary gift for executives, clients, friends, and family. These handcrafted model ships are unique, stunning works of art that will be treasured for generations! They come fully assembled and ready for display in the home or office. We guarantee the highest quality, and best value.', None, None),
    ('Trains', "Model trains are a rewarding hobby for enthusiasts of all ages. Whether you're looking for collectible wooden trains, electric streetcars or locomotives, you'll find a number of great choices for any budget within this category. The interactive aspect of trains makes toy trains perfect for young children. The wooden train sets are ideal for children under the age of 5.", None, None),
    ('Trucks and Buses', 'The Truck and Bus models are realistic replicas of buses and specialized trucks produced from the early 1920s to present. The models range in size from 1:12 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. Materials used include tin, diecast and plastic. All models include a certificate of authenticity from their manufacturers and are a perfect ornament for the home and office.', None, None),
    ('Vintage Cars', 'Our Vintage Car models realistically portray automobiles produced from the early 1900s through the 1940s. Materials used include Bakelite, diecast, plastic and wood. Most of the replicas are in the 1:18 and 1:24 scale sizes, which provide the optimum in detail and accuracy. Prices range from $30.00 up to $180.00 for some special limited edition replicas. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office.', None, None)
]

cursor.executemany('''
INSERT INTO ProductLines (productLine, textDescription, htmlDescription, image) 
VALUES (?, ?, ?, ?)
''', product_lines)

# Insert data into Products table
products = [
    ('S10_1678','1969 Harley Davidson Ultimate Chopper','Motorcycles','1:10','Min Lin Diecast','This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.','7933','48.81','95.7'),
    ('S10_1949','1952 Alpine Renault 1300','Classic Cars','1:10','Classic Metal Creations','Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.','7305','98.58','214.3'),
    ('S10_2016','1996 Moto Guzzi 1100i','Motorcycles','1:10','Highway 66 Mini Classics','Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail, rotating wheels, working kick stand, diecast metal with plastic parts and baked enamel finish.','6625','68.99','118.94'),
    ('S10_4698','2003 Harley-Davidson Eagle Drag Bike','Motorcycles','1:10','Red Start Diecast','Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with resin parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires and rear racing slick, certificate of authenticity, detailed engine, display stand, precision diecast replica, baked enamel finish, 1:10 scale model, removable fender, seat and tank cover piece for displaying the superior detail of the v-twin engine','5582','91.02','193.66'),
    ('S10_4757','1972 Alfa Romeo GTA','Classic Cars','1:10','Motor City Art Classics','Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.','3252','85.68','136'),
    ('S10_4962','1962 Lancia Delta 16V','Classic Cars','1:10','Second Gear Diecast','Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.','6791','103.42','147.74'),
    ('S12_1099','1968 Ford Mustang','Classic Cars','1:12','Autoart Studio Design','Hood, doors and trunk all open to reveal highly detailed interior features. Steering wheel actually turns the front wheels. Color dark green.','68','95.34','194.57'),
    ('S12_1108','2001 Ferrari Enzo','Classic Cars','1:12','Second Gear Diecast','Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.','3619','95.59','207.8'),
    ('S12_1666','1958 Setra Bus','Trucks and Buses','1:12','Welly Diecast Productions','Model features 30 windows, skylights & glare resistant glass, working steering system, original logos','1579','77.9','136.67'),
    ('S12_2823','2002 Suzuki XREO','Motorcycles','1:12','Unimax Art Galleries','Official logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail, rotating wheels, working kick stand, diecast metal with plastic parts and baked enamel finish.','9997','66.27','150.62'),
    ('S12_3148','1969 Corvair Monza','Classic Cars','1:18','Welly Diecast Productions','1:18 scale die-cast about 10 inches long doors open, hood opens, trunk opens and wheels roll','6906','89.14','151.08'),
    ('S12_3380','1968 Dodge Charger','Classic Cars','1:12','Welly Diecast Productions','1:12 scale model of a 1968 Dodge Charger. Hood, doors and trunk all open to reveal highly detailed interior features. Steering wheel actually turns the front wheels. Color black','9123','75.16','117.44'),
    ('S12_3891','1969 Ford Falcon','Classic Cars','1:12','Second Gear Diecast','Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.','1049','83.05','173.02'),
    ('S12_3990','1970 Plymouth Hemi Cuda','Classic Cars','1:12','Studio M Art Models','Very detailed 1970 Plymouth Cuda model in 1:12 scale. The Cuda is generally accepted as one of the fastest original muscle cars from the 1970s. This model is a reproduction of one of the original 652 cars built in 1970. Red color.','5663','31.92','79.8'),
    ('S12_4473','1957 Chevy Pickup','Trucks and Buses','1:12','Exoto Designs','1:12 scale die-cast about 20 inches long Hood opens, Rubber wheels','6125','55.7','118.5')
]

cursor.executemany('''
INSERT INTO Products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', products)

employees = [
    (1002, 'Murphy', 'Diane', 'x5800', 'dmurphy@classicmodelcars.com', '1', None, 'President'),
    (1056, 'Patterson', 'Mary', 'x4611', 'mpatterso@classicmodelcars.com', '1', 1002, 'VP Sales'),
    (1076, 'Firrelli', 'Jeff', 'x9273', 'jfirrelli@classicmodelcars.com', '1', 1002, 'VP Marketing'),
    (1088, 'Patterson', 'William', 'x4871', 'wpatterson@classicmodelcars.com', '6', 1056, 'Sales Manager (APAC)'),
    (1102, 'Bondur', 'Gerard', 'x5408', 'gbondur@classicmodelcars.com', '4', 1056, 'Sales Manager (EMEA)'),
    (1143, 'Bow', 'Anthony', 'x5428', 'abow@classicmodelcars.com', '1', 1056, 'Sales Manager (NA)'),
    (1165, 'Jennings', 'Leslie', 'x3291', 'ljennings@classicmodelcars.com', '1', 1143, 'Sales Rep'),
    (1166, 'Thompson', 'Leslie', 'x4065', 'lthompson@classicmodelcars.com', '1', 1143, 'Sales Rep'),
    (1188, 'Firrelli', 'Julie', 'x2173', 'jfirrelli@classicmodelcars.com', '2', 1143, 'Sales Rep'),
    (1216, 'Patterson', 'Steve', 'x4334', 'spatterson@classicmodelcars.com', '2', 1143, 'Sales Rep'),
    (1286, 'Tseng', 'Foon Yue', 'x2248', 'ftseng@classicmodelcars.com', '3', 1143, 'Sales Rep'),
    (1323, 'Vanauf', 'George', 'x4102', 'gvanauf@classicmodelcars.com', '3', 1143, 'Sales Rep'),
    (1337, 'Bondur', 'Loui', 'x6493', 'lbondur@classicmodelcars.com', '4', 1102, 'Sales Rep'),
    (1370, 'Hernandez', 'Gerard', 'x2028', 'ghernande@classicmodelcars.com', '4', 1102, 'Sales Rep'),
    (1401, 'Castillo', 'Pamela', 'x2759', 'pcastillo@classicmodelcars.com', '4', 1102, 'Sales Rep'),
    (1501, 'Bott', 'Larry', 'x2311', 'lbott@classicmodelcars.com', '7', 1102, 'Sales Rep'),
    (1504, 'Jones', 'Barry', 'x102', 'bjones@classicmodelcars.com', '7', 1102, 'Sales Rep'),
    (1611, 'Fixter', 'Andy', 'x101', 'afixter@classicmodelcars.com', '6', 1088, 'Sales Rep'),
    (1612, 'Marsh', 'Peter', 'x102', 'pmarsh@classicmodelcars.com', '6', 1088, 'Sales Rep'),
    (1619, 'King', 'Tom', 'x103', 'tking@classicmodelcars.com', '6', 1088, 'Sales Rep'),
    (1621, 'Nishi', 'Mami', 'x101', 'mnishi@classicmodelcars.com', '5', 1056, 'Sales Rep'),
    (1625, 'Kato', 'Yoshimi', 'x102', 'ykato@classicmodelcars.com', '5', 1621, 'Sales Rep'),
    (1702, 'Gerard', 'Martin', 'x2312', 'mgerard@classicmodelcars.com', '4', 1102, 'Sales Rep')
]

cursor.executemany('''
INSERT INTO Employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', employees)


orders = [
    (10100, '2003-01-06 00:00:00', '2003-01-13 00:00:00', '2003-01-10 00:00:00', 'Shipped', None, 363),
    (10101, '2003-01-09 00:00:00', '2003-01-18 00:00:00', '2003-01-11 00:00:00', 'Shipped', 'Check on availability.', 128),
    (10102, '2003-01-10 00:00:00', '2003-01-18 00:00:00', '2003-01-14 00:00:00', 'Shipped', None, 181),
    (10103, '2003-01-29 00:00:00', '2003-02-07 00:00:00', '2003-02-02 00:00:00', 'Shipped', None, 121),
    (10104, '2003-01-31 00:00:00', '2003-02-09 00:00:00', '2003-02-01 00:00:00', 'Shipped', None, 141),
    (10105, '2003-02-11 00:00:00', '2003-02-21 00:00:00', '2003-02-12 00:00:00', 'Shipped', None, 145),
    (10106, '2003-02-17 00:00:00', '2003-02-24 00:00:00', '2003-02-21 00:00:00', 'Shipped', None, 278),
    (10107, '2003-02-24 00:00:00', '2003-03-03 00:00:00', '2003-02-26 00:00:00', 'Shipped', 'Difficult to negotiate with customer. We need more marketing materials', 131),
    (10108, '2003-03-03 00:00:00', '2003-03-12 00:00:00', '2003-03-08 00:00:00', 'Shipped', None, 385),
    (10109, '2003-03-10 00:00:00', '2003-03-19 00:00:00', '2003-03-11 00:00:00', 'Shipped', 'Customer requested that FedEx Ground is used for this shipping', 486),
    (10110, '2003-03-18 00:00:00', '2003-03-24 00:00:00', '2003-03-20 00:00:00', 'Shipped', None, 187),
    (10111, '2003-03-25 00:00:00', '2003-03-31 00:00:00', '2003-03-30 00:00:00', 'Shipped', None, 129),
    (10112, '2003-03-24 00:00:00', '2003-04-03 00:00:00', '2003-03-29 00:00:00', 'Shipped', 'Customer requested that ad materials (such as posters, pamphlets) be included in the shipment', 144),
    (10113, '2003-03-26 00:00:00', '2003-04-02 00:00:00', '2003-03-27 00:00:00', 'Shipped', None, 124),
    (10114, '2003-04-01 00:00:00', '2003-04-07 00:00:00', '2003-04-02 00:00:00', 'Shipped', None, 172),
    (10115, '2003-04-04 00:00:00', '2003-04-12 00:00:00', '2003-04-07 00:00:00', 'Shipped', None, 424),
    (10116, '2003-04-11 00:00:00', '2003-04-19 00:00:00', '2003-04-13 00:00:00', 'Shipped', None, 381),
    (10117, '2003-04-16 00:00:00', '2003-04-24 00:00:00', '2003-04-17 00:00:00', 'Shipped', None, 148),
    (10118, '2003-04-21 00:00:00', '2003-04-29 00:00:00', '2003-04-26 00:00:00', 'Shipped', 'Customer has worked with some of our vendors in the past and is aware of their MSRP', 216)
]

cursor.executemany('''
INSERT INTO Orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber) 
VALUES (?, ?, ?, ?, ?, ?, ?)
''', orders)

order_details = [
    (10100, 'S18_1749', 30, 136, 3),
    (10100, 'S18_2248', 50, 55.09, 2),
    (10100, 'S18_4409', 22, 75.46, 4),
    (10100, 'S24_3969', 49, 35.29, 1),
    (10101, 'S18_2325', 25, 108.06, 4),
    (10101, 'S18_2795', 26, 167.06, 1),
    (10101, 'S24_1937', 45, 32.53, 3),
    (10101, 'S24_2022', 46, 44.35, 2),
    (10102, 'S18_1342', 39, 95.55, 2),
    (10102, 'S18_1367', 41, 43.13, 1),
    (10103, 'S10_1949', 26, 214.3, 11),
    (10103, 'S10_4962', 42, 119.67, 4),
    (10103, 'S12_1666', 27, 121.64, 8),
    (10103, 'S18_1097', 35, 94.5, 10),
    (10103, 'S18_2432', 22, 58.34, 2),
    (10103, 'S18_2949', 27, 92.19, 12),
    (10103, 'S18_2957', 35, 61.84, 14),
    (10103, 'S18_3136', 25, 86.92, 13),
    (10103, 'S18_3320', 46, 86.31, 16),
    (10103, 'S18_4600', 36, 98.07, 5),
    (10103, 'S18_4668', 41, 40.75, 9),
    (10103, 'S24_2300', 36, 107.34, 1),
    (10103, 'S24_4258', 25, 88.62, 15),
    (10103, 'S32_1268', 31, 92.46, 3),
    (10103, 'S32_3522', 45, 63.35, 7),
    (10103, 'S700_2824', 42, 94.07, 6),
    (10104, 'S12_3148', 34, 131.44, 1)
]

cursor.executemany('''
INSERT INTO OrderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) 
VALUES (?, ?, ?, ?, ?)
''', order_details)

payments = [
    (103, 'HQ336336', '2004-10-19 00:00:00', 6066.78),
    (103, 'JM555205', '2003-06-05 00:00:00', 14571.44),
    (103, 'OM314933', '2004-12-18 00:00:00', 1676.14),
    (112, 'BO864823', '2004-12-17 00:00:00', 14191.12),
    (112, 'HQ55022', '2003-06-06 00:00:00', 32641.98),
    (112, 'ND748579', '2004-08-20 00:00:00', 33347.88),
    (114, 'GG31455', '2003-05-20 00:00:00', 45864.03),
    (114, 'MA765515', '2004-12-15 00:00:00', 82261.22),
    (114, 'NP603840', '2003-05-31 00:00:00', 7565.08),
    (114, 'NR27552', '2004-03-10 00:00:00', 44894.74),
    (119, 'DB933704', '2004-11-14 00:00:00', 19501.82),
    (119, 'LN373447', '2004-08-08 00:00:00', 47924.19),
    (119, 'NG94694', '2005-02-22 00:00:00', 49523.67),
    (121, 'DB889831', '2003-02-16 00:00:00', 50218.95),
    (121, 'FD317790', '2003-10-28 00:00:00', 1491.38),
    (121, 'KI831359', '2004-11-04 00:00:00', 17876.32),
    (121, 'MA302151', '2004-11-28 00:00:00', 34638.14),
    (124, 'AE215433', '2005-03-05 00:00:00', 101244.59),
    (124, 'BG255406', '2004-08-28 00:00:00', 85410.87),
    (124, 'CQ287967', '2003-04-11 00:00:00', 11044.3),
    (124, 'ET64396', '2005-04-16 00:00:00', 83598.04),
    (124, 'HI366474', '2004-12-27 00:00:00', 47142.7),
    (124, 'HR86578', '2004-11-02 00:00:00', 55639.66),
    (124, 'KI131716', '2003-08-15 00:00:00', 111654.4),
    (124, 'LF217299', '2004-03-26 00:00:00', 43369.3),
    (124, 'NT141748', '2003-11-25 00:00:00', 45084.38),
    (128, 'DI925118', '2003-01-28 00:00:00', 10549.01),
    (128, 'FA465482', '2003-10-18 00:00:00', 24101.81),
    (128, 'FH668230', '2004-03-24 00:00:00', 33820.62),
    (128, 'IP383901', '2004-11-18 00:00:00', 7466.32),
    (129, 'DM826140', '2004-12-08 00:00:00', 26248.78),
    (129, 'ID449593', '2003-12-11 00:00:00', 23923.93),
    (129, 'PI42991', '2003-04-09 00:00:00', 16537.85),
    (131, 'CL442705', '2003-03-12 00:00:00', 22292.62),
    (131, 'MA724562', '2004-12-02 00:00:00', 50025.35),
    (131, 'NB445135', '2004-09-11 00:00:00', 35321.97),
    (141, 'AU364101', '2003-07-19 00:00:00', 36251.03),
    (141, 'DB583216', '2004-11-01 00:00:00', 36140.38),
    (141, 'DL460618', '2005-05-19 00:00:00', 46895.48),
    (141, 'HJ32686', '2004-01-30 00:00:00', 59830.55),
    (141, 'ID10962', '2004-12-31 00:00:00', 116208.4)
]

cursor.executemany('''
INSERT INTO Payments (customerNumber, checkNumber, paymentDate, amount) 
VALUES (?, ?, ?, ?)
''', payments)

# Commit changes and close the connection
conn.commit()
conn.close()
