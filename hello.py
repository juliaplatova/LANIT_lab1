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
	name = input("Enter your name: ").strip()
	if name == "":
		name = "unknown"

	if len(_sys.argv) > 1:
		message = message[:]
	else:
		message = "".join([c for c in message])

	print(message + " from @" + name)


if __name__ == "__main__":
	main()
