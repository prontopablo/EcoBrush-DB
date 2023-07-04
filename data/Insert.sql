INSERT INTO Customers (customer_number, customer_name, customer_email) VALUES (1, 'Victor Hugo', 'thehunchback@notredam.com');
INSERT INTO Customers (customer_number, customer_name, customer_email) VALUES (2, 'Jules Verne', 'journey@centreofearth.com');
INSERT INTO Customers (customer_number, customer_name, customer_email) VALUES (3, 'Albert Camus', 'thestranger@anonymous.com');


INSERT INTO Toothbrushes (toothbrush_number, toothbrush_model, toothbrush_colour, toothbrush_price) VALUES (1, 'Classic', 'Blue', 5.99);
INSERT INTO Toothbrushes (toothbrush_number, toothbrush_model, toothbrush_colour, toothbrush_price) VALUES (2, 'Eco-Friendly', 'Green', 7.99);


INSERT INTO Materials (material_number, material_name) VALUES (1, 'Bamboo');
INSERT INTO Materials (material_number, material_name) VALUES (2, 'Plastic');


INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (1, 1);
INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (1, 2);
INSERT INTO ToothbrushesMaterials (toothbrush_number, material_number) VALUES (2, 1);


INSERT INTO Suppliers (supplier_number, supplier_name, supplier_address) VALUES (1, 'Panda Bamboo Supply Co.', '10 Avenue Alsace-Lorraine');
INSERT INTO Suppliers (supplier_number, supplier_name, supplier_address) VALUES (2, 'Evil Plastic Co.', '1428 Elm St.');


INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (1, '1984-04-01', 5.99, 1);
INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (2, '1990-12-25', 15.98, 2);
INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (3, '1991-12-25', 19.97, 2);
INSERT INTO Orders (order_number, order_date, order_total_price, customer_number) VALUES (4, '1942-01-02', 7.99, 3);