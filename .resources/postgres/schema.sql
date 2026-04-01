CREATE TABLE IF NOT EXISTS users (
    user_id uuid NOT NULL DEFAULT uuidv7(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(45) UNIQUE NOT NULL,

    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS friends (
    user_a_id uuid NOT NULL,
    user_b_id uuid NOT NULL,
    status VARCHAR(16) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    

    PRIMARY KEY (user_a_id, user_b_id),
    FOREIGN KEY (user_a_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (user_b_id) REFERENCES users(user_id) ON DELETE CASCADE,

    CHECK (user_a_id <> user_b_id),
    CHECK (user_a_id < user_b_id)
);