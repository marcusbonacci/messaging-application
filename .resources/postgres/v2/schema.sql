CREATE TABLE users_status (
    status_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    description VARCHAR(15)
);

CREATE TABLE users (
    user_id uuid PRIMARY KEY DEFAULT uuidv7(),
    status_id INT NOT NULL REFERENCES users_status(status_id),
    username VARCHAR(30) UNIQUE NOT NULL,
    display_name VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);