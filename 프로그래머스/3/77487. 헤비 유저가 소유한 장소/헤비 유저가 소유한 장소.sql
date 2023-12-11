-- 코드를 입력하세요
SELECT ID, NAME, HOST_ID
FROM PLACES LEFT JOIN (
                        SELECT HOST_ID
                        FROM PLACES
                        GROUP BY 1
                        HAVING COUNT(1) >= 2) temp 
            USING(HOST_ID)
WHERE temp.HOST_ID IS NOT NULL
ORDER BY ID