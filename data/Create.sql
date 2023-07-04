DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Toothbrushes;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS ToothbrushesMaterials;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Materials;

CREATE TABLE Customers (
   customer_number INTEGER PRIMARY KEY,
   customer_name TEXT NOT NULL,
   customer_email TEXT UNIQUE
);

CREATE TABLE Toothbrushes (
  toothbrush_number INTEGER PRIMARY KEY,
  toothbrush_model TEXT NOT NULL,
  toothbrush_colour TEXT NOT NULL,
  toothbrush_price NUMERIC(10,2) NOT NULL CHECK (toothbrush_price >= 0)
);

CREATE TABLE Orders (
  order_number INTEGER PRIMARY KEY,
  order_date DATE NOT NULL CHECK (order_date <= CURRENT_DATE),
  order_total_price NUMERIC(10,2) NOT NULL CHECK (order_total_price >= 0),
  customer_number INTEGER,
  FOREIGN KEY (customer_number) REFERENCES Customers(customer_number) ON DELETE CASCADE
);

CREATE TABLE Materials (
  material_number INTEGER PRIMARY KEY,
  material_name TEXT NOT NULL
);

CREATE TABLE ToothbrushesMaterials (
  toothbrush_number INTEGER NOT NULL,
  material_number INTEGER NOT NULL,
  PRIMARY KEY (toothbrush_number, material_number),
  FOREIGN KEY (toothbrush_number) REFERENCES Toothbrushes(toothbrush_number) ON DELETE CASCADE,
  FOREIGN KEY (material_number) REFERENCES Materials(material_number) ON DELETE CASCADE
);

CREATE TABLE Suppliers (
  supplier_number INTEGER PRIMARY KEY,
  supplier_name TEXT NOT NULL,
  supplier_address TEXT NOT NULL
);

CREATE VIEW IF NOT EXISTS ToothbrushesMaterialsSuppliers AS
  SELECT tb.toothbrush_number, tb.toothbrush_model, tb.toothbrush_colour, tb.toothbrush_price,
        GROUP_CONCAT(m.material_name, ' | ') AS material_names,
        GROUP_CONCAT(s.supplier_name, ' | ') AS supplier_names,
        GROUP_CONCAT(s.supplier_address, ' | ') AS supplier_addresses
  FROM Toothbrushes tb
  JOIN ToothbrushesMaterials tbm ON tb.toothbrush_number = tbm.toothbrush_number
  JOIN Materials m ON tbm.material_number = m.material_number
  JOIN Suppliers s ON m.material_number = s.supplier_number
  GROUP BY tb.toothbrush_number;
