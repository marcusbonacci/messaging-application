# Messaging Application Requirements

Basic Requirements:

- Users should be able to send messages through audiences.
- Users should be able to send friend_requests, and have friends.
- Messages should use UUIDv7, and be stored in a nosql database.
- Metrics on users, audiences, and groups should be stored somehow.

### Audience
An audience can be one or multiple people / groups that can subscribe to a channel.
Audiences are a logical partition / separation of concerns.

Example:

Each message sent will have a target audience.

UserA - UserB:

UserA sends a message to an audience, Any user in said audience (A & B) will be subscribed to the audience, and recieve any published messages.

Audiences will allow users to send messages to numerous people / groups at once.

If a user is in a group, they're subscribed to said audience.

### Messages

Messages will be stored by audience_id using a MongoDB (TBD), like so:

#### message object (json)

message_id: uuidv7 (fk)
audience_id: uuidv7 (fk)
sender_id: uuidv7 (fk)
created_at: timestamptz @ utc
updated_at: timestamptz @ utc