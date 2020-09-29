#!/bin/sh

install () {
	src="`basename $(pwd)`"
	if [ `id -u` -eq 0 ]; then
		bin="/usr/local/bin"
		dst="/opt/${src}"
	else
		bin="${HOME}/bin"
		dst="${bin}/${src}"
	fi

	echo "[+] Installing files..."
	sleep 1
	mkdir -p "${dst}" &&
	cp -a *.py "${dst}" &&
	cd "${dst}" &&
	chmod 700 price_tracker.py &&
	ln -sf "${dst}/price_tracker.py" "${bin}/price_tracker"
}

install && echo '[+] All done.' || echo '[-] Installation failed.'
