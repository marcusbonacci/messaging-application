CREATE TABLE users_status (
    status_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    description VARCHAR(15)
);

CREATE TABLE requests_status (
    status_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    description VARCHAR(15)
);

CREATE TABLE audience_types (
    type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    description VARCHAR(15)
);

CREATE TABLE users (
    user_id uuid NOT NULL DEFAULT uuidv7(),
    status_id INT NOT NULL DEFAULT 1,
    username VARCHAR(30) UNIQUE NOT NULL,
    display_name VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id),
    FOREIGN KEY (status_id) REFERENCES users_status(status_id)
);

CREATE TABLE friend_requests (
    sender uuid NOT NULL,
    reciever uuid NOT NULL,
    status_id INT NOT NULL DEFAULT 1,

    PRIMARY KEY (sender, reciever),
    FOREIGN KEY (sender) REFERENCES users(user_id),
    FOREIGN KEY (reciever) REFERENCES users(user_id),
    FOREIGN KEY (status_id) REFERENCES requests_status(status_id)
);

CREATE TABLE friends (
    user_a_id uuid NOT NULL,
    user_b_id uuid NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CHECK (user_a_id <> user_b_id),
    CHECK (user_a_id < user_b_id),

    PRIMARY KEY (user_a_id, user_b_id),
    FOREIGN KEY (user_a_id) REFERENCES users(user_id),
    FOREIGN KEY (user_b_id) REFERENCES users(user_id)
);

CREATE TABLE audience (
    audience_id uuid NOT NULL DEFAULT uuidv7(),
    type_id INT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT NULL,

    PRIMARY KEY (audience_id),
    FOREIGN KEY (type_id) REFERENCES audience_types(type_id)
);

CREATE TABLE memberships (
    audience_id uuid NOT NULL,
    user_id uuid NOT NULL,
    joined_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (audience_id, user_id)
);