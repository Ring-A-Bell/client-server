# Simple Client in a Client-Server System

## Introduction

This project implements a simple client in a client-server system. The client connects to a Group Coordinator Daemon (GCD), receives a list of potential group members, sends a message to each member, prints their response, and then exits.

## Details

- Written in Python 3 using the built-in Python socket library
- Developed and tested on *cs2.seattleu.edu*
- Handed in on *cs1.seattleu.edu*

---

## Usage

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to start the client:

`python client.py <hostname> <port>`

Replace <hostname> and <port> with the hostname and port of the Group Coordinator Daemon (GCD) respectively. For example:

`python client.py cs2.seattleu.edu 23600`

## Details

- Use an `AF_INET` type socket with `SOCK_STREAM` protocol.
- The message to send to the GCD is just the text `JOIN`.
- The GCD and other group members expect all messages to come in as a pickled byte stream: `pickle.dumps('JOIN')`
- The return value from the GCD `JOIN` message will be a pickled bit stream of a list of dicts with keys '`host`' and '`port`'.
- The message to send to the other group members is just the text `HELLO` (also pickled).
- Set the connection timeout to `1500ms` for the group members you are trying to `HELLO` and handle timeouts and other failures gracefully, proceeding on to other group members.

## Testing

- A testing GCD is running at port `23600` on host *cs2.seattleu.edu*.

> Note: Ensure that Python 3 is installed on your system.
