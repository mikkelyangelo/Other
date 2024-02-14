select id_ticket, bonus_add,class, cost from ticket
where status = 'FREE' and id_flight='$id'
AND (id_ticket,class, cost) NOT IN (
    SELECT id_t, class, cost
    FROM temp_table
);