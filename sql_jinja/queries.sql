-- :query users
SELECT *
FROM users
-- :block profiles
	LEFT JOIN profiles USING (user_id)
	-- :block login_history
		LEFT JOIN login_history USING (profile_id)
	-- :endblock
-- :endblock
-- :block user_id
WHERE user_id = $1
-- :endblock
-- :endquery
