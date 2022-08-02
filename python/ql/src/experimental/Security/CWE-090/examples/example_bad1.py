from flask import request, Flask
import ldap


@app.route("/normal")
def normal():
    unsafe_dc = request.args['dc']
    unsafe_filter = request.args['username']

    dn = f"dc={unsafe_dc}"
    search_filter = f"(user={unsafe_filter})"

    ldap_connection = ldap.initialize("ldap://127.0.0.1")
    user = ldap_connection.search_s(
        dn, ldap.SCOPE_SUBTREE, search_filter)
