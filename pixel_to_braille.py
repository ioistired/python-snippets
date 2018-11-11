"""
void lwTranslatePixelsGroup(int byte, char *output) {
    int code = 0x2800 + byte;
    /* Convert to unicode. This is in the U0800-UFFFF range, so we need to
     * emit it like this in three bytes:
     * 1110xxxx 10xxxxxx 10xxxxxx. */
    output[0] = 0xE0 | (code >> 12);          /* 1110-xxxx */
    output[1] = 0x80 | ((code >> 6) & 0x3F);  /* 10-xxxxxx */
    output[2] = 0x80 | (code & 0x3F);         /* 10-xxxxxx */
}
"""

def translate_pixel_group(byte):
	output = bytearray(3)
	code = 0x2800 + byte
	output[0] = 0xE0 | (code >> 12)
	output[1] = 0x80 | ((code >> 6) & 0x3F)
	output[2] = 0x80 | (code & 0x3F)
	return output.decode('utf-8')
