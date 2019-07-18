import socket

msg = """Return-Path: <haydar.qarawlus@web.de>
Received: from telepax.uni-paderborn.de (telepax.uni-paderborn.de [131.234.189.14])
	 by mail.uni-paderborn.de (Cyrus 3.0.10) with LMTPA;
	 Thu, 18 Jul 2019 22:39:29 +0200
X-Cyrus-Session-Id: cyrus-181255-1563482369-1-12597894566696012387
X-Sieve: CMU Sieve 3.0
Received: from moooout.web.de ([212.227.17.12])
	by mail.uni-paderborn.de with esmtps (TLS1.2:ECDHE_RSA_AES_128_GCM_SHA256:128)
	(Exim 4.89 telepax)
	id 1hoDBV-0005x3-51
	for qarawlus@mail.upb.de; Thu, 18 Jul 2019 22:39:27 +0200
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=web.de;
	s=dbaedf251592; t=1563482364;
	bh=un3hhjanqAIUrSORb1JxSnZnmea5o6blcVNw/xYwiBQ=;
	h=X-UI-Sender-Class:From:To:Subject:Date;
	b=pA0JkZlxnHH4yNQMe/GEQrdZaxi0LE3/GsqlF9188dYE7GW/Wkp7YypbpmzY0/+Je
	 6Lc4FROfeXrq9I54g6H1p6+cjFtN2eFfcYZwE4juLLkwwnIzSpiuNkZTnmNs6iJHB3
	 kO3V3AOLevZhP6Hjb8n1Wf5IIgLasDt6DcPmvM48=
X-UI-Sender-Class: c548c8c5-30a9-4db5-a2e7-cb6cb037b8f9
Received: from [89.247.126.219] ([89.247.126.219]) by web-mail.web.de
 (3c-app-webde-bap32.server.lan [172.19.172.32]) (via HTTP); Thu, 18 Jul
 2019 22:39:24 +0200
MIME-Version: 1.0
Message-ID: <trinity-8b95cd3b-733f-4bbb-b8a1-6501c96d5f28-1563482364371@3c-app-webde-bap32>
From: haydar.qarawlus@web.de
To: qarawlus@mail.upb.de
Subject: Spam email
Content-Type: text/html; charset=UTF-8
Date: Thu, 18 Jul 2019 22:39:24 +0200
Importance: normal
Sensitivity: Normal
X-Priority: 3
X-Provags-ID: V03:K1:sXujXP6zY4A4oUQK03tOdDo4nTtmn81DJ9IFNMIwtrC/QTXHyQkSAr31LTUKrwvETRdFx
 BXM6HiegEpc+yS+aFFquSNRdpsNXC5Q9S906ieB766CkaGGv6DtlAB9UPow+ZSrpLKebli05RFjr
 gzRcReFVsSm81rSDEXK2635E18czcNemSGRWZgIVc0DbwCP7TnCYQDRPa80azWBESUgTHTb6PpuZ
 n+D/WsxJeE3OBmqnvVTxJqAmFHjlVH3gA9zo+pK0cZxr7BB/ZA0OwBMSP9KXIlbhwh1zqJTLgA0d
 3A=
X-Spam-Flag: NO
X-UI-Out-Filterresults: notjunk:1;V03:K0:c+DsefLROfo=:C5yliudjWB5rJFoxWy6oXB
 OyW2ia2h86J0mZy6rbDIlD2gqTKq8gk/l0FNKXOHDvr+/CYu2q1L/VWAgIvCIlT/1okOk85F0
 mL7yfkXzX7xNxv9l82RtyfvBGF1seyTUxHhngzHlQHN3XxfHpzWAdFxEhrTdM1xHfRolQttwR
 Z832SCk5KBxvTwKVH/wI0Rd/GXqtsexke0pGyglUPqEtZlCypGonfhhR7EvD+fR9YcvUuV2lX
 JM1MsE+pIPkZzFyuc4HnE5fdWxuzMOluD/xAesjqe/Rti7fESwi6CiM1sWPXkW2M3+w/288Lm
 lgUQceFRYkROxtzDzsZ4FGXHsbhGL564/ZzyydUXSoboDrZInFn6rSFFaYTQ49F+QWxGJuzo6
 QX84tV7GIO/pzLlHzTmQFVbr7N7dr68nY5McvGKJjcy4LrOUS7LZhUOCGOivZ0DxCJcE2Dte/
 wZtbRES26DCwmtGvIPX7RoNp9/7szMTlDhO8NV8hkel603IrWfncJiNP5sF/0Oy1IQ7truKRs
 psDTr1fVCakVg7r67cnjxUsKTkRcvmrYc1FJATX1U97A6tiDyxzDHPLIcIqsikFM2MGADL90U
 Co/dp1N6P5OeQkHVjQAHh4nZf6IBTk5pYezZqs9ML2g6+IuHH8nH/ipQ==
X-DKIM: DKIM passed: (address=haydar.qarawlus@web.de domain=web.de), signature is good.
X-IMT-Spam-Score: 1.7 (+)
X-Sophos-SenderHistory: ip=212.227.17.12,fs=43673394,da=51091440,mc=47255,sc=758,hc=46497,sp=1,fso=51091062,re=17,sd=1,hd=0
X-PMX-Version: 6.4.6.2792898, Antispam-Engine: 2.7.2.2107409, Antispam-Data: 2019.7.18.203017, AntiVirus-Engine: 5.63.0, AntiVirus-Data: 2019.7.12.5630001
X-PerlMx-Spam: Gauge=XIIIIIII, Probability=17%, Report='
  CTYPE_JUST_HTML 0.848, PRIORITY_NO_NAME 0.716, HTML_70_90 0.1, HTML_NO_HTTP 0.1, RCVD_FROM_IP_DATE 0.1, BODYTEXTH_SIZE_10000_LESS 0, BODY_SIZE_1000_LESS 0, BODY_SIZE_2000_LESS 0, BODY_SIZE_200_299 0, BODY_SIZE_5000_LESS 0, BODY_SIZE_7000_LESS 0, DKIM_SIGNATURE 0, DQ_S_H 0, INVALID_MSGID_NO_FQDN 0, NO_CTA_URI_FOUND 0, NO_REAL_NAME 0, NO_URI_FOUND 0, NO_URI_HTTPS 0, SMALL_BODY 0, WEBMAIL_SOURCE 0, __BODY_NO_MAILTO 0, __BODY_TEXT_X4 0, __CT 0, __CTYPE_HTML 0, __CTYPE_IS_HTML 0, __DKIM_ALIGNS_2 0, __DQ_IP_FSO_LARGE 0, __DQ_S_HIST_1 0, __DQ_S_HIST_2 0, __DQ_S_IP_HD_0 0, __DQ_S_IP_MC_100_P 0, __DQ_S_IP_MC_10_P 0, __DQ_S_IP_MC_1K_P 0, __DQ_S_IP_MC_5_P 0, __DQ_S_IP_SC_1_P 0, __DQ_S_IP_SD_1_P 0, __HAS_FROM 0, __HAS_HTML 0, __HAS_MSGID 0, __HAS_X_PRIORITY 0, __HTML_TAG_DIV 0, __MIME_HTML 0, __MIME_HTML_ONLY 0, __MIME_TEXT_H 0, __MIME_TEXT_H1 0, __MIME_VERSION 0, __PHISH_SPEAR_HTTP_RECEIVED 0,
  __PHISH_SPEAR_STRUCTURE_1 0, __PHISH_SPEAR_SUBJ_SUBJECT 0, __SANE_MSGID 0, __SUBJ_ALPHA_END 0, __TAG_EXISTS_HTML 0, __TO_MALFORMED_2 0, __TO_NO_NAME 0'
X-Envelope-To: qarawlus@mail.upb.de
X-IMT-Authenticated-Sender: 

<html><head></head><body><div style="font-family: Verdana;font-size: 12.0px;"><div>This is a spam email<br/>
&nbsp;</div>

<div class="signature">Mit freundlichen Gr&uuml;&szlig;en<br/>
Haydar Qarawlus</div></div></body></html>"""

s = socket.socket()
s.connect(('10.0.0.2', 25))
while True:
	s.send(bytes(msg, 'UTF-8'))
	# data = s.recv(1024)
	# print(data)
# s.close()
