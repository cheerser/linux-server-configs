```sql
CREATE TABLE users (
  "username" varchar(255) NOT NULL,
  "domain" varchar(255) NOT NULL,
  "password" varchar(255) NOT NULL,
  "createdAt" timestamp NOT NULL default CURRENT_TIMESTAMP
);
```