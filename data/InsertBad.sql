-- Customers table:
-- Customer with an empty name, violating NOT NULL constraint
INSERT INTO Customers (customer_number, customer_name, customer_email) VALUES (1, '', 'customer1@example.com');

-- Customer with a non-unique email, violating UNIQUE constraint
INSERT INTO Customers (customer_number, customer_name, customer_email) VALUES (2, 'Customer 2', 'customer1@example.com');



-- Orders table:
-- Order with a future order date, violating CHECK constraint
INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (1, '2023-05-05', 10.00, 1);

-- Order with a non-existent customer number, violating FOREIGN KEY constraint
INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (2, '2022-01-01', 20.00, 10);

-- Order with a negative order_total_price, violating CHECK constraint
INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (3, '2022-02-02', -5.00, 1);




-- Toothbrushes table:
-- Toothbrush with a negative price, violating CHECK constraint
INSERT INTO Toothbrushes (toothbrush_number, toothbrush_model, toothbrush_colour, toothbrush_price) VALUES (1, 'Model A', 'Red', -5.00);




-- Materials table:
-- Material with an empty name, violating NOT NULL constraint
INSERT INTO Materials (material_number, material_name) VALUES (1, '');




-- ToothbrushesMaterials table:
-- Toothbrush-material relation with a non-existent toothbrush number, violating FOREIGN KEY constraint
INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (1000, 1);

-- Toothbrush-material relation with a non-existent material number, violating FOREIGN KEY constraint
INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (1, 10);

-- Toothbrush-material relation with duplicate (toothbrush_number, material_number) values, violating PRIMARY KEY constraint
INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (1, 1);
INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (1, 1);




-- Suppliers table:
-- Supplier with an empty address, violating NOT NULL constraint
INSERT INTO Suppliers (supplier_number, supplier_name, supplier_address) VALUES (1, 'Supplier A', '');

-- Supplier with a non-integer supplier number, violating PRIMARY KEY constraint
INSERT INTO Suppliers (supplier_number, supplier_name, supplier_address) VALUES ('A', 'Supplier B', 'Address B');
