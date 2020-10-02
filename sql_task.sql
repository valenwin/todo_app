-- get all statuses, not repeating, alphabetically ordered
SELECT DISTINCT title, complete
FROM core_task
ORDER BY complete;

-- get the count of all tasks in each project, order by tasks count descending
SELECT cp.id, cp.title AS project_title, count(core_task.id) AS task_count
FROM core_task
INNER JOIN core_project cp on core_task.project_id = cp.id
GROUP BY cp.title
ORDER BY task_count DESC;

-- get the count of all tasks in each project, order by projects names
SELECT cp.id, cp.title, count(core_task.id) AS task_count
FROM core_task
INNER JOIN core_project cp on core_task.project_id = cp.id
GROUP BY cp.title
ORDER BY cp.title;

-- get the tasks for all projects having the name beginning with "N" letter
SELECT id, title
FROM core_task
WHERE title LIKE 'N%';

-- get the list of all projects containing the 'a' letter in the middle of the name, and show
-- the tasks count near each project. Mention that there can exist projects without tasks and tasks with project_id = NULL
SELECT core_project.title, count(ct.id) AS task_count
FROM core_project
RIGHT JOIN core_task ct on core_project.id = ct.project_id
WHERE core_project.title LIKE '%a%'
GROUP BY core_project.title;

-- get the list of tasks with duplicate names. Order alphabetically
SELECT *
FROM core_task
ORDER BY title;

-- get list of tasks having several exact matches of both name and status,
-- from the project 'Garage'. Order by matches count
SELECT cp.title AS project_title, core_task.title AS task_title
FROM core_task
RIGHT JOIN core_project cp on core_task.project_id = cp.id
WHERE cp.title = 'Garage'
GROUP BY task_title, core_task.complete
HAVING count(core_task.id) > 1
ORDER BY count(task_title);

-- get the list of project names having more than 10 tasks in status 'completed'. Order by project_id
SELECT core_project.title
FROM core_project
RIGHT JOIN core_task ct on core_project.id = ct.project_id
WHERE ct.complete = TRUE
GROUP BY core_project.id
HAVING count(ct.id) > 10
ORDER BY core_project.id;
