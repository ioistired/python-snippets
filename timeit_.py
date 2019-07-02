import timeit as _timeit, math, sys

def _format_time(timespan, precision=3):
	if timespan >= 60.0:
		parts = [('d', 60*60*24),('h', 60*60),('min', 60), ('s', 1)]
		time = []
		leftover = timespan
		for suffix, length in parts:
			value = int(leftover / length)
			if value > 0:
				leftover = leftover % length
				time.append(f'{value}{suffix}')
			if leftover < 1:
				break
		return ' '.join(time)

	units = ['s', 'ms', 'us', 'ns']
	scaling = [1, 1e3, 1e6, 1e9]

	if timespan > 0.0:
		order = min(-int(math.floor(math.log10(timespan)) // 3), 3)
	else:
		order = 3
	return f"{timespan * scaling[order]:.{precision-1}f} {units[order]}"

def timeit(stmt, setup='pass', repeat=7, number=0, precision=3):
	timer = _timeit.Timer(stmt, setup)

	if number == 0:
		for index in range(0, 10):
			number = 10 ** index
			time_number = timer.timeit(number)
			if time_number >= 0.2:
				break

	all_runs = timer.repeat(repeat, number)
	best = min(all_runs) / number
	worst = max(all_runs) / number

	if worst > 4 * best and best > 0 and worst > 1e-6:
		print(f"The slowest run took {worst/best:0.2f} times longer than the "
			  "fastest. This could mean that an intermediate result "
			  "is being cached.")

	fmt = "{mean} {pm} {std} per loop (mean {pm} std. dev. of {runs} run{run_plural}, {number} loop{loop_plural} each)"
	timings = [ dt / number for dt in all_runs]
	average = lambda: math.fsum(timings) / len(timings)
	stdev = lambda: (math.fsum([(x - average()) ** 2 for x in timings]) / len(timings)) ** 0.5
	pm = '+-'
	if getattr(sys.stdout, 'encoding', None):
		try:
			'\xb1'.encode(sys.stdout.encoding)
			pm = '\xb1'
		except:
			pass

	print(fmt.format(pm = pm, runs = repeat, number = number,
		loop_plural = "" if number == 1 else "s",
		run_plural = "" if repeat == 1 else "s",
		mean = _format_time(average(), precision),
		std = _format_time(stdev(), precision)))
