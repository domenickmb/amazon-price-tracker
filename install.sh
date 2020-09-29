#!/bin/bash

install () {
	src="`basename $(pwd)`"
	if [ `id -u` -eq 0 ]; then
		# Set the variables for system-wide installation. /opt/$src will be created where the scripts
		# will reside and a symlink of the main script will be created inside /usr/local/bin directory
		bin="/usr/local/bin"
		dst="/opt/${src}"

	else
		# Set the variables for 'user only' installation. A subdirectory inside ~/bin will be created
		# where the scripts will reside and a symlink of the main script will be created inside ~/bin
		bin="${HOME}/bin"
		dst="${bin}/${src}"

		if [[ ! "$PATH" =~ "$bin" ]]; then
			echo 'PATH=$HOME/bin:$PATH' >> ~/.bashrc
		fi

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
