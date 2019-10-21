from pypika import (
	PostgreSQLQuery as Query,
	Table,
)
from pypika.terms import Term
from pypika.functions import Function, Coalesce

rp = Table('role_permissions')
pp = Table('page_permissions')

bit_or = Function('bit_or', 'col')

entity_id = 123
role_ids = [4, 5, 6]
default_permissions = 16384

"""SQL version:
WITH everyone_perms AS (SELECT permissions FROM role_permissions WHERE entity = ($2::BIGINT[])[1]),
all_permissions AS (
		SELECT
			permissions,
			0 AS allow,
			0 AS deny
		FROM role_permissions
		WHERE entity = ANY ($2)
	UNION ALL
		SELECT
			0 AS permissions,
			allow,
			deny
		FROM page_permissions
		WHERE entity = ANY ($2) OR page_id = $1)
SELECT bit_or(permissions) | bit_or(allow) | (coalesce((SELECT * FROM everyone_perms), $3)) & ~bit_or(deny)
FROM all_permissions
"""

"""pypika attempt:"""
q = (Query
	.with_(
		Query.select(rp.permissions).from_(rp).where(rp.entity == entity_id),
		'everyone_perms')
	.with_(
			Query.select(
				rp.permissions,
				Term(0).as_('allow'),
				Term(0).as_('deny'))
			.from_(rp)
			.where(rp.entity.isin(role_ids))
		.union_all(
			Query.select(
				Term(0).as_('permissions'),
				pp.allow,
				pp.deny)
			.from_(pp)
			.where(pp.entity.isin(role_ids) | pp.page_id == entity_id)),
		'all_permissions')
	.select(
		bit_or('permissions') | bit_or('allow') | bit_or('deny') | Coalesce(Query.select(pypika.Table('everyone_perms').star).from_(pypika.Table('everyone_perms')), default_permissions) & ~bit_or('deny'))
	.from_('all_permissions'))

print(q)
