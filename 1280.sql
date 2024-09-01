/*
1. with as 是instant view, with t1 as (), t2 as()...() 然後直接接著select
難搞的可以用這個方法拆開搞
2. CASE WHEN COUNT IS NOT NULL THEN COUNT ELSE 0 END
用來+column value，如果null就+0
3. 看好left join的條件，只拼id是不夠的，因爲subject name會散開
*/

WITH cte1 AS
    (SELECT *
     FROM students
     CROSS JOIN subjects),
     cte2 AS
    (SELECT student_id,
            subject_name,
            Count(subject_name) AS COUNT
     FROM examinations GROUP  BY student_id,
                                 subject_name)
SELECT cte1.student_id,
       cte1.student_name,
       cte1.subject_name,
       CASE
           WHEN COUNT IS NOT NULL THEN COUNT
           ELSE 0
       END AS attended_exams
FROM cte1
LEFT JOIN cte2 ON cte1.student_id = cte2.student_id
AND cte1.subject_name = cte2.subject_name
ORDER  BY cte1.student_id,
          cte1.subject_name;
