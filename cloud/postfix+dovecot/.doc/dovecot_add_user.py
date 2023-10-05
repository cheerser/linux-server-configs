import click

'''
CREATE TABLE users (
  "name" varchar(255) NOT NULL,
  "domain" varchar(255) NOT NULL,
  "password" varchar(255) NOT NULL,
  "createdAt" timestamp NOT NULL default CURRENT_TIMESTAMP
);
'''

import subprocess

import psycopg


@click.command()
@click.argument('user')
@click.argument('password')
def main(user, password):
    name, domain = user.split('@')
    proc = subprocess.run(f'doveadm pw -s SHA512-CRYPT -p {password}'.split(), capture_output=True)
    hashed_password = proc.stdout.rstrip()

    with psycopg.connect("dbname=mail user=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users(name, domain, password) VALUES (%s, %s, %s)",
                (name, domain, hashed_password.decode())
            )
        conn.commit()


if __name__ == '__main__':
    main()