#  similar to
# https://github.com/TildeBeta/6X/blob/35baeeecc0c44361d1359bca00d95abc48da8581/sixx/plugins/core.py#L11-L34

intervals = (
	('week', 60 * 60 * 24 * 7),
	('day', 60 * 60 * 24),
	('hour', 60 * 60),
	('minute', 60),
	('second', 1),
)

def natural_time(seconds) -> str:
	message = []
	for name, divisor in intervals:
		n, seconds = divmod(seconds, divisor)

		if n == 0:
			continue

		message.append(f'{n} {name}{"s" if n != 1 else ""}')

	return ' '.join(message)
