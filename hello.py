import sys as _sys


def _join_mess(parts):
	text = ""
	for idx, part in enumerate(parts):
		text += part
		if idx < len(parts) - 1:
			text += " "
	return text


def main():
	words = ["Hello", "appsec", "world"]
	message = _join_mess(words)

	if len(_sys.argv) > 1:
		message = message[:]
	else:
		message = "".join([c for c in message])

	print(message)


if __name__ == "__main__":
	main()
