-- :query users
SELECT *
FROM users
-- :qblock profiles
	LEFT JOIN profiles USING (user_id)
	-- :qblock login_history
		LEFT JOIN login_history USING (profile_id)
	-- :endqblock
-- :endqblock
-- :qblock user_id
WHERE user_id = $1
-- :endqblock
-- :endquery
