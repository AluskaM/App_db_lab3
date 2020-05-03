DECLARE
    var_app_name        reviews.app_name%TYPE := 'app_name';
    var_reviews_count   reviews.reviews_count%TYPE;
    var_review_date     reviews.review_date%TYPE;
    
BEGIN

    var_review_date := TO_DATE( 'October 01, 2020', 'MONTH DD, YYYY' );
    FOR i IN 1..10 LOOP
    INSERT INTO reviews (
        app_name,
        reviews_count,
        review_date)
        VALUES (
        TRIM(var_app_name)||'_' || i,
        i * 500,
        var_review_date
    );

    END LOOP;

END;
