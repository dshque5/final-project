SELECT c.login, COUNT(o.id)
FROM "Couriers" AS c 
JOIN "Orders" AS o ON c.id=o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;