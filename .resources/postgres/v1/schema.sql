CREATE TABLE IF NOT EXISTS users_status (
    status_id SERIAL NOT NULL,
    description VARCHAR(15),

    PRIMARY KEY (status_id)
);

CREATE TABLE IF NOT EXISTS friends_status (
    status_id SERIAL NOT NULL,
    description VARCHAR(15),

    PRIMARY KEY (status_id)
);

CREATE TABLE IF NOT EXISTS users (
    user_id uuid NOT NULL DEFAULT uuidv7(),
    username VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(45) UNIQUE NOT NULL,
    status INT NOT NULL DEFAULT 1,
    description VARCHAR(55),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id),
    FOREIGN KEY (status) REFERENCES users_status(status_id)
);

CREATE TABLE IF NOT EXISTS friends (
    user_a_id uuid NOT NULL,
    user_b_id uuid NOT NULL,
    status INT NOT NULL DEFAULT 1,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_a_id, user_b_id),
    FOREIGN KEY (user_a_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (user_b_id) REFERENCES users(user_id) ON DELETE CASCADE,

    CHECK (user_a_id <> user_b_id),
    CHECK (user_a_id < user_b_id)
);

CREATE TABLE IF NOT EXISTS audience (
    audience_id uuid NOT NULL DEFAULT uuidv7(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(audience_id)
);

CREATE TABLE IF NOT EXISTS audience_viewer (
    audience_publisher uuid NOT NULL,
    audience_subscriber uuid NOT NULL,

    PRIMARY KEY(audience_publisher, audience_subscriber)
);