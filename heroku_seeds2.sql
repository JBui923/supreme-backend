INSERT INTO productsizes (small, medium, large, xlarge, product_id)
VALUES
    (True, True, True, True, 1),
    (True, True, True, True, 2),
    (True, True, True, True, 3),
    (True, True, True, True, 4),
    (True, True, True, True, 5),
    (True, True, True, True, 6),
    (True, True, True, True, 7),
    (True, True, True, True, 8),
    (True, True, True, True, 9),
    (True, True, True, True, 10),
    (True, True, True, True, 11),
    (True, True, True, True, 12),
    (True, True, True, True, 13),
    (True, True, True, True, 14),
    (True, True, True, True, 15),
    (True, True, True, True, 16),
    (True, True, True, True, 17),
    (True, True, True, True, 18),
    (True, True, True, True, 19),
    (True, True, True, True, 20),
    (True, True, True, True, 21),
    (True, True, True, True, 22),
    (True, True, True, True, 23),
    (True, True, True, True, 24),
    (True, True, True, True, 25),
    (True, True, True, True, 26),
    (True, True, True, True, 27),
    (True, True, True, True, 28),
    (True, True, True, True, 29),
    (True, True, True, True, 30),
    (True, True, True, True, 31),
    (True, True, True, True, 32),
    (True, True, True, True, 33),
    (True, True, True, True, 34),
    (True, True, True, True, 35),
    (True, True, True, True, 36),
    (True, True, True, True, 37),
    (True, True, True, True, 38),
    (True, True, True, True, 39),
    (True, True, True, True, 40),
    (True, True, True, True, 41),
    (True, True, True, True, 42),
    (True, True, True, True, 43),
    (True, True, True, True, 44),
    (True, True, True, True, 45),
    (True, True, True, True, 46),
    (True, True, True, True, 47),
    (True, True, True, True, 48),
    (True, True, True, True, 49),
    (True, True, True, True, 50),
    (True, True, True, True, 51),
    (True, True, True, True, 52),
    (True, True, True, True, 53),
    (True, True, True, True, 54),
    (True, True, True, True, 55),
    (True, True, True, True, 56),
    (True, True, True, True, 57),
    (True, True, True, True, 58),
    (True, True, True, True, 59),
    (True, True, True, True, 60);


INSERT INTO transactions (products, user_id, total)
VALUES
    (ARRAY[1, 25, 38], 1, 56000 ),
    (ARRAY[43, 47], 1, 110300),
    (ARRAY[51, 61], 1, 27600),
    (ARRAY[3, 27, 30, 47], 2, 56000 ),
    (ARRAY[52, 35], 2, 110300),
    (ARRAY[40, 62], 2, 27600);


INSERT INTO reviews (user_id, first_name, last_name, product_id, review_body)
VALUES
    (1, 'demo', 'user', 1, 'Pure Drip');