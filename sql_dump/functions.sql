-- DROP FUNCTION sync_test.update_quantity(int4, int4);

CREATE OR REPLACE FUNCTION sync_test.update_quantity(p_id integer, number integer)
 RETURNS integer
 LANGUAGE plpgsql
AS $function$
DECLARE
    updated_rows INT;
BEGIN
    UPDATE stock_order SET order_quantity = order_quantity + number WHERE id = p_id RETURNING id INTO updated_rows;
    RETURN updated_rows;
END;
$function$
;

-- DROP FUNCTION sync_test.update_quantity_i(int4, int4);

CREATE OR REPLACE FUNCTION sync_test.update_quantity_i(i_id integer, number integer)
 RETURNS integer
 LANGUAGE plpgsql
AS $function$
DECLARE
    updated_rows INT := 0;
BEGIN
    WITH updated_rows_cte AS (
        UPDATE stock_order 
        SET order_quantity = order_quantity + number 
        WHERE item_id = i_id
        RETURNING item_id
    )
    SELECT COUNT(*) INTO updated_rows FROM updated_rows_cte;
    
    RETURN updated_rows;
END;
$function$
;