# EcoBrush-DB
_SQL Database for a toothbrush company_

**Natural Language Description:** An eco-friendly wooden toothbrush company uses a relational
database for the management of its information system. Customers place orders that contain
toothbrushes made up of materials supplied by a supplier. More specifically, we are interested in the
following notions: <br> <br>
**Customers:** Each customer can be identified by their customer number. For each customer, we also
know their name and email. One customer can place zero or more orders, as a customer may have
registered but has not yet placed an order. <br> <br>
**Orders:** Each order can be identified by an order number. An order has a date and total price.
Multiple orders can be placed by a single customer. One order contains zero or more toothbrushes,
as an order can contain other products instead. <br> <br>
**Toothbrushes:** Each toothbrush is identified by a toothbrush number. A toothbrush has a model,
colour, and price. One toothbrush uses one or more materials. <br> <br>
**Materials:** Each material is identified by its material number. A material also has a name. One
material can be used in zero or more toothbrushes as the material may be currently unused. A
material may have zero or one current supplier, as we can imagine we use one supplier for each
material, and we may not currently have a supplier for a certain material. <br> <br>
**Suppliers:** Each supplier is identified by their supplier number. We also know each supplier’s name
and address. A supplier may supply zero or more materials, as one supplier may supply many
materials, or they currently do not supply any materials. <br> <br>

**UML Diagram:** <br>
![image](https://github.com/prontopablo/EcoBrush-DB/assets/55544101/718d6c34-7fed-4cf9-927a-6c19b803b72b) <br>
_(The blue box represents the name translation rules)_

**Relational Model:** <br>
**Customers** (customer_number, customer_name, customer_email) <br> <br>
**Orders** (order_number, order_date, order_total_price, customer_number, product_number)
/* having product_number is more generic than having toothbrush_number */ <br> <br>
**Toothbrushes** (toothbrush_number, toothbrush_model, toothbrush_colour, toothbrush_price) <br> <br>
**Materials** (material_number, material_name) <br> <br>
**ToothbrushesMaterials** (toothbrush_number, material_number) /* following the many-to-many
association */ <br> <br>
**Suppliers** (supplier_number, supplier_name, supplier_address) <br> <br>
Orders[customer_number] ⊆ Customers[customer_number] <br> 
ToothbrushesMaterials[toothbrush_number] ⊆ Toothbrushes[toothbrush_number] <br> 
ToothbrushesMaterials[material_number] ⊆ Materials[material_number] <br> 
/*As orders can contain products other than toothbrushes, we don’t need to constrain
product_number */ 
