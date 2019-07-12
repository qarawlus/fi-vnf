import socket

msg = "Return-Path: <noreply@uni-paderborn.de>\n\
Received: from telepax.uni-paderborn.de (telepax.uni-paderborn.de [131.234.189.14])\n\
	 by mail.uni-paderborn.de (Cyrus 3.0.10) with LMTPA;\n\
	 Tue, 18 Jun 2019 15:18:10 +0200\n\
X-Cyrus-Session-Id: cyrus-227659-1560863890-1-9203275373212007459\n\
X-Sieve: CMU Sieve 3.0\n\
Received: from paul-mail2.uni-paderborn.de ([131.234.157.142] helo=CN-AP02)\n\
	by mail.uni-paderborn.de with esmtp (Exim 4.89 telepax)\n\
	id 1hdE01-0006yl-60\n\
	for qaarawlus@mail.uni-paderborn.de; Tue, 18 Jun 2019 15:18:09 +0200\n\
MIME-Version: 1.0\n\
From: noreply@uni-paderborn.de\n\
To: qaarawlus@mail.uni-paderborn.de\n\
Date: 18 Jun 2019 15:18:09 +0200\n\
Subject: (L.079.05807/FI) Reminder: miniproject intermediate presentation\n\
 tomorrow\n\
Content-Type: text/plain; charset=iso-8859-1\n\
Content-Transfer-Encoding: quoted-printable\n\
Message-Id: <E1hdE01-0006yl-60.1L@mail.uni-paderborn.de>\n\
X-Envelope-To: qaarawlus@mail.uni-paderborn.de\n\
X-IMT-Authenticated-Sender: \n\
Hi, =0D=0A=0D=0Asmall reminder: tomorrow intermediate project reminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectreminder: tomorrow intermediate projectpre=\n\
sentation. =0D=0A=0D=0ANO homework discussions tomorrow! =0D=0A=0D=0A=\n\
best=0D=0A=0D=0AHK\n\
"

s = socket.socket()
s.connect(('10.0.0.2', 25))
s.send(bytes(msg, 'UTF-8'))
data = s.recv(1024)
print(data)
s.close()
