SELECT c.name AS categoria, COUNT(p.id) AS quantidade
FROM products p
JOIN categories c ON p.id_categories = c.id
GROUP BY c.name;
