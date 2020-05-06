CREATE OR REPLACE VIEW Apps AS
SELECT app_name, 
category_name,
audience_type,
price,
reviews_count,
review_date
FROM App JOIN Reviews 
ON App.app_name=Reviews.app_name;
