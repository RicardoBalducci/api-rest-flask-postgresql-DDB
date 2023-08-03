CREATE TABLE customer(
	cedula VARCHAR(70) PRIMARY KEY,
	name VARCHAR(70),
	whatsapp VARCHAR(70),
	email VARCHAR(700)
);

CREATE TABLE orders(
	quantity VARCHAR(70),
	payment_method VARCHAR(70),
	remarks VARCHAR(70),
	city VARCHAR(70),
	municipality VARCHAR(70),
	cedula VARCHAR(70),
	total VARCHAR(70),
	payment_screenshot bytea,
	status VARCHAR(70),
	delivery_amount VARCHAR(70),
	order_number VARCHAR(70) PRIMARY KEY,
	datetime DATE,
	CONSTRAINT cedula FOREIGN KEY (cedula) REFERENCES customer(cedula)
)
