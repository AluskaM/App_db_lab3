DECLARE
    var_id              reviews.id%TYPE;
    var_app_name        reviews.app_name%TYPE := 'app_name';
    var_reviews_count   reviews.reviews_count%TYPE;

    
BEGIN

    
    FOR i IN 1..10 LOOP
    INSERT INTO reviews (
        id,
        app_name,
        reviews_count
      )
        VALUES (
        i,
        TRIM(var_app_name)||'_' || i,
        i * 500
    );

    END LOOP;

END;

select * from Reviews
