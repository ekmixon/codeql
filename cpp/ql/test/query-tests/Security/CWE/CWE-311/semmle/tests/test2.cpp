
#define FILE int

int fprintf(FILE *stream, const char *format, ...);
char *strcpy(char *s1, const char *s2);

char *crypt(char *input);

struct myStruct
{
	// sensitive
	char *password;
	char *thepasswd;
	char *accountkey;

	// encrypted
	char password_hash[64];
	char *encrypted_passwd;

	// not sensitive
	char *password_file;
	int num_passwords;
	bool have_passwd;

	// dubious
	char *passwd_config;
};

char *getPassword();
char *getPasswordHash();
int getPasswordMaxChars();

void tests(FILE *log, myStruct &s)
{
	fprintf(log, "password = %s\n", s.password); // BAD
	fprintf(log, "thepasswd = %s\n", s.thepasswd); // BAD
	fprintf(log, "accountkey = %s\n", s.accountkey); // DUBIOUS [NOT REPORTED]
	fprintf(log, "password_hash = %s\n", s.password_hash); // GOOD
	fprintf(log, "encrypted_passwd = %s\n", s.encrypted_passwd); // GOOD
	fprintf(log, "password_file = %s\n", s.password_file); // GOOD
	fprintf(log, "passwd_config = %s\n", s.passwd_config); // DUBIOUS [REPORTED]
	fprintf(log, "num_passwords = %i\n", s.num_passwords); // GOOD
	fprintf(log, "have_passwd = %i\n", s.have_passwd); // GOOD

	fprintf(log, "getPassword() = %i\n", getPassword()); // BAD
	fprintf(log, "getPasswordHash() = %i\n", getPasswordHash()); // GOOD
	fprintf(log, "getPasswordMaxChars() = %i\n", getPasswordMaxChars()); // GOOD

	{
		char *cpy1 = s.password;
		char *cpy2 = crypt(s.password);

		fprintf(log, "cpy1 = %s\n", cpy1); // BAD
		fprintf(log, "cpy2 = %s\n", cpy2); // GOOD
	}

	{
		char buf[1024];

		strcpy(buf, s.password);
		fprintf(log, "buf = %s\n", buf); // BAD [NOT DETECTED]
		
		strcpy(buf, s.password_hash);
		fprintf(log, "buf = %s\n", buf); // GOOD
	}
}
