import io
import requests
import typing

class RemoteFile(typing.BinaryIO):
	def __init__(self, url):
		self.url = url
		self.session = requests.Session()
		self._content_length = None
		self.pos = 0

	def _fetch_content_length(self):
		self._content_length = self.session.head(self.url).headers['Content-Length']

	def read(self, size=-1):
		# TODO support If-Range
		if size == -1 and self._content_length is None:
			self._fetch_content_length()

		start = self.tell()
		end = '' if size == -1 else start + size - 1
		range_header = f'bytes={start}-{end}'

		r = self.session.get(self.url, headers={'Range': range_header})
		if r.status_code == 200:
			raise OSError('range requested but the whole file was returned')
		elif r.status_code == 416:
			raise OSError('requested range not satisfiable')
		elif r.status_code != 206:  # Partial content
			raise OSError('got unexpected status code', r.status_code)

		buf = r.content
		self.pos += len(buf)
		return buf

	def seek(self, offset, whence=io.SEEK_SET):
		old_pos = self.tell()

		if whence == io.SEEK_SET:
			if offset < 0:
				raise ValueError('negative seek value')
			self.pos = offset
		elif whence == io.SEEK_CUR:
			self.pos += offset
		elif whence == io.SEEK_END:
			if self._content_length is None:
				self._fetch_content_length()
			self.pos = self._content_length + offset

		if self.pos < 0:
			self.pos = old_pos
			raise OSError('new position would be negative')

	def __repr__(self):
		return f'{type(self).__qualname__}({self.url!r})'

	def tell(self):
		return self.pos

	def writable(self):
		return False

	def seekable(self):
		return True

	def write(self):
		raise OSError('read only file')

	def truncate(self, size=None):
		raise OSError('read only file')

	def __enter__(self):
		return self

	def __exit__(self, *excinfo):
		self.session.close()
