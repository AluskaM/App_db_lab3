CREATE TABLE Category(
    category_name VARCHAR2(20) NOT NULL);
ALTER TABLE Category
    ADD CONSTRAINT category_name_pk PRIMARY KEY(category_name);    
    
CREATE TABLE Audience(
    audience_type VARCHAR2(20) NOT NULL);
ALTER TABLE Audience
    ADD CONSTRAINT  audience_type_pk PRIMARY KEY( audience_type);
    
CREATE TABLE App(
    id INTEGER NOT NULL,
    app_name VARCHAR2(50) NOT NULL,
    category_name VARCHAR2(20) NOT NULL,
    audience_type VARCHAR2(20) NOT NULL,
    price NUMBER NOT NULL);
ALTER TABLE App
    ADD CONSTRAINT id_pk PRIMARY KEY(id); 

CREATE TABLE Reviews(
    review_date date,
    app_name VARCHAR2(50) NOT NULL,
    reviews_count INT NOT NULL);
ALTER TABLE Reviews
    ADD CONSTRAINT  reviews_reviews_count_pk PRIMARY KEY( reviews_count);
    
ALTER TABLE App
    ADD CONSTRAINT id_fk FOREIGN KEY(id) REFERENCES App(id); 
ALTER TABLE App
    ADD CONSTRAINT category_name_fk FOREIGN KEY(category_name) REFERENCES Category(category_name);
ALTER TABLE App
    ADD CONSTRAINT audience_type_fk FOREIGN KEY(audience_type) REFERENCES Audience(audience_type);
