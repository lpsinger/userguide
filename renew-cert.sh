#!/bin/sh
# Renew the robot certificate from the Kerberos keytab.
set -e
X509_USER_CERT="$HOME/.globus/usercert.pem"
X509_USER_KEY="$HOME/.globus/userkey.pem"
X509_USER_PROXY="$HOME/.globus/userproxy.pem"
KERBEROS_KEYTAB="${HOME}/.globus/krb5.keytab"
KERBEROS_PRINCIPAL="$(klist -k "${KERBEROS_KEYTAB}" | tail -n 1 | sed 's/.*\s//')"
kinit "${KERBEROS_PRINCIPAL}" -k -t "${KERBEROS_KEYTAB}"
ligo-proxy-init -k > /dev/null
cp "${X509_USER_PROXY}" "${X509_USER_CERT}"
cp "${X509_USER_PROXY}" "${X509_USER_KEY}"
